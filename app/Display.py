from Embedding import TakeFields as TF
import pandas as pd
from que import DataFramePrioritySorter

def AddSortValue(data, looking_for_interest=None, looking_for_degree=None):

    if not looking_for_interest and not looking_for_degree:
        data['Sort Value'] = pd.to_numeric(data['Rating'], errors='coerce') / 5  # Only normalize Rating
        return data


    if looking_for_interest:
        interest_similarities = [TF(interest, looking_for_interest) for interest in data['Topics of Interest']]
        data['Interest Similarity'] = pd.Series(interest_similarities, index=data.index)
    else:
        data['Interest Similarity'] = 0 

    if looking_for_degree:
        degree_similarities = [TF(degree, looking_for_degree) for degree in data['Degree']]
        data['Degree Similarity'] = pd.Series(degree_similarities, index=data.index)
      
    else:
        data['Degree Similarity'] = 0  
        
    data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce') #rating to numefic, if not string 

    data['Sort Value'] = (
        0.5 * data['Interest Similarity']
        + 0.2 * data['Degree Similarity']
        + 0.3 * (data['Rating'] / 5)
    )
    
    return quicksort_data(data,'Sorted Value')


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

