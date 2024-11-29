import pandas as pd
import heapq 

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))   # multiply the priority value times -1 in order to invert the order so we can pop the max value later.
                                                        # heap by default intruduces first the max value in the heap.
    
    def pop(self):
        if len(self.heap) != 0:
            neg_priority, item = heapq.heappop(self.heap)
            return (-neg_priority, item)

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





