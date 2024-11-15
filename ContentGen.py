import pandas as pd
import random


first_names = ["Alex", "Taylor", "Jordan", "Casey", "Morgan", "Jamie", "Riley", "Quinn", "Cameron", "Drew", "John", "Michael", "Robert", "David", "James", "William", "Joseph", "Charles", "Thomas", "Daniel"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall"]
nationalities = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland", "United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Japan", "South Korea", "China", "India", "Brazil"]
countries_of_residence = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland", "United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Japan", "South Korea", "China", "India", "Brazil"]
degrees = [
    # IE Business School
    "Bachelor in Business Administration",
    "Bachelor in Economics",
    "Bachelor in Data and Business Analytics",
    "International MBA",
    "Global Online MBA",
    "Master in Management",
    "Master in Management & Strategy",
    "Master in Finance",
    "Master in Business Analytics and Big Data",
    "Master in Sustainability Business Transformation",
    "Executive MBA",
    "Global Executive MBA",
    "IE Brown Executive MBA",
    "Executive MBA Presencial",
    "Executive Master in Digital Transformation & Innovation Leadership",
    "Master in Digital Business & Innovation",
    "Master in Applied Economics",

    # IE Law School
    "Bachelor of Laws (LL.B)",
    "Master of Laws (LL.M)",
    "Master in Global Corporate Compliance",
    "Executive Master in International Business Law",
    "Executive LL.M.",
    "Master in International Legal Studies (LL.M.)",

    # IE School of Politics, Economics and Global Affairs
    "Bachelor in International Relations",
    "Bachelor in Political Science",
    "Bachelor in Philosophy, Politics, Law & Economics (PPLE)",
    "Master in International Development",
    "Master in International Relations",
    "Executive Master in International Development",

    # IE School of Architecture and Design
    "Bachelor in Architectural Studies",
    "Bachelor in Design",
    "Bachelor in Design: Comprehensive Design Track",
    "Bachelor in Design: Videogame Design And Virtual Environments Track",
    "Bachelor in Design: Interior Design Track",
    "Bachelor in Fashion Design",
    "Master in Business for Architecture and Design",
    "Master in Strategic Design of Spaces",
    "Master in Real Estate Development",
    "Master in Architecture",
    "Master in Creative Direction, Content & Branding",
    "Programa Avanzado BuiltTech",
    "Sustainable Project Leadership",
    "(MDES) Master in Interior Design",
    "(MDES) Master in Videogame Design and Virtual Environments",

    # IE School of Science and Technology
    "Bachelor in Computer Science and Artificial Intelligence",
    "Bachelor in Applied Mathematics",
    "Bachelor in Environmental Sciences for Sustainability",
    "Master in Computer Science and Business Technology",
    "Master in Cybersecurity",
    "Master in Technology + Global Affairs",

    # IE School of Human Sciences and Technology
    "Bachelor in Communication and Digital Media",
    "Bachelor in Behavioral and Social Sciences",
    "Master in Visual and Digital Media",
    "Bachelor in Humanities",
    "Master in Customer Experience & Innovation",
    "Master in Talent Development & Human Resources"
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
        rating = random.randint(1, 5)
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
        sort_value = 0.0

        
        data.append([first_name, last_name,rating, age, nationality, country_of_residence, degree, graduation_year, gpa, availability, looking_for, email, description, additional_information, sort_value])

    return data

def write_to_csv(data, filename):
    
    headers = ["First Name", "Last Name","rating" ,"Age", "Nationality", "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability", "Looking For", "Email", "Description", "Additional Information", "Sort Value"]

    
    df = pd.DataFrame(data, columns=headers)


    df.to_csv(filename, index=False)
    print(f"Data successfully written to '{filename}'.")

def main():
    
    generated_data = generate_random_data(10000)
    
    
    write_to_csv(generated_data, 'generated_database.csv')
    

main()


