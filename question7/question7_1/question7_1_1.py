# ExamForNTU question7_1_1

import pandas as pd
import numpy as np

# Use pandas to read TXT file
# 'sep' means separator
df = pd.read_csv("/Users/darnell/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt", sep = '\t')

# Convert data from 'dataframe' to 'array'
df = df.values

# Define the sizes of  grid
l1 = 50
l2 = 57
index = 0

f=open("output_index_7_1.txt", "w")
print("index",file=f)
for i in range(len(df)):
    # Calculate the index
    index = l1*df[i][1]+df[i][0]
    print(index, file=f)
