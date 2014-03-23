#!/usr/bin/env python


def nextPathPoint(triangle, startpoint):
    # triangle should be the 2d list of value
    # startpoint should be the [x][y] coords of triangle to get where we're at
    # TODO: resolution should be how far down the rabbit hole we should go
    #
    # options = Layer one of options under startpoint
    options = getNextPoints(triangle, startpoint)
    optiondict = {}
    for option in options:
        optiondict[option] = {}
        optiondict[option]['value'] = getValue(triangle, option)
        optiondict[option]['potential'] = optiondict[option]['value']
        optiondict[option]['options'] = getNextPoints(triangle, option)
        for optx in optiondict[option]['options']:
            maxvalue = 0
            for foo in getNextPoints(triangle, optx):
                if getValue(triangle, foo) > maxvalue:
                    maxvalue = getValue(triangle, foo)
        optiondict[option]['potential'] = optiondict[option]['potential'] + maxvalue
    maxvalue = 0
    for key in optiondict:
        if optiondict[key]['potential'] > maxvalue:
            maxvalue = optiondict[key]['potential']
            maxkey = key
    return maxkey


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
print "start value, point: %d (%d, %d)" % (getValue(parsedinput, pathpoint),
                                           pathpoint[0], pathpoint[1])
for i in range(0, len(parsedinput)-3):
    nextpathpoint = nextPathPoint(parsedinput, pathpoint)
    print "next value, point: %d (%d, %d)" % (
        getValue(parsedinput, nextpathpoint), nextpathpoint[0],
        nextpathpoint[1])
    pathlist.append(nextpathpoint)
    pathpoint = nextpathpoint
# Manually get the last two point
choices = getNextPoints(parsedinput, pathlist[-1:][0])
maxvalue = 0
maxpoint = (0, 0)
for choice in choices:
    if getValue(parsedinput, choice) > maxvalue:
        maxvalue = getValue(parsedinput, choice)
        maxpoint = choice
print "next value, point: %d (%d, %d)" % (maxvalue, maxpoint[0], maxpoint[1])
pathlist.append(maxpoint)

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
