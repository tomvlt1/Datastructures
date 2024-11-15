from Filter import main as Filter_main
from Embedding import TakeFields as TF
import pandas as pd

def AddSortValue(data, looking_for_interest, looking_for_degree):
   
    
    interest_similarities = [TF(interest, looking_for_interest) for interest in data['Topics of Interest']]
    degree_similarities = [TF(degree, looking_for_degree) for degree in data['Degree']]
    
    
    data['Interest Similarity'] = pd.Series(interest_similarities, index=data.index)
    data['Degree Similarity'] = pd.Series(degree_similarities, index=data.index)

    
    data['Sort Value'] = 0.5 * data['Interest Similarity'] + 0.2 * data['Degree Similarity'] + 0.3 * (data['Rating']/5)

    return data

def main():
    data = Filter_main()
    
    data = AddSortValue(data, "Computer Science", "Data Science")
    
    
    
    return data

print(main().head(10))

