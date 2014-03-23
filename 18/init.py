#!/usr/bin/env python


def nextPathPoint(triangle, startpoint):
    # triangle should be the 2d list of value
    # startpoint should be the [x][y] coords of triangle to get where we're at
    # TODO: resolution should be how far down the rabbit hole we should go
    topoptions = getNextPoints(triangle, startpoint)
    biggestoptionpotential = (0, 0)
    for i, option in enumerate(topoptions):
        optionpotential = getValue(triangle, option)
        nextpointvalues = []
        for nextpoint in getNextPoints(triangle, option):
            nextpointvalues.append(getValue(triangle, nextpoint))
        optionpotential = optionpotential + max(nextpointvalues)
        if optionpotential > biggestoptionpotential[1]:
            biggestoptionpotential = (i, optionpotential)
    return topoptions[biggestoptionpotential[0]]


def getValue(triangle, coords):
    return int(triangle[coords[0]][coords[1]])


def getNextPoints(triangle, startpoint):
    # returns a list of next coordinates:
    # return [(x,y), (x1, y1)]
    nextrow = int(startpoint[0])+1
    nextvalue = int(startpoint[1])+1
    choices = []
    choices.append((nextrow, startpoint[1]))
    choices.append((nextrow, nextvalue))
    return choices

# load triangle file
fh = open('input', 'r')
rawinput = fh.readlines()
fh.close()

# break triangle var up into a 2d array so I can use it
parsedinput = []
for line in rawinput:
    parsedinput.append(line.split())

# print triangle because visual learning
for line in parsedinput:
    print line

pathlist = [(0, 0)]
pathpoint = pathlist[0]
print "start value, point: %d (%d, %d)" % (getValue(parsedinput, pathpoint), pathpoint[0], pathpoint[1])
for i in range(0, len(parsedinput)-2):
    nextpathpoint = nextPathPoint(parsedinput, pathpoint)
    print "next value, point: %d (%d, %d)" % (getValue(parsedinput, nextpathpoint), nextpathpoint[0], nextpathpoint[1])
    pathlist.append(nextpathpoint)
    pathpoint = nextpathpoint
# Manually get the last point
choices = getNextPoints(parsedinput, pathlist[-1:][0])
maxvalue = 0
maxpoint = (0, 0)
for choice in choices:
    if getValue(parsedinput, choice) > maxvalue:
        maxvalue = getValue(parsedinput, choice)
        maxpoint = choice
print "next value, point: %d (%d, %d)" % (maxvalue, maxpoint[0], maxpoint[1])
pathlist.append(maxpoint)

totalsum = 0
for point in pathlist:
    totalsum = totalsum + getValue(parsedinput, point)
print "totalsum: %d" % totalsum
