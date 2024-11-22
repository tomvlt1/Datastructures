import pandas as pd

data = pd.read_csv("generated_database.csv", header=None, names=[
    "First Name", "Last Name", "Rating", "Age", "DOB", "Nationality", 
    "Country of Residence", "Degree", "Graduation Year", "GPA", 
    "Availability", "Topics of Interest", "Email", "Description", 
    "Additional Information", "Sort Value"
])

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce')
data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce')
data['Graduation Year'] = pd.to_numeric(data['Graduation Year'], errors='coerce')






