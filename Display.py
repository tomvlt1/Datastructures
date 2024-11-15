from Filter import main as Filter_main
from Embedding import TakeFields as TF
import pandas as pd

def AddSortValue(data, looking_for_interest, looking_for_degree):
    # Ensure there are no NaN values in key columns
    data['Topics of Interest'] = data['Topics of Interest'].fillna("")
    data['Degree'] = data['Degree'].fillna("")
    data['Rating'] = data['Rating'].fillna(0)

    # Calculate similarity scores for each row and add them to lists
    interest_similarities = [TF(interest, looking_for_interest) for interest in data['Topics of Interest']]
    degree_similarities = [TF(degree, looking_for_degree) for degree in data['Degree']]

    # Create new Series for the similarity scores
    data['Interest Similarity'] = pd.Series(interest_similarities, index=data.index)
    data['Degree Similarity'] = pd.Series(degree_similarities, index=data.index)

    # Calculate Sort Value (normalized rating between 0 and 1)
    data['Sort Value'] = 0.5 * data['Interest Similarity'] + 0.2 * data['Degree Similarity'] + 0.3 * (data['Rating'] / 5)

    return data

def main():
    # Filter the data using Filter_main
    data = Filter_main()

    # Add sorting value to the filtered data
    data = AddSortValue(data, ["Computer Science", "Artificial Intelligence", "Machine Learning"], 
                        ["Data Science", "Computer Science", "Information Technology"])

    # Display the first 10 rows of the DataFrame


    return data




print(main().head(10))

