import hashlib
import re
from datetime import datetime
import csv

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
        image=None
    ):

        self.project_name = project_name
        self.admin = admin
        self.keywords = keywords
        self.project_stage = project_stage
        self.language_spoken = language_spoken
        self.project_description = project_description
        self.positions_needed = positions_needed
        self.image = image

     
        self.number_of_people = self._validate_number(number_of_people)
        self.completion_estimate_months = self._validate_number(completion_estimate_months)


        self.start_date = self._validate_date(start_date)

    def _validate_number(self, value):
        try:
            num = int(value)
            if num < 0:
                raise ValueError
            return num
        except (ValueError, TypeError):
            return 0  

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            return None  # Or set a default date

    def validate_project_name(self):
        return bool(self.project_name.strip())

    def validate_admin(self):
        return bool(self.admin.strip()) and self._validate_email(self.admin)

    def _validate_email(self, email):
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

    def validate_keywords(self):
        return bool(self.keywords.strip())

    def validate_project_stage(self):
        valid_stages = ["Planning", "Development", "Testing", "Deployment", "Completed"]
        return self.project_stage in valid_stages

    def validate_language_spoken(self):
        return bool(self.language_spoken.strip())

    def validate_start_date(self):
        return self.start_date is not None

    def validate_completion_estimate(self):
        return self.completion_estimate_months > 0

    def validate_project_description(self):
        return bool(self.project_description.strip())

    def validate_positions_needed(self):
        return self.positions_needed >= 0

    def is_valid(self):
        return (
            self.validate_project_name() and
            self.validate_admin() and
            self.validate_keywords() and
            self.validate_project_stage() and
            self.validate_language_spoken() and
            self.validate_start_date() and
            self.validate_completion_estimate() and
            self.validate_project_description() and
            self.validate_positions_needed()
        )

    def hash_project_description(self):
        return hashlib.sha256(self.project_description.encode()).hexdigest()

    def save_to_csv(self):
        fieldnames = [
            "Project Name", "Admin", "Number of People", "Keywords",
            "Project Stage", "Language Spoken", "Start Date",
            "Completion Estimate (Months)", "Project Description",
            "Positions Needed", "Image"
        ]

        projects = []
        project_exists = False

        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Project Name"].lower() == self.project_name.lower():
                        # Update existing project
                        project_exists = True
                        row["Admin"] = self.admin
                        row["Number of People"] = self.number_of_people
                        row["Keywords"] = self.keywords
                        row["Project Stage"] = self.project_stage
                        row["Language Spoken"] = self.language_spoken
                        row["Start Date"] = self.start_date
                        row["Completion Estimate (Months)"] = self.completion_estimate_months
                        row["Project Description"] = self.project_description
                        row["Positions Needed"] = self.positions_needed
                        row["Image"] = self.image
                    projects.append(row)
        except FileNotFoundError:
            # File doesn't exist, will create a new one
            pass

        if not project_exists:
            # Add new project
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
                "Image": self.image
            })

        with open("generated_project_database.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(projects)

    @staticmethod
    def load_all_projects_data():
        projects = []
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    projects.append(row)
        except FileNotFoundError:
            pass
        return projects

    @staticmethod
    def get_project_data_from_csv(project_name):
        try:
            with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Project Name"].lower() == project_name.lower():
                        return row  # Returns the project data
        except FileNotFoundError:
            pass
        return {}
    




