from Embedding import TakeFields as TF
import pandas as pd
from que import DataFramePrioritySorter


def AddSortValue(dataDic, looking_for_interest=None, looking_for_degree=None):
    data = pd.DataFrame(dataDic) #from json to dataframe 
    if data.empty: 
        return data 
    
    if (not looking_for_interest or looking_for_interest =='') and (not looking_for_degree or looking_for_degree ==''): #check for the emty spece aswell
        data['Sort Value'] = pd.to_numeric(data['Rating'], errors='coerce') / 5 
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

    data['Sort Value'] = ( 0.5 * data['Interest Similarity']  + 0.2 * data['Degree Similarity']  + 0.3 * (data['Rating'] / 5) )
    
    sorter = DataFramePrioritySorter(data,'Sort Value')
    
    sorted_data = sorter.sort()
    return sorted_data

