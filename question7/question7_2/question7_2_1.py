# ExamForNTU question7_2_1

import pandas as pd
import numpy as np

# Use pandas to read TXT file
# 'sep' means separator
df = pd.read_csv("/Users/darnell/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_coordinates_7_2.txt", sep = '\t')

# Convert data from 'dataframe' to 'array'
df = df.values

# Define the sizes of grid
l1, l2, l3, l4, l5, l6 = 4, 8, 5, 9, 6, 7
f=open("output_index_7_2.txt", "w")
index=0
print("index", file=f)
for i in range(len(df)):
    # Calculate the index
    index=l1*l2*l3*l4*l5*int(df[i][5])+l1*l2*l3*l4*int(df[i][4])+l1*l2*l3*int(df[i][3])+l1*l2*int(df[i][2])+l1*df[i][1]+int(df[i][0])
    print(index, file=f)