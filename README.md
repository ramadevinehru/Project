Placement Eligibility Application

Overview:
This project is a "Placement Eligibility Application" built using "Python, MySQL, and Streamlit". It helps filter students based on various criteria such as programming skills, soft skills, interview performance, and placement status. Additionally, it provides insights into students' placement performance.

Features:
- Database Creation: Automatically creates a MySQL database and necessary tables.
- Fake Data Generation: Uses `Faker` to populate the database with realistic student data.
- Student Eligibility Filtering: Allows users to filter students based on multiple criteria.
- Placement Insights: Generates analytical insights such as:
  - Average programming performance per batch
  - Top problem solvers
  - Best soft skills performers
  - Highest placement packages
  - Placement rate per batch
  Interactive UI: Built with "Streamlit" for an easy-to-use interface.

Technologies Used:
- Python
- MySQL
- Streamlit
- Pandas
- Faker (for generating synthetic data)

Prerequisites:
Ensure you have the following installed:
- Python (>=3.13)
- MySQL Server
- Required Python libraries



Usage:
1. Open the Streamlit web app.
2. Enter the filtering criteria for student eligibility.
3. Click "Filter Eligible Students" to see matching records.
4. Click "Show Insights" to generate various analytical insights.

Database Schema:
### Students Table
Stores student details such as name, age, gender, enrollment year, and graduation year.

### Programming Table
Tracks students' programming language expertise, problems solved, and certifications earned.

### SoftSkills Table
Records soft skills like communication, teamwork, leadership, and presentation.

### Placements Table
Stores placement details such as company name, package, interview rounds cleared, and placement status.

## Contribution
Feel free to contribute by forking the repository and submitting pull requests.

## License
This project is licensed under the MIT License.

## Author
Ramadevi N

