from Filter import main as Filter_main
from Embedding import TakeFields as TF
import pandas as pd

def AddSortValue(data, looking_for_interest, looking_for_degree):


    interest_similarities = [TF(interest, looking_for_interest) for interest in data['Topics of Interest']]
    degree_similarities = [TF(degree, looking_for_degree) for degree in data['Degree']]

    data['Interest Similarity'] = pd.Series(interest_similarities, index=data.index)
    data['Degree Similarity'] = pd.Series(degree_similarities, index=data.index)

    #make sure that the rating variable is numeric 
    data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')
    
    data['Sort Value'] = 0.5 * data['Interest Similarity'] + 0.2 * data['Degree Similarity'] + 0.3 * (data['Rating'] / 5)
    
    return data

def main():
    data = Filter_main()
    if data is None or data.empty:
        raise ValueError("Filter_main() returned None or an empty DataFrame.")
    print(f"Filter_main() returned data with shape: {data.shape}")
    print(data.head())

    data = AddSortValue(data, ["Computer Science", "Artificial Intelligence", "Machine Learning"], 
                        ["Data Science", "Computer Science", "Information Technology"])
    return data

#print(main().head(50))

