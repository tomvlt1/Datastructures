import pandas as pd
import random


first_names = ["Alex", "Taylor", "Jordan", "Casey", "Morgan", "Jamie", "Riley", "Quinn", "Cameron", "Drew"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
nationalities = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland"]
countries_of_residence = ["Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland"]
degrees = [
    "Business Management", "Data Science", "International Relations", 
    "Business Management and Data Science", "Computer Science", 
    "Biochemical Engineering", "Law", "Medicine", "Economics", "Applied Maths"
]

def generate_random_data(num_rows):
    data = []

    for _ in range(num_rows):
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(17, 35)
        nationality = random.choice(nationalities)
        
        
        country_of_residence = random.choice([c for c in countries_of_residence if c != nationality] + [nationality])
        
        degree = random.choice(degrees)
        graduation_year = random.randint(2024, 2028)
        
        
        gpa = round(random.gauss(8, 1), 2)
        gpa = max(0, min(10, gpa))  
        
        availability = random.randint(2, 20)

        
        data.append([first_name, last_name, age, nationality, country_of_residence, degree, graduation_year, gpa, availability])

    return data

def write_to_csv(data, filename):
    
    headers = ["First Name", "Last Name", "Age", "Nationality", "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability"]

    
    df = pd.DataFrame(data, columns=headers)


    df.to_csv(filename, index=False)
    print(f"Data successfully written to '{filename}'.")

def main():
    
    generated_data = generate_random_data(5000)
    
    
    write_to_csv(generated_data, 'generated_database.csv')
    

main()


