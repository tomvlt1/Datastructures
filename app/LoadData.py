import pandas as pd

 

#For collaborators I need to send the names of the fields and not send more than necessary

data = pd.read_csv("generated_database.csv", header=None, names=[
    "First Name", "Last Name", "Rating", "Age", "DOB", "Nationality",
    "Country of Residence", "Degree", "Graduation Year", "GPA",
    "Availability", "Topics of Interest", "Email", "Description",
    "Additional Information", "LinkedIn","Sort Value"],low_memory=False)


data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce')

data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce')

data['Graduation Year'] = pd.to_numeric(data['Graduation Year'], errors='coerce')

 




