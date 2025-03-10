import streamlit as st
import pandas as pd
from database import DatabaseConnection
from placement import PlacementApp
import os
from dotenv import load_dotenv

load_dotenv()

host=os.getenv('HOST')
password=os.getenv('PASSWORD')
user=os.getenv('USER')
database_name=os.getenv('DATABASE_NAME')


def main():
    db_connection = DatabaseConnection(host=host, user=user, password=password, database=database_name)
    app = PlacementApp(db_connection)
    
    st.title("Placement Eligibility Streamlit Application")
    
    problems_solved = st.number_input("Minimum Problems Solved", min_value=0, max_value=100, value=50)
    soft_skills_score = st.number_input("Minimum Soft Skills Score", min_value=50, max_value=100, value=75)
    mock_interview_score = st.slider("Minimum Mock Interview Score", min_value=0, max_value=100, value=50)
    leadership_score = st.slider("Minimum Leadership Score", min_value=0, max_value=100, value=50)
    internships_completed = st.slider("Minimum Internships Completed", min_value=0, max_value=10, value=1)
    certifications_earned = st.slider("Minimum Certifications Earned", min_value=0, max_value=20, value=2)
    programming_language = st.text_input("Preferred Programming Language", "Python")
    placement_status = st.selectbox("Placement Status", ["Placed", "Not Placed"])
    interview_rounds_cleared = st.slider("Minimum Interview Rounds Cleared", min_value=0, max_value=10, value=1)
    graduation_year = st.selectbox("Graduation Year", app.get_graduation_years())
    
    if st.button("Filter Eligible Students"):
        result = app.filter_eligible_students(problems_solved, soft_skills_score, mock_interview_score, leadership_score,
                                              internships_completed, certifications_earned, programming_language,
                                              placement_status, interview_rounds_cleared, graduation_year)
        df = pd.DataFrame(result, columns=["Name", "Age", "Gender", "Email", "Phone", "Graduation Year", "Problems Solved", "Communication", "Teamwork", "Presentation",
                                           "Mock Interview Score", "Leadership", "Internships Completed", "Certifications Earned", 
                                           "Programming Language", "Placement Status", "Interview Rounds Cleared"])
        st.dataframe(df)
    
    if st.button("Show Insights"):
        queries = app.show_insights()
        for title, query in queries.items():
            st.subheader(title)
            df = pd.DataFrame(app.db_connection.execute_query(query))
            st.dataframe(df)
    
    db_connection.close()

if __name__ == "__main__":
    main()
