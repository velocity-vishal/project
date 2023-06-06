# Steps to create SQL script from excel file

1. Clone the repo in local
2. Update the variable as per your need in constant file
3. Create a python virtual environment - `python -m venv venv`
4. Install the dependency through - `pip install -r requirements.txt`
5. Replace the `site-data.csv` file with your csv or excel file for which you want to generate seed script
6. Start the uvicorn server - `uvicorn main:app --reload` 
7. Beutify the SQL script from - `https://codebeautify.org/sqlformatter`
8. Replace 'NULL' with NULL
9. Your SQL script is ready!!
