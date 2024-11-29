import openai
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def get_key_words(text):
    
    openai.api_key = "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"
    client = openai.OpenAI(api_key="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")

    examples = """Computer Science", "Entrepreneurship", "Art", "Music", "Sports", "Tech", "Machine Learning", "Data Science", "Business", "Finance", "Economics", "Politics", "Philosophy", "History", "Literature", "Languages", "Mathematics", "Physics", "Chemistry", "Biology", "Medicine", "Psychology", "Sociology", "Anthropology", "Geography", "Environmental Science", "Law", "Architecture", "Design", "Fashion", "Film", "Theatre", "Dance", "Photography", "Culinary Arts", "Travel", "Fitness", "Health", "Nutrition", "Yoga", "Meditation", "Mindfulness", "Sustainability", "Climate Change", "Renewable Energy", "Urban Planning", "Transportation", "Public Policy", "International Relations", "Global Affairs", "Development", "Human Rights", "Social Justice", "Equality", "Diversity", "Inclusion", "Feminism", "LGBTQ+", "Mental Health", "Wellness", "Self-Care", "Parenting", "Education", "Child Development", "Youth Empowerment", "Elderly Care", "Disability Rights", "Animal Rights", "Veganism", "Vegetarianism", "Healthy Living", "Fitness", "Sports", "Outdoor Activities", "Adventure", "Travel", "Exploration", "Camping", "Hiking", "Cycling", "Running", "Swimming", "Skiing", "Snowboarding", "Surfing", "Skateboarding", "Basketball", "Football", "Soccer", "Tennis", "Golf", "Cricket", "Rugby", "Baseball", "Softball", "Volleyball", "Handball", "Table Tennis", "Badminton", "Squash", "Gymnastics", "Dance", "Yoga", "Pilates", "Martial Arts", "Boxing", "Wrestling", "Weightlifting", "CrossFit", "Bodybuilding", "Powerlifting", "Parkour", "Rock Climbing", "Mountaineering", "Sailing", "Rowing", "Canoeing", "Kayaking", "Surfing", "Kitesurfing", "Windsurfing", "Scuba Diving", "Snorkeling", "Fishing", "Hunting", "Cycling", "Mountain Biking","AI", "Blockchain", "SaaS", "IoT", "Fintech", "Edtech", "Healthcare", "Sustainability", "Agritech", "E-commerce"""
    prompt = f"""
    Extract the keywords from the following text: {text}
    Keywords should be inspired by the following examples: {examples}.
    Format your output as a valid Python list of strings comma separated values AND NOTHING ELSE, examples [value1, value2, value3] ].
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt}]
        )
        
        key_words = response.choices[0].message.content.strip()
        print("Raw API Output:", key_words)

        cleaned_key_words = key_words.strip('"')
        keywords = eval(cleaned_key_words)
        
        return keywords
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    pdf_path = '/Users/tom/Downloads/cv v1 finance target (1).pdf'  
    text = extract_text_from_pdf(pdf_path)
    if text:
        keywords = get_key_words(text)
        print("Extracted Keywords:", keywords)
        print(keywords[1]) #to test if proper list
    else:
        print("No text extracted from PDF.")
        

