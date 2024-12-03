import hashlib
import re 
from datetime import datetime  
import csv
import pandas as pd
import random

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
    # Initialize text attributes
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
        try:
            number = float(self.gpa)  # Try converting to a float
            return True  # It's a valid number
        except ValueError:
            return False  # Invalid number

    def validate_email(self):
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email)) # returns true or false 

    def validate_password(self):
        return bool(
            re.fullmatch(
                r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$",
                self.password,
            )
        )

    def validate_age(self):
        try:
            age = int(self.age)
            if age < 18 or age > 120:
                return False
            return True
        except ValueError:
            return False

    def validate_dob(self): #tries to convert the date into a string format into a defined format.
        try:
            datetime.strptime(self.dob, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_linkedin(self):
        if self.linkedin and not re.match(r"^(https://www\.linkedin\.com/.*)$", self.linkedin):
            return False
        return True

    def hash_password(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def save_to_csv(self):
        fieldnames = [
            "First Name", "Last Name", "Rating", "Age", "DOB", "Nationality", 
            "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability",
            "Topics of Interest", "Email", "Description", "Additional Information", 
            "Sort Value", "Type", "Password", "LinkedIn", "Mentor", "Image"
        ]

        # Read the existing data from the CSV file
        users = []
        email_exists = 0
        try:
            with open("generated_database.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Email"].lower() == self.email.lower():
                        # Update the user row with new data if email exists
                        email_exists = 1
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
                        row["Password"] =self.password  
                        row["LinkedIn"] = self.linkedin
                        row["Mentor"] = self.mentor
                        row["Image"] = self.image
                            
                    users.append(row)
        except FileNotFoundError:
            # If the file does not exist, we need to create it
            pass
        # If email doesn't exist, add new data
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
            
    def full_names():
        # Leer el archivo CSV
        df = pd.read_csv('generated_database.csv')
        
        # Crear la lista de nombres completos
        lstFullNames = [f"{df['First Name'].iloc[i]} {df['Last Name'].iloc[i]}" for i in range(len(df["First Name"]))]

        # Función de ordenación (algoritmo de Quicksort)
        def sortingmechanism(lst):
            if len(lst) <= 1:
                return lst
            else:
                randompivotval = random.randint(0, len(lst) - 1)
                randompivot = lst[randompivotval]
                lst.pop(randompivotval)
                lower_bound = [i for i in lst if randompivot > i]
                upper_bound = [i for i in lst if randompivot <= i]
                return sortingmechanism(lower_bound) + [randompivot] + sortingmechanism(upper_bound)

        # Ordenar la lista de nombres completos
        return sortingmechanism(lstFullNames)            


    @staticmethod #not usign self
    def email_exists(email):
        user_data = User.load_all_user_data()
        for user in user_data:
            if user["Email"] == email:
                return True 
        return False  

    @staticmethod
    def load_all_user_data():
        user_data = []
        with open("generated_database.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)  # Usamos DictReader para leer las filas como diccionarios
            for row in reader:
                user_data.append(row)
        return user_data
    
    @staticmethod 
    def load_mentor_user_data():
        user_data = []
        with open("generated_database.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                if row.get('Type', '').strip().lower() == 'alumni' and (row.get('Mentor', '').strip().lower() == 'true'):
                    user_data.append(row)


        return user_data
    
    @staticmethod
    def get_user_data_from_csv(email):
        with open('generated_database.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Email'].lower() == email.lower():
                    return row  # Devuelve los datos del usuario
        return {}
    @staticmethod
    #to binary search
    def full_names(fullname):
       
        # Leer el archivo CSV
        df = pd.read_csv('generated_database.csv')         
        # Crear la lista de nombres completos
        lst = [f"{df['First Name'].iloc[i]} {df['Last Name'].iloc[i]}" for i in range(len(df["First Name"]))]    
        # Ordenar la lista
        sorted_lst = User.sortingmechanism(lst)  
       
        return User.binarysearch(sorted_lst,fullname)
    @staticmethod
   # Definir el mecanismo de ordenación
    def sortingmechanism(lst):
            if len(lst) <= 1:
                return lst
            else:
                randompivotval = random.randint(0, len(lst) - 1)
                randompivot = lst[randompivotval]
                lst.pop(randompivotval)
                lower_bound = [i for i in lst if randompivot > i]
                upper_bound = [i for i in lst if randompivot <= i]
                return User.sortingmechanism(lower_bound) + [randompivot] + User.sortingmechanism(upper_bound) 
    
    @staticmethod      
    def binarysearch(fullnameslist,fullname):  
            
            # Validate the input list
            if not isinstance(fullnameslist, list):
                return 'No list was provided'
            if not fullnameslist:
                return 'The provided list is empty'    
            # Binary search algorithm
            start = 0
            end = len(fullnameslist) - 1    
            while start <= end:
                mid = (start + end) // 2        
                # Check if fullname is at the midpoint
                if fullnameslist[mid] == fullname:
                    return fullnameslist[mid]  # Return the fullname if found
                # Adjust the search range
                elif fullnameslist[mid] > fullname:
                    end = mid - 1
                else:
                    start = mid + 1   
            return None    

   
