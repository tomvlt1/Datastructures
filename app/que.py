import heapq
from itertools import count
import pandas as pd

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = count()  # Unique sequence count
    
    def push(self, priority, item):
        # Multiply priority by -1 to simulate a max-heap
        heapq.heappush(self.heap, (-priority, next(self.counter), item))
    
    def pop(self):
        if not self.is_empty():
            neg_priority, _, item = heapq.heappop(self.heap)
            return (-neg_priority, item)
        else:
            raise IndexError("pop from an empty priority queue")
    
    def is_empty(self):
        return len(self.heap) == 0


class DataFramePrioritySorter:
    def __init__(self, dataframe, sort_column):
        if sort_column not in dataframe.columns:
            raise ValueError(f"Column '{sort_column}' does not exist in the DataFrame.")
        
        self.df = dataframe
        self.sort_column = sort_column
        self.priority_queue = PriorityQueue()
    
    def sort(self):
        # Convert DataFrame to list of dictionaries for faster iteration
        records = self.df.to_dict('records')
        for record in records:
            sort_value = record[self.sort_column]
            self.priority_queue.push(sort_value, record)
        
        sorted_records = []
        while not self.priority_queue.is_empty():
            priority, record = self.priority_queue.pop()
            sorted_records.append(record)
        
        sorted_df = pd.DataFrame(sorted_records).reset_index(drop=True)
        return sorted_df
