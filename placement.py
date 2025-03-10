class PlacementApp:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_graduation_years(self):
        query = "SELECT DISTINCT graduation_year FROM Students ORDER BY graduation_year DESC"
        result = self.db_connection.execute_query(query)
        return [r[0] for r in result]

    def filter_eligible_students(self, problems_solved, soft_skills_score, mock_interview_score, leadership_score,
                                 internships_completed, certifications_earned, programming_language, placement_status,
                                 interview_rounds_cleared, graduation_year):
        query = '''
        SELECT S.name, S.age, S.gender, S.email, S.phone, S.graduation_year, P.problems_solved, SS.communication, SS.teamwork, SS.presentation, 
               PL.mock_interview_score, SS.leadership, PL.internships_completed, P.certifications_earned, P.language, 
               PL.placement_status, PL.interview_rounds_cleared
        FROM Students S
        JOIN Programming P ON S.student_id = P.student_id
        JOIN SoftSkills SS ON S.student_id = SS.student_id
        JOIN Placements PL ON S.student_id = PL.student_id
        WHERE P.problems_solved >= %s 
          AND (SS.communication + SS.teamwork + SS.presentation) / 3 >= %s
          AND PL.mock_interview_score >= %s
          AND SS.leadership >= %s
          AND PL.internships_completed >= %s
          AND P.certifications_earned >= %s
          AND P.language = %s
          AND PL.placement_status = %s
          AND PL.interview_rounds_cleared >= %s
          AND S.graduation_year = %s
        '''
        return self.db_connection.execute_query(query, (problems_solved, soft_skills_score, mock_interview_score, leadership_score, 
                                                        internships_completed, certifications_earned, programming_language, 
                                                        placement_status, interview_rounds_cleared, graduation_year))

    def show_insights(self):
        queries = {
            "Avg Programming Performance per Batch": "SELECT course_batch, AVG(problems_solved) FROM Students JOIN Programming ON Students.student_id = Programming.student_id GROUP BY course_batch;",
            "Top 5 Problem Solvers": "SELECT name, problems_solved FROM Students JOIN Programming ON Students.student_id = Programming.student_id ORDER BY problems_solved DESC LIMIT 5;",
            "Highest Soft Skills Scores": "SELECT name, (communication + teamwork + presentation + leadership + critical_thinking + interpersonal_skills) AS soft_skills_total FROM Students JOIN SoftSkills ON Students.student_id = SoftSkills.student_id ORDER BY soft_skills_total DESC LIMIT 5;",
            "Most Internships Completed": "SELECT name, internships_completed FROM Students JOIN Placements ON Students.student_id = Placements.student_id ORDER BY internships_completed DESC LIMIT 5;",
            "Placement Rate per Batch": "SELECT course_batch, COUNT(*) AS total_students, SUM(CASE WHEN placement_status='Placed' THEN 1 ELSE 0 END) AS placed_students, (SUM(CASE WHEN placement_status='Placed' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS placement_rate FROM Students JOIN Placements ON Students.student_id = Placements.student_id GROUP BY course_batch;",
            "Avg Placement Package per Batch": "SELECT course_batch, AVG(placement_package) FROM Students JOIN Placements ON Students.student_id = Placements.student_id WHERE placement_status='Placed' GROUP BY course_batch;",
            "Top 5 Mock Interview Scores": "SELECT name, mock_interview_score FROM Students JOIN Placements ON Students.student_id = Placements.student_id ORDER BY mock_interview_score DESC LIMIT 5;",
            "Most Interview Rounds Cleared": "SELECT name, interview_rounds_cleared FROM Students JOIN Placements ON Students.student_id = Placements.student_id ORDER BY interview_rounds_cleared DESC LIMIT 5;",
            "Best Leadership Scores": "SELECT name, leadership FROM Students JOIN SoftSkills ON Students.student_id = SoftSkills.student_id ORDER BY leadership DESC LIMIT 5;"
        }
        return queries
