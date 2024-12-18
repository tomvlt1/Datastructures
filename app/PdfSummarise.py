import openai
from pdfminer.high_level import extract_text #this library will be used to extract the text from the PDF



def summarise_pdf(file):
    text = extract_text(file) #extract the content from the CV literally as it was given
    #plz dont steal my key toni :( - thomas - nevermind OpenAI shut it down after the github was made public
    key = "" 
    client = openai.OpenAI(api_key=key)
    example = """As a student at IE University, I am pursuing a double degree in Business Management and Data Science, combining technical know-how with business insights. I am passionate about applying data-driven solutions to real-world problems and exploring the intersection of finance, technology, and sustainability. 

I have gained hands-on experience in various domains, such as M&A, digital strategy, and web development, through my internships at Tikehau Capital and UENI Ltd. I have also completed a JPMorgan Chase course on investment banking, enhancing my skills in DCF valuations and company analysis. I am proficient in Python and versed in SQL, R, and web tech (HTML & CSS). In addition, I am committed to community service, having tutored underprivileged students in math and computer science. I am bilingual in French and English, and have foundational Spanish skills."""
    prompt = f"""
    Read the following text: {text}.
    I want you to create a short description of the person based on the text.
    This should be in the first person and should be a few sentences long, describing the person's interests, skills, and background.
    Image you are that person. Make yourself sound interesting and engaging as this is for a professional profile on a networking site.
    You can use this example as a reference: {example}. Make it very very short with ONLY the most important factors.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o", #using 4o, the most powerful model and pretty cheap
            messages=[ 
                {"role": "system", "content": prompt}
            ]
        )
        summary = response.choices[0].message.content.strip()

        summary = summary.encode('ascii', 'ignore').decode('ascii') #clean the output as we were getting errors when is was being outputted to the html
        print("Raw API Output:", summary)

        summary = (summary)
        
        return summary
    except Exception as e:
        return str(e)


