import pandas as pd

data = pd.read_csv("app/generated_database.csv", header=None, names=[
    "First_name", "Last_name", "Age", "Nationality", "Country_of_residence", 
    "Degree", "Graduation_year", "GPA", "Availability", "Looking_for", 
    "Email", "Description", "Additional_information"
])

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce')
data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce')



