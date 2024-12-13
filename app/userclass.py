# This files is used to define a User class that we use to handle user data, the functionalities that it provides are:
# - Initializing the object (user) and storing user attributes (name, email, password, GPA, age, etc.)
# - Validating user information (email, password, age, date of birth, LinkedIn URL).
# - Hashing passwords for secure storage.
# - Saving user details to a CSV file or updating them if they already exist.
# - Getting user data from the CSV.
# - Implementing a binary search over full names of the users. We will user this for the search feature.
# - Sorting full names alphabetically using a min-heap. We use this for the binary seach. 

import hashlib
import re 
from datetime import datetime  
import csv
import pandas as pd
import heapq

class User:
    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
        description,
        additional_info,
        rating,
        age,
        dob,
        nationality,
        country_residence,
        degree,
        graduation_year,
        gpa,
        availability,
        topics_of_interest,
        user_type,
        linkedin,
        mentor,
        image=None
    ):
        # Initializes a User object with the attributes 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.description = description
        self.additional_info = additional_info       
        self.nationality = nationality
        self.country_residence = country_residence
        self.degree = degree
        self.topics_of_interest = topics_of_interest
        self.user_type = user_type
        self.linkedin = linkedin
        self.mentor = mentor
        self.image = image
        self.dob = dob

        if rating == '' or rating is None:
            self.rating = 0
        else:
            self.rating = rating

        if age == '' or age is None:
            self.age = 0
        else:
            self.age = age

        if graduation_year == '' or graduation_year is None:
            self.graduation_year = 0
        else:
            self.graduation_year = graduation_year

        if gpa == '' or gpa is None:
            self.gpa = 0
        else:
            self.gpa = gpa

        if availability == '' or availability is None:
            self.availability = 0
        else:
            self.availability = availability
    
    def validate_GPA(self):
        # Chechs that the GPA format is corret
        try:
            number = float(self.gpa)
            return True  
        except ValueError:
            return False 

    def validate_email(self):
        # Validates the email format using a regular expression
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email))

    def validate_password(self):
        # Validates the password, pbligating the user to choose a complex password
        return bool(
            re.fullmatch(
                r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$",
                self.password,
            )
        )

    def validate_age(self):
        # Validates that the age is within a range
        try:
            age = int(self.age)
            if age < 18 or age > 120:
                return False
            return True
        except ValueError:
            return False

    def validate_dob(self):
        # Validates the date of birth format. It should be correct as the html only allows the user to input this format.
        try:
            datetime.strptime(self.dob, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_linkedin(self):
        # Validates that the LinkedIn link.
        if self.linkedin and not re.match(r"^(https://www\.linkedin\.com/.*)$", self.linkedin):
            return False
        return True

    def hash_password(self):
        # Hashes the password befor saving to the database.
        return hashlib.sha256(self.password.encode()).hexdigest()

    def save_to_csv(self):
        # Saves the user's data into out database. If the user already exists it updates the record and if it does not it creates a new one, we do that using the email as the key (unique) value.
        fieldnames = [
            "First Name", "Last Name", "Rating", "Age", "DOB", "Nationality", 
            "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability",
            "Topics of Interest", "Email", "Description", "Additional Information", 
            "Sort Value", "Type", "Password", "LinkedIn", "Mentor", "Image"
        ]

        users = []
        email_exists = 0
        try:
            with open("generated_database.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Email"].lower() == self.email.lower():
                        email_exists = 1
                        # Update existing user rcord
                        row["First Name"] = self.first_name
                        row["Last Name"] = self.last_name
                        row["Rating"] = self.rating
                        row["Age"] = self.age
                        row["DOB"] = self.dob
                        row["Nationality"] = self.nationality
                        row["Country of Residence"] = self.country_residence
                        row["Degree"] = self.degree
                        row["Graduation Year"] = self.graduation_year
                        row["GPA"] = self.gpa
                        row["Availability"] = self.availability
                        row["Topics of Interest"] = self.topics_of_interest
                        row["Description"] = self.description
                        row["Additional Information"] = self.additional_info
                        row["Sort Value"] = 0
                        row["Type"] = self.user_type
                        row["Password"] = self.password  
                        row["LinkedIn"] = self.linkedin
                        row["Mentor"] = self.mentor
                        row["Image"] = self.image
                            
                    users.append(row)
        except FileNotFoundError:
            # If file doesn't exist, it will be created.
            pass
        
        # If email does not exist, add a new user entry
        if email_exists == 0:
            users.append({
                "First Name": self.first_name,
                "Last Name": self.last_name,
                "Rating": self.rating,
                "Age": self.age,
                "DOB": self.dob,
                "Nationality": self.nationality,
                "Country of Residence": self.country_residence,
                "Degree": self.degree,
                "Graduation Year": self.graduation_year,
                "GPA": self.gpa,
                "Availability": self.availability,
                "Topics of Interest": self.topics_of_interest,
                "Email": self.email,
                "Description": self.description,
                "Additional Information": self.additional_info,
                "Sort Value": 0,
                "Type": self.user_type,
                "Password": self.hash_password(),
                "LinkedIn": self.linkedin,
                "Mentor": self.mentor,
                "Image": self.image
            })

        with open("generated_database.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  
            writer.writerows(users) 

    @staticmethod
    def email_exists(email):
        # Checks if an email exists in the database.
        user_data = User.load_all_user_data()
        for user in user_data:
            if user["Email"] == email:
                return True 
        return False  

    @staticmethod
    def load_all_user_data():
        # Takes the data stored in the csv file and loads it into a list of dictionaries, we use that instead of a dataframe for the seek of performance.
        user_data = []
        with open("generated_database.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_data.append(row)
        return user_data
    
    @staticmethod 
    def load_mentor_user_data():
        # Loads data of all users who are alumni and also mentors.
        user_data = []
        with open("generated_database.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('Type', '').strip().lower() == 'alumni' and (row.get('Mentor', '').strip().lower() == 'true'):
                    user_data.append(row)
        return user_data
    
    @staticmethod
    def get_user_data_from_csv(email):
        # Retrieves a single user's data by their email from the CSV.
        with open('generated_database.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Email'].lower() == email.lower():
                    return row
        return {}

    @staticmethod
    def full_names(fullname):
        # It first creates the fullnames, sorts them alphabetically, then performs a binary search.
        df = pd.read_csv('generated_database.csv')         
        lst = [f"{df['First Name'].iloc[i]} {df['Last Name'].iloc[i]}" for i in range(len(df["First Name"]))]    
        sorted_lst = User.alphabetical_priority_sort(lst)  
       
        return User.binarysearch(sorted_lst, fullname)
    
    @staticmethod
    def alphabetical_priority_sort(values):
        # Sorts a list of strings alphabetically using a min-heap.
        heapq.heapify(values)
        sorted_values = []
        while values:
            sorted_values.append(heapq.heappop(values))
        return sorted_values

    @staticmethod      
    def binarysearch(fullnameslist, fullname):
        # Performs a binary search on a sorted list of full names to find a given fullname.
        # If the name id found it will return the name, if it is not it will return Nonw.
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
