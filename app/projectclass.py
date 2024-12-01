import csv
from userclass import User 

class Project:
    def __init__(
        self,
        project_name,
        admin,
        number_of_people,
        keywords,
        project_stage,
        language_spoken,
        start_date,
        completion_estimate_months,
        project_description,
        positions_needed,
        sort_value,
        id_project
     
    ):

        self.project_name = project_name
        self.admin = admin
        self.keywords = keywords
        self.project_stage = project_stage
        self.language_spoken = language_spoken
        self.project_description = project_description
        self.positions_needed = positions_needed         
        self.number_of_people = number_of_people
        self.completion_estimate_months = completion_estimate_months
        self.start_date = start_date
        self.sort_value=sort_value
        self.id_project=id_project
   
    def validate_project_stage(self):
        valid_stages = ["Planning", "Development", "Testing", "Deployment", "Completed"]
        return self.project_stage in valid_stages

    def validate_language_spoken(self):
        return bool(self.language_spoken.strip())
   
    def admin_exists(self):
        user_data = User.load_all_user_data()
        for user in user_data:
            if user["Email"] ==self.admin:
                return True 
        return False  

    
    def save_to_csv(self):
        fieldnames = [
            "Project Name", "Admin", "Number of People", "Keywords",
            "Project Stage", "Language Spoken", "Start Date",
            "Completion Estimate (Months)", "Project Description",
            "Positions Needed", "Sort Value", "id_project"
        ]
        
        projects = []
        project_exists = False

        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["id_project"]) == int(self.id_project):
                        # Si el proyecto ya existe, lo actualizamos
                        project_exists = True
                        row["Project Name"] = self.project_name
                        row["Admin"] = self.admin
                        row["Number of People"] = self.number_of_people
                        row["Keywords"] = self.keywords
                        row["Project Stage"] = self.project_stage
                        row["Language Spoken"] = self.language_spoken
                        row["Start Date"] = self.start_date
                        row["Completion Estimate (Months)"] = self.completion_estimate_months
                        row["Project Description"] = self.project_description
                        row["Positions Needed"] = self.positions_needed
                        row['Sort Value'] = self.sort_value
                        row["id_project"] = self.id_project
                    projects.append(row)  # Agregamos el proyecto al listado
        except FileNotFoundError:
            pass

        if not project_exists:
            # Si el proyecto no existía, lo agregamos como nuevo
            projects.append({
                "Project Name": self.project_name,
                "Admin": self.admin,
                "Number of People": self.number_of_people,
                "Keywords": self.keywords,
                "Project Stage": self.project_stage,
                "Language Spoken": self.language_spoken,
                "Start Date": self.start_date,
                "Completion Estimate (Months)": self.completion_estimate_months,
                "Project Description": self.project_description,
                "Positions Needed": self.positions_needed,
                "Sort Value": self.sort_value,
                "id_project": self.id_project
            })

        with open("generated_project_database.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  
            writer.writerows(projects) 

    @staticmethod
    def load_all_projects_data(UserEmail=None):      
        projects = []
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if UserEmail==None or UserEmail=='':       
                    for row in reader:
                        projects.append(row) 
                else:
                    # Loop through each row in the CSV
                    for row in reader:
                        # Check if the 'Email' field is not empty and matches the filter 
                        if row["Admin"].lower().strip()==UserEmail.lower().strip():
                            projects.append(row)               
        except FileNotFoundError:
            pass
        return projects

    @staticmethod
    def get_project_data_from_csv(id_project):
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["id_project"]) == int(id_project):
                        return row  # Returns the project data
        except FileNotFoundError:
            pass
        return {}
    




