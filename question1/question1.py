# ExamForNTU question1

# Define a function to get the operation
def getOperations(m, n, sum, f):

    rightPosition = [0] * m     # Record the position of right operations.
    downSum = 0                 # Record the sum of numbers passed in down operations.
    rightTimes = n - 1          # Record the time of right operations.
    maxSub = m                  # Record the largest number in every step of right operations.

    # Get the total sum of right operations(the sum of down operations is fixed).
    for i in range(m+1):
        downSum += i
    sum -= downSum

    # Do the right operation at the maximum number as far as possible. If failed, minimize maxSub.
    while sum > 0 :
        if sum-maxSub >= rightTimes - 1:
            sum -= maxSub
            rightTimes -= 1
            rightPosition[maxSub-1] += 1
        else:
            maxSub -= 1

    # Judge whether the data of sum is out of bounds.
    if rightTimes != 0:
        print ("Cannot find the operations", end='', file=f)
    else:
        # Print the operations.
        for i in range(m):
            while rightPosition[i] > 0:
                print("R", end='', file=f)
                rightPosition[i] -= 1
            # Judge weather need a down operation
            if i != m-1:
                print("D", end='', file=f)


# Main

f=open("output_question_1.txt", "w")
rows, columns, sum = 9, 9, [65, 72, 90, 110]
for i in sum:
    print(i, end=' ', file=f)
    getOperations(rows, columns, i, f)
    print('', file=f)

print("", file=f)
rows, columns, sum = 90000, 100000, [87127231192, 5994891682]
for i in sum:
    print(i, end=' ', file=f)
    getOperations(rows, columns, i, f)
    print('', file=f)

f.close()