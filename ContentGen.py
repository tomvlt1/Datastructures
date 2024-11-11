
import pandas as pd
from openai import OpenAI


#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
#IE key "sk-svcacct-Wxz3qtCz18dC8ic91rZ-LfDkLRo78m2ZrRsEXB5f5ST0hH5h_hBdnlLOYj7J_xT3BlbkFJ1h7NM0xnrAEq7Pk2muYfo5IfphWuVKCUF5lYsqRdgXq39B6xYA9Q65nb8baDIA"
# export OPENAI_API_KEY="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"
# function to generate a custom message using OpenAI GPT model
def GenerateDatabase(variable_description, size):
    client = OpenAI()
    prompt = (f"Based on on the {variable_description}, create {size} lines of data in a database in a csv file.")
    
    try:
        completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a machine learning model seeking to generate a database. Do not include any information but the data istself,absolutely no additional text. Do not write ```csv or ```"},
        {
            "role": "user",
            "content": prompt
        }
    ]
)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating custom message: {e}")
        return ""

def write_to_pandas(data):
    try:
        lines = data.splitlines() 
        header = lines[0].split(",")
        rows = [line.split(",") for line in lines[1:]] #in both cases the \t is the separator (tab / next line)

        
        df = pd.DataFrame(rows, columns=header)

        
        df.to_csv('generated_database.csv', index=False)
        print("Data successfully written to 'generated_database.csv'.")
    except Exception as e:
        print(f"Error writing to pandas: {e}")


if __name__ == "__main__":
    
    
    variable_description = """first name	last name	age	nationality	country of residence	degree	Graduation year	GPA	Availability
Generic first name	Generate last name	Range from 17- 35	Any nationality with a europe focus	Any with a focus of europe but not necessarily the same as nationaliy	Choose from: Business Management , Data Science, International Relations, Data Science, Business Management and Data Science, Computer Science, Biochemical Engineering, Law, Medicine, Economics, Applied Maths	from 2024 - 2028	from 0-10 with an average around 8	Hours per week available 2-20"""
    generated_data = GenerateDatabase(variable_description, 10)
    
    
    print(generated_data)
    
   
    write_to_pandas(generated_data)



    
    