import hashlib
import re  # to validate email and password
from datetime import datetime  # to validate dob
import csv


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
    ):
        # Initialize the User object with all attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.description = description
        self.additional_info = additional_info
        self.rating = rating
        self.age = age
        self.dob = dob
        self.nationality = nationality
        self.country_residence = country_residence
        self.degree = degree
        self.graduation_year = graduation_year
        self.gpa = gpa
        self.availability = availability
        self.topics_of_interest = topics_of_interest
        self.user_type = user_type
        self.linkedin = linkedin

    def validate_email(self):
        """Validate the email format using regex."""
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email))

    def validate_password(self):
        """Validate the password format (at least 8 characters, one uppercase, one number, and one special character)."""
        return bool(
            re.fullmatch(
                r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$",
                self.password,
            )
        )

    def validate_age(self):
        """Validate the age to be between 18 and 120."""
        try:
            age = int(self.age)
            if age < 18 or age > 120:
                return False
            return True
        except ValueError:
            return False

    def validate_dob(self):
        """Validate the date of birth format (YYYY-MM-DD)."""
        try:
            datetime.strptime(self.dob, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_linkedin(self):
        """Validate the LinkedIn URL format (optional)."""
        if self.linkedin and not re.match(r"^(https://www\.linkedin\.com/.*)$", self.linkedin):
            return False
        return True

    def hash_password(self):
        """Hash the password using SHA-256 for secure storage."""
        return hashlib.sha256(self.password.encode()).hexdigest()

    def save_to_csv(self):
        """Save the user's data to a CSV file."""
        fieldnames = [
            "First Name",
            "Last Name",
            "Rating",
            "Age",
            "DOB",
            "Nationality",
            "Country of Residence",
            "Degree",
            "Graduation Year",
            "GPA",
            "Availability",
            "Topics of Interest",
            "Email",
            "Description",
            "Additional Information",
            "Sort Value",
            "Type",
            "Password",
            "LinkedIn",
        ]

        # Open the CSV file in append mode
        with open("generated_database.csv", mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header only if the file is empty
            if file.tell() == 0:
                writer.writeheader()

            # Write the user's data to the file
            writer.writerow(
                {
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
                }
            )

    @staticmethod
    def load_user_data():
        user_data = []
        with open("generated_database.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)  # Usamos DictReader para leer las filas como diccionarios
            for row in reader:
                email = row["Email"]
                stored_password = row["Password"]

                # Añadimos un diccionario con las claves 'email' y 'password' a la lista
                user_data.append({"email": email, "password": stored_password})

        return user_data

    @staticmethod
    def email_exists(email):
        user_data = User.load_user_data()
        for user in user_data:
            if user["email"] == email:
                return True  # Email exists
        return False  # Email does not exist
