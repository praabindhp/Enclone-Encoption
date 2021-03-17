# Libraries To Be Imported
import fileinput
import sys
import os
from typing import Counter
import csv
import pandas as pd
import names

# Inputs :: Source & Destination
inputFileName = "Titanic.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_modified.csv"

# Reading CSV File
df = pd.read_csv(inputFileName)

# Creating List of Column Names
list_of_column_names = list(df.columns)
  
# Displaying List of Column Names 
# print('List of Column Names : ', list_of_column_names)

random_names = []
for header in list_of_column_names: # Encopted List With Random Names
    random_names.append(names.get_first_name())
# print(random_names)

# Converting List To String
changed_header_initial = ''
for name in random_names:
    changed_header_initial = str(changed_header_initial+','+name)

# String - Changed Headers
changed_header_initial = changed_header_initial[1:]
# print(changed_header_initial)

# Appending The Headers To The Modified CSV File
with open(outputFileName, "w") as outfile:
    for line in fileinput.input(
        [inputFileName],
        inplace=False):
        if fileinput.isfirstline():
            outfile.write(changed_header_initial+'\n')
        else:
            outfile.write(line)

# For Identification Purposes
# Storing The Header & Randomly Generated Names As A Dictionary 
res = {} 
for key in list_of_column_names: 
    for value in random_names: 
        res[key] = value 
        random_names.remove(value) 
        break
print ("dict : " +  str(res))