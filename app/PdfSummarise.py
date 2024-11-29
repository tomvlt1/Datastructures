# Using pdfminer.six for better results
from pdfminer.high_level import extract_text

text = extract_text('/Users/tom/Downloads/cv v1 finance target (1).pdf')
#print(text)

import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not done yet
nltk.download('stopwords')

# Preprocessing
text = text.lower()
text = re.sub(r'\W+', ' ', text) 
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_text = [word for word in text.split() if word not in stop_words]


