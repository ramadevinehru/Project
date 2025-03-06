import mysql.connector
from faker import Faker
import random

fake = Faker()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789'
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS placement")

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='placement'
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender VARCHAR(50),
        email VARCHAR(255),
        phone VARCHAR(50),
        enrollment_year INT,
        course_batch VARCHAR(100),
        city VARCHAR(100),
        graduation_year INT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Programming (
        programming_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        language VARCHAR(100),
        problems_solved INT,
        assessments_completed INT,
        mini_projects INT,
        certifications_earned INT,
        latest_project_score INT,
        FOREIGN KEY(student_id) REFERENCES Students(student_id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS SoftSkills (
        soft_skill_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        communication INT,
        teamwork INT,
        presentation INT,
        leadership INT,
        critical_thinking INT,
        interpersonal_skills INT,
        FOREIGN KEY(student_id) REFERENCES Students(student_id)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Placements (
        placement_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        mock_interview_score INT,
        internships_completed INT,
        placement_status VARCHAR(100),
        company_name VARCHAR(255),
        placement_package FLOAT,
        interview_rounds_cleared INT,
        placement_date DATE,
        FOREIGN KEY(student_id) REFERENCES Students(student_id)
    );
''')

conn.commit()

def insert_fake_data(n=1000):
    courses = ["Cybersecurity", "AIML", "CSE", "DataScience", "Robotics", "SoftwareEng", "IT"]
    for _ in range(n):
        name = fake.name()
        age = random.randint(20, 25)
        gender = random.choice(["Male", "Female", "Other"])
        email = fake.email()
        phone = fake.phone_number()
        enrollment_year = random.randint(2018, 2023)
        course_name = random.choice(courses)
        course_batch = f"{course_name}{enrollment_year}"
        city = fake.city()
        graduation_year = enrollment_year + 4
       
        cursor.execute("""
            INSERT INTO Students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))
        conn.commit()
        student_id = cursor.lastrowid
       
        cursor.execute("""
            INSERT INTO Programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (student_id, random.choice(["Python", "SQL", "Java"]), random.randint(10, 100), random.randint(1, 10), random.randint(1, 5), random.randint(0, 5), random.randint(50, 100)))
       
        cursor.execute("""
            INSERT INTO SoftSkills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (student_id, random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100)))
       
        cursor.execute("""
            INSERT INTO Placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (student_id, random.randint(50, 100), random.randint(0, 3), random.choice(["Ready", "Not Ready", "Placed"]), fake.company(), random.uniform(3.0, 12.0), random.randint(1, 5), fake.date_this_decade()))
       
    conn.commit()

insert_fake_data(1000)

conn.close()

