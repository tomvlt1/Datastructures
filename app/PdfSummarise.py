import openai
from pdfminer.high_level import extract_text



def summarise_pdf(file):
    text = extract_text(file)
    key = "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" #plz dont steal my key toni :( - thomas
    #client = openai.OpenAI(api_key="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")
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
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        summary = response.choices[0].message.content.strip()

        summary = summary.encode('ascii', 'ignore').decode('ascii')
        print("Raw API Output:", summary)

        summary = (summary)
        
        return summary
    except Exception as e:
        return str(e)


