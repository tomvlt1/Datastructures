import pandas as pd
import random
from datetime import date

def generate_random_data(num_rows):
   
    topics_of_interest = ["Computer Science", "Entrepreneurship", "Art", "Music", "Sports", "Tech", "Machine Learning", "Data Science", "Business", "Finance", "Economics", "Politics", "Philosophy", "History", "Literature", "Languages", "Mathematics", "Physics", "Chemistry", "Biology", "Medicine", "Psychology", "Sociology", "Anthropology", "Geography", "Environmental Science", "Law", "Architecture", "Design", "Fashion", "Film", "Theatre", "Dance", "Photography", "Culinary Arts", "Travel", "Fitness", "Health", "Nutrition", "Yoga", "Meditation", "Mindfulness", "Sustainability", "Climate Change", "Renewable Energy", "Urban Planning", "Transportation", "Public Policy", "International Relations", "Global Affairs", "Development", "Human Rights", "Social Justice", "Equality", "Diversity", "Inclusion", "Feminism", "LGBTQ+", "Mental Health", "Wellness", "Self-Care", "Parenting", "Education", "Child Development", "Youth Empowerment", "Elderly Care", "Disability Rights", "Animal Rights", "Veganism", "Vegetarianism", "Healthy Living", "Fitness", "Sports", "Outdoor Activities", "Adventure", "Travel", "Exploration", "Camping", "Hiking", "Cycling", "Running", "Swimming", "Skiing", "Snowboarding", "Surfing", "Skateboarding", "Basketball", "Football", "Soccer", "Tennis", "Golf", "Cricket", "Rugby", "Baseball", "Softball", "Volleyball", "Handball", "Table Tennis", "Badminton", "Squash", "Gymnastics", "Dance", "Yoga", "Pilates", "Martial Arts", "Boxing", "Wrestling", "Weightlifting", "CrossFit", "Bodybuilding", "Powerlifting", "Parkour", "Rock Climbing", "Mountaineering", "Sailing", "Rowing", "Canoeing", "Kayaking", "Surfing", "Kitesurfing", "Windsurfing", "Scuba Diving", "Snorkeling", "Fishing", "Hunting", "Cycling", "Mountain Biking"]
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
    "Master in Talent Development & Human Resources"]
    email_suffixes = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@icloud.com", "@protonmail.com", "@aol.com", "@zoho.com", "@yandex.com", "@mail.com"]

    data = []
    
    for _ in range(num_rows):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1990, 2007)
        DOB = date(year, month, day)
        age = date.today().year - DOB.year - ((date.today().month, date.today().day) < (DOB.month, DOB.day)) # calculate age based on date of birth, it check with logical statemnt if the birthday has already passed this year

        # random amount of topics of interest and random topics
        num_topics = random.randint(1, 10)
        topics = random.sample(topics_of_interest, num_topics)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        rating = random.randint(1, 5)
        nationality = random.choice(nationalities)
    
        email = generate_email(first_name, email_suffixes)
        description = f"Hello my name is {first_name} {last_name}: Generic description "
        additional_information = f"My linkedin profile is: {first_name}{last_name}linkedin.com and my github profile is: {first_name}{last_name}github.com"
        
        country_of_residence = random.choice([c for c in countries_of_residence if c != nationality] + [nationality])
        
        degree = random.choice(degrees)
        graduation_year = random.randint(2024, 2028)
        
        gpa = round(random.gauss(8, 1), 2)
        gpa = max(0, min(10, gpa))  
        
        availability = random.randint(2, 20)
        sort_value = 0.0

        
        data.append([first_name, last_name, rating, age, DOB, nationality, country_of_residence, degree, graduation_year, gpa, availability, topics, email, description, additional_information, sort_value])

    return data

def generate_email(first_name, email_suffixes):
    #randomly selects first name and email suffix and pastes them together in one line

    return first_name.lower() + random.choice(email_suffixes)

def write_to_csv(data, filename):
    
    headers = ["First Name", "Last Name","Rating" ,"Age","DOB", "Nationality", "Country of Residence", "Degree", "Graduation Year", "GPA", "Availability", "Topics of Interest", "Email", "Description", "Additional Information", "Sort Value"]

    
    df = pd.DataFrame(data, columns=headers)


    df.to_csv(filename, index=False)
    print(f"Data successfully written to '{filename}'.")

def main():
    
    generated_data = generate_random_data(5000)
    write_to_csv(generated_data, 'generated_database.csv')
    

#main()

