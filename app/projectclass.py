# This file is used to define a Project class for managing project's data. The functionalities it creates are:
# - Storing project information (name, admin, keywords, stage, language, etc.).
# - Validating the project stage and language.
# - Checking if the admin (project owner) exists as a user.
# - Saving and updating project data in our database.
# - Loading project data from the database.
# - Implementing search functionality using binary search on project names.

import csv
from userclass import User 
import pandas as pd
import heapq

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
        # Initializes a Project instance with provided details.
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
        self.sort_value = sort_value
        self.id_project = id_project
   
    def validate_project_stage(self):
        # Validates that the project stage is one of the recognized stages.
        valid_stages = ["Planning", "Development", "Testing", "Deployment", "Completed"]
        return self.project_stage in valid_stages

    def validate_language_spoken(self):
        # Validates that the language spoken field is not empty.
        return bool(self.language_spoken.strip())
   
    def admin_exists(self):
        # Checks if the admin's email exists in the user database.
        user_data = User.load_all_user_data()
        for user in user_data:
            if user["Email"] == self.admin:
                return True 
        return False  

    def save_to_csv(self):
        # Saves or updates the project's data into our project database'.
        # If the project already exists, it updates its record if not, creates a new record.
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
                        # If the project already exists, update it.
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
                    projects.append(row)
        except FileNotFoundError:
            # If the file does not exist, it will be created below.
            pass

        if not project_exists:
            # If the project does not exist, create it.
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
        # Loads all projects or filters them by admin email if UserEmail is provided.
        projects = []
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if UserEmail is None or UserEmail == '':
                    for row in reader:
                        projects.append(row)
                else:
                    # If an admin email is provided, return only that admin's projects.
                    for row in reader:
                        if row["Admin"].lower().strip() == UserEmail.lower().strip():
                            projects.append(row)               
        except FileNotFoundError:
            pass
        return projects

    @staticmethod
    def get_project_data_from_csv(id_project):
        # Retrieves and returns a project's data from the CSV by its id_project.
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["id_project"]) == int(id_project):
                        return row
        except FileNotFoundError:
            pass
        return {}
    
    @staticmethod
    def full_names(fullname):
        # Performs the binary search created below.
        df = pd.read_csv('generated_project_database.csv')         
        lst = [f"{df['Project Name'].iloc[i]}" for i in range(len(df["Project Name"]))]    
        sorted_lst = User.alphabetical_priority_sort(lst)  
       
        return User.binarysearch(sorted_lst, fullname)

    @staticmethod
    def alphabetical_priority_sort(values):
        # Sorts a list of project names alphabetically using a min-heap.
        heapq.heapify(values)
        sorted_values = []
        while values:
            sorted_values.append(heapq.heappop(values))
        return sorted_values

    @staticmethod      
    def binarysearch(fullnameslist, fullname):
        # A binary search on a list of names to try to find the inputed project name.
        # If it is found it will return the fullname if not, it will return None.
        if not isinstance(fullnameslist, list):
            return 'No list was provided'
        if not fullnameslist:
            return 'The provided list is empty'    

        start = 0
        end = len(fullnameslist) - 1    
        while start <= end:
            mid = (start + end) // 2        
            if fullnameslist[mid] == fullname:
                return fullnameslist[mid]
            elif fullnameslist[mid] > fullname:
                end = mid - 1
            else:
                start = mid + 1    
        return None    
