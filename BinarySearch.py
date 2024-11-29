import pandas as pd
import random

df = pd.read_csv('app/generated_database.csv')

lstFullNames = []

for i in range(len(df["First Name"])):
    first_name = df['First Name'].iloc[i]
    last_name = df['Last Name'].iloc[i]
    full_name = first_name + ' ' + last_name
    lstFullNames.append(full_name)

def sortingmechanism(list):
  if len(list)==1 or len(list)==0:
   return list
  else:
    randompivotval = random.randint(0, len(list) - 1)
    randompivot = list[randompivotval]
    lower_bound=[]
    upper_bound=[]
    list.pop(randompivotval)
    for i in list:
      if randompivot<=i:
        upper_bound.append(i)
      elif randompivot>i:
        lower_bound.append(i)
  return sortingmechanism(lower_bound) + [randompivot] + sortingmechanism(upper_bound)

lstFullNamesSorted = sortingmechanism(lstFullNames)

def binarysearch(fullnameslist, fullname):
    if not isinstance(fullnameslist, list):
        return 'No list was provided'
    if not fullnameslist:
        return 'The provided list is empty'
    
    start = 0
    end = len(fullnameslist) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if fullnameslist[mid] == fullname:
            return mid
        elif fullnameslist[mid] > fullname:
            end = mid - 1
        else:
            start = mid + 1
    
    return None  

name_provided = "Quinn Johnson"
result = binarysearch(lstFullNamesSorted, name_provided)
print(lstFullNamesSorted[result])