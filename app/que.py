# priority_sorter.py
import pandas as pd
import heapq 

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self):
        if not self.is_empty():
            neg_priority, item = heapq.heappop(self.heap)
            return (-neg_priority, item)
        else:
            raise IndexError("pop from an empty priority queue")
    
    def is_empty(self):
        return len(self.heap) == 0

class DataFramePrioritySorter:
 
    def __init__(self, dataframe, sort_column):
        self.df = dataframe
        self.sort_column = sort_column
        self.priority_queue = PriorityQueue()
    
    def sort(self):
        for index, row in self.df.iterrows():
            sort_value = row[self.sort_column]
            self.priority_queue.push(sort_value, row)
        
        sorted_rows = []
        while not self.priority_queue.is_empty():
            priority, row = self.priority_queue.pop() 
            sorted_rows.append(row)
        
        sorted_df = pd.DataFrame(sorted_rows).reset_index(drop=True)
        return sorted_df
