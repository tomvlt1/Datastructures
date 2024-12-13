#This file is responsible for the generation of "fake" projects, so that it is possible to have a functioing application 
#In this file we provide a random set of attributes for each possible characteristic of the project and it randomly generates projects with such attributes, by randomly selecting the attributes
import pandas as pd
import random
from datetime import date

#Here is where we specify the possible value that each characteristic of the project could take. It takes as an input the number of projects to generate.
def generate_random_data(num_rows):
    project_names = ["Apollo", "Voyager", "Luna", "Phoenix", "Orion", "Horizon", "Genesis", "Zenith", "Pioneer", "Odyssey"]
    project_stages = ["Ideation", "Prototype", "Development", "Testing", "Launch"]
    first_names = ["Alex", "Taylor", "Jordan", "Casey", "Morgan", "Jamie", "Riley", "Quinn", "Cameron", "Drew", "John", "Michael", "Robert", "David", "James", "William", "Joseph", "Charles", "Thomas", "Daniel"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall"]
    admins = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(10)]
    keywords_list = ["AI", "Blockchain", "SaaS", "IoT", "Fintech", "Edtech", "Healthcare", "Sustainability", "Agritech", "E-commerce"]
    languages_list = ["English", "Spanish", "French", "German", "Mandarin", "Hindi", "Portuguese", "Russian", "Japanese", "Korean"]
    positions_list = ["Developer", "Designer", "Project Manager", "Data Scientist", "Marketing Specialist", "Business Analyst"]
    data = []
    
    for _ in range(num_rows):
        project_name = random.choice(project_names)
        admin = random.choice(admins)
        max_people = random.randint(2, 8)
        current_people = random.randint(1, max_people)
        num_people = f"{current_people}/{max_people}"
        keywords = random.sample(keywords_list, random.randint(2, 5))
        project_stage = random.choice(project_stages)
        language_spoken = random.choice(languages_list)
        start_date = date(random.randint(2015, 2023), random.randint(1, 12), random.randint(1, 28))
        completion_estimate = random.randint(1, 36)  # In months
        project_description = f"This project is focused on {', '.join(keywords)} and aims to achieve significant progress in the {project_stage} stage."
        positions_needed_count = max_people - current_people
        positions_needed = random.sample(positions_list, min(positions_needed_count, len(positions_list)))
        
        data.append([project_name, admin, num_people, keywords, project_stage, language_spoken, start_date, completion_estimate, project_description, positions_needed])

    return data
#This saves the file as a CSV, it takes in the dataset previously generated ant the file name desired by the user and saves such. 
def write_to_csv(data, filename):
    headers = ["Project Name", "Admin", "Number of People", "Keywords", "Project Stage", "Language Spoken", "Start Date", "Completion Estimate (Months)", "Project Description", "Positions Needed"]
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(filename, index=False)
    print(f"Data successfully written to '{filename}'.")

def main():
    generated_data = generate_random_data(500)
    write_to_csv(generated_data, 'app/generated_project_database.csv')

main()
