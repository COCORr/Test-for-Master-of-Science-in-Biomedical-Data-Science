# ExamForNTU question7_1_2

import pandas as pd
import numpy as np

# Use pandas to read TXT file
# 'sep' means separator
df = pd.read_csv("/Users/darnell/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt", sep = '\t')

# Convert data from 'dataframe' to 'array'
df = df.values

# Define the sizes of grid
l1 = 50
l2 = 57

f=open("output_coordinates_7_1.txt", "w")
print("x1 x2", file=f)
for i in range(len(df)):
    # Calculate the coordinates
    x1 = df[i] % l1

    x2 = (df[i] - x1) / l1
    print(x1[0],int(x2[0]),file=f)