import pandas as pd

def quicksort_data(data, column):
    if len(data) <= 1:
        return data
    
    pivot = data[column].iloc[len(data) // 2]

    left = data[data[column] > pivot] 
    middle = data[data[column] == pivot]
    right = data[data[column] < pivot]

    return pd.concat([quicksort_data(left, column), middle, quicksort_data(right, column)])




