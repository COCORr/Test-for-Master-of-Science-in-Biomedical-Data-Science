# ExamForNTU question6


# Define a function to judge whether a half-line to the right of a point intersects a line segment
# sPoint1 and sPoint2 are the vertexes of a line segment
def isIntersection(pointX, pointY, sPoint1X, sPoint1Y, sPoint2X, sPoint2Y):

    # The horizontal edge of the polygon is not considered
    if sPoint1Y == sPoint2Y:
        return False

    # Calculate the coordinates of the intersection of half-line and line which the segment located
    x = (sPoint2X - sPoint1X) * pointY - (sPoint2X - sPoint1X) * sPoint1Y + (sPoint2Y - sPoint1Y) * sPoint1X
    x = x / (sPoint2Y - sPoint1Y)

    if x < pointX:
        return False
    # Judge whether the intersection  is on the line segment
    if pointY > sPoint1Y and pointY < sPoint2Y:
        return True
    if pointY < sPoint1Y and pointY > sPoint2Y:
        return True

    # Solve vertex problems (When it intersects a vertex, it's hard to calculate how many sides it intersects)
    # For the intersection of polygon vertex and the half-line, it is necessary to judge whether the vertex is the vertex with the larger Y-axis
    # If the half-line intersects with the smaller vertex, ignore it.
    if sPoint1Y > sPoint2Y:
        if pointY == sPoint1Y:
            return True
    else:
        if pointY == sPoint2Y:

            return True

    return False


# Define a function to judge whether a point is in the polygon
# xList and yList are the list of coordinates of points which make up the polygon
def isInPolygon(pointX, pointY, xList, yList):
    pointNum = len(xList)       # Record the num of points which make up the polygon
    intersectionNum = 0         # Record the num of intersectionNum

    for i in range(pointNum - 1):
        # Judge whether the point is exactly on a vertical line segment
        if pointX == xList[i] and pointX == xList[i + 1]:
            if pointY >= yList[i] and pointY <= yList[i + 1]:
                return True
            if pointY <= yList[i] and pointY >= yList[i + 1]:
                return True

        # Judge whether the point is exactly on a non vertical line segment
        if xList[i] - pointX != 0 and xList[i + 1] - pointX != 0 and (yList[i] - pointY)/(xList[i] - pointX) == (yList[i + 1]-pointY)/(xList[i + 1]-pointX):
            if xList[i] >= pointX and xList[i + 1] <= pointX:
                return True
            if xList[i] <= pointX and xList[i + 1] >= pointX:
                return True

        # Judge whether a half-line to the right of a point intersects a line segment
        if isIntersection(pointX, pointY, xList[i], yList[i], xList[i + 1], yList[i + 1]):
            intersectionNum += 1

    # The two vertices of the last line segment are the first point and the last point
    if isIntersection(pointX, pointY, xList[0], yList[0], xList[pointNum - 1], yList[pointNum - 1]):
        intersectionNum += 1

    # If the number of intersections is odd, the point is in the polygon

    if intersectionNum % 2 == 0:
        return False
    else:
        return True


# Main
xList=[4, 2, 3, 2, 5, 9, 14, 20, 18, 11]
yList=[3, 6, 12, 17, 20, 21, 19, 14, 3, 7]

pListX=[7, 10, 11, 12, 16, 16, 17, 18, 18, 20]
pListY=[11, 14, 4, 21, 3, 10, 4, 7, 17, 7]

f=open("output_question_6.txt", "w")
for i in range(len(pListX)):
    print(pListX[i],pListY[i], end=' ', file=f)
    if isInPolygon(pListX[i], pListY[i], xList, yList):
        print("inside", file=f)
    else:
        print("outside", file=f)
