# ExamForNTU question7_2_2

import pandas as pd
import numpy as np

# Use pandas to read TXT file
# 'sep' means separator
df = pd.read_csv("/Users/darnell/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_index_7_2.txt", sep = '\t')

# Convert data from 'dataframe' to 'array'
df = df.values
# Define the sizes of grid
l1, l2, l3, l4, l5, l6 = 4, 8, 5, 9, 6, 7

f=open("output_coordinates_7_2.txt", "w")
print("x1 x2 x3 x4 x5 x6", file=f)
for i in range(len(df)):
    # Calculate the coordinates
    index = int(df[i])
    x1 = index % l1
    x2 = (index - x1) % (l1 * l2) / l1
    x3 = (index - l1 * x2 - x1) % (l1 * l2 * l3) / (l1 * l2)
    x4 = (index - (l1 * l2) * x3 - l1 * x2 - x1) % (l1 * l2 * l3 *l4) / (l1 * l2 * l3)
    x5 = (index - (l1 * l2 * l3) * x4 - (l1 * l2) * x3 - l1 * x2 - x1) % (l1 * l2 * l3 * l4 * l5) / (l1 * l2 * l3 * l4)
    x6 = (index- (l1 * l2 * l3 * l4) * x5 - (l1 * l2 * l3) * x4 - (l1 * l2) * x3 - l1 * x2 - x1) % (l1 * l2 * l3 * l4 * l5 * l6) / (l1 * l2 * l3 * l4 * l5)
    print(int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), file=f)

