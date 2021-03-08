# ExamForNTU question4

import pandas as pd
import numpy as np

# Define a function to find 4-connectivity connected components of a pixel and recurse its components to find more components
def fourConnect(pixelList, row, column, counter):
    # Set the pixel to a new class
    pixelList[row][column] = counter

    # Judge whether there is connected pixel on the left and recurse it to find more components
    if pixelList[row][column - 1] == 1:
        pixelList[row][column - 1] = counter
        fourConnect(pixelList, row, column - 1, counter)

    # Judge whether there is connected pixel on the top and recurse it to find more components
    if pixelList[row - 1][column] == 1:
        pixelList[row - 1][column] = counter
        fourConnect(pixelList, row - 1, column, counter)

    # Judge whether there is connected pixel below and recurse it to find more components
    if pixelList[row+1][column] == 1:
        pixelList[row+1][column] = counter
        fourConnect(pixelList, row + 1, column, counter)

    # Judge whether there is connected pixel on the right and recurse it to find more components
    if pixelList[row][column + 1] == 1:
        pixelList[row][column + 1] = counter
        fourConnect(pixelList, row, column + 1, counter)


# Define a function to find 8-connectivity connected components of a pixel and recurse its components to find more components
def eightConnect(pixelList, row, column, counter):
    # Set the pixel to a new class
    pixelList[row][column] = counter

    # Judge whether there is connected pixel on the left and recurse it to find more components
    if pixelList[row][column - 1] == 1:
        pixelList[row][column - 1] = counter
        eightConnect(pixelList, row, column - 1, counter)

    # Judge whether there is connected pixel on the top and recurse it to find more components
    if pixelList[row - 1][column] == 1:
        pixelList[row - 1][column] = counter
        eightConnect(pixelList, row - 1, column, counter)

    # Judge whether there is connected pixel below and recurse it to find more components
    if pixelList[row + 1][column] == 1:
        pixelList[row + 1][column] = counter
        eightConnect(pixelList, row + 1, column, counter)

    # Judge whether there is connected pixel on the right and recurse it to find more components
    if pixelList[row][column + 1] == 1:
        pixelList[row][column + 1] = counter
        eightConnect(pixelList, row, column + 1, counter)

    # Judge whether there is connected pixel on the top left and recurse it to find more components
    if pixelList[row - 1][column - 1] == 1:
        pixelList[row - 1][column - 1] = counter
        eightConnect(pixelList, row - 1, column - 1, counter)
    # Judge whether there is connected pixel on the lower left and recurse it to find more components
    if pixelList[row - 1][column + 1] == 1:
        pixelList[row - 1][column + 1] = counter
        eightConnect(pixelList, row-1, column + 1, counter)

    # Judge whether there is connected pixel on the top right and recurse it to find more components
    if pixelList[row + 1][column - 1] == 1:
        pixelList[row + 1][column - 1] = counter
        eightConnect(pixelList, row + 1, column - 1, counter)

    # Judge whether there is connected pixel on the lower right and recurse it to find more components
    if pixelList[row + 1][column + 1] == 1:
        pixelList[row + 1][column + 1] = counter
        eightConnect(pixelList, row + 1, column + 1, counter)



# Main

# Use pandas to read TXT file
# 'sep' means separator
df = pd.read_csv("/Users/darnell/Desktop/AY20_MBDS_questions/Question 4/input_question_4", sep = '\t', header = None)

# Convert data from 'dataframe' to 'array'
df = df.values

# Create a new two-dimensional array in which every value is zero
# 'dtype' means datatype
pixelList = np.zeros((len(df)+2, len(df[0])+2), dtype=int)

# Copy data to new array
# The new array is surrounded by zeros to prevent boundary problems
for i in range(len(df)):
    for j in range(len(df[0])):
        pixelList[i + 1][j + 1] = df[i][j]

# Define the counter
# It starts with 2 to distinguish from the number of pixel(1)
# At the end of the program, all group numbers should be subtracted by 1
counter = 2

# Judge connected components
for i in range(1, len(pixelList)-1):
    for j in range(1, len(pixelList[i])-1):
        # Meet 1 means a new group
        if pixelList[i][j] == 1:
            # Find 4-connectivity connected components
            #fourConnect(pixelList, i, j, counter)

            # Find 8-connectivity connected components
            eightConnect(pixelList, i, j, counter)

            # Update group number
            counter += 1


# Copy data to original array to remove the zeros surrounded by the array
for i in range(1, len(pixelList)-1):
    for j in range(1, len(pixelList[i])-1):
        # All group numbers are subtracted by 1
        if pixelList[i][j] != 0:
            pixelList[i][j] -= 1
        df[i-1][j-1] = pixelList[i][j]

# Print final result
f=open("output_question_4_eightConnect.txt", "w")
print(df, file=f)
f.close()