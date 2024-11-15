import pandas as pd
import random


first_names = ["Alex", "Taylor", "Jordan", "Casey", "Morgan", "Jamie", "Riley", "Quinn", "Cameron", "Drew", "John", "Michael", "Robert", "David", "James", "William", "Joseph", "Charles", "Thomas", "Daniel"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall"]
nationalities = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland", "United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Japan", "South Korea", "China", "India", "Brazil"]
countries_of_residence = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland", "United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Japan", "South Korea", "China", "India", "Brazil"]
degrees = [
    "Business Management", "Data Science", "International Relations", 
    "Business Management and Data Science", "Computer Science", 
    "Biochemical Engineering", "Law", "Medicine", "Economics", "Applied Maths"
]
email_suffixes = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@icloud.com", "@protonmail.com", "@aol.com", "@zoho.com", "@yandex.com", "@mail.com"]
#randomly selects first name and email suffix and pastes them together in one line
def generate_email(first_name):
    return first_name.lower() + random.choice(email_suffixes)

looking_fors = ["Internship", "Project", "Full-time Job", "Student Job", "Thesis", "Volunteering", "Part-time Job", "Freelancing", "Remote Work", "Startup"]
def generate_random_data(num_rows):
    data = []

    for _ in range(num_rows):
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(17, 35)
        nationality = random.choice(nationalities)
        looking_for = random.choice(looking_fors)
        email = generate_email(first_name)
        description = f"Hello my name is {first_name} {last_name}: Generic description "
        additional_information = f"My linkedin profile is: {first_name}{last_name}linkedin.com and my github profile is: {first_name}{last_name}github.com"
        
        country_of_residence = random.choice([c for c in countries_of_residence if c != nationality] + [nationality])
        
        degree = random.choice(degrees)
        graduation_year = random.randint(2024, 2028)
        
        
        gpa = round(random.gauss(8, 1), 2)
        gpa = max(0, min(10, gpa))  
        
        availability = random.randint(2, 20)

        
        data.append([first_name, last_name, age, nationality, country_of_residence, degree, graduation_year, gpa, availability, looking_for, email, description, additional_information])

    return data

def write_to_csv(data, filename):
    
    headers = ["First Name", "Last Name", "Age", "Nationality", "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability", "Looking For", "Email", "Description", "Additonal Information" ]

    
    df = pd.DataFrame(data, columns=headers)


    df.to_csv(filename, index=False)
    print(f"Data successfully written to '{filename}'.")

def main():
    
    generated_data = generate_random_data(10000)
    
    
    write_to_csv(generated_data, 'generated_database.csv')
    

main()


