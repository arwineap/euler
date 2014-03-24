#!/usr/bin/env python


def makechoice(triangle, coords):
    # I need to know how many levels of triangle to fold up off the bottom
    # on small-input, at y index 12 we need to fold the last two rows together
    # len(triangle) is 15.
    # at y index 8, I need 5 iterations
    # at y index 12 I need 1 iteration
    # this means my 'effective' height is len()-2
    triheight = len(triangle)-2
    iterations = triheight-coords[0]
    # fold the triangle array to make it easier for the dumb choice function
    for x in range(iterations):
        triangle = foldtriangle(triangle)
    return dumbchoice(triangle, coords)


def dumbchoice(triangle, coords):
    option1 = (coords[0]+1, coords[1])
    option2 = (coords[0]+1, coords[1]+1)
    if getValue(triangle, option1) > getValue(triangle, option2):
        return option1
    else:
        return option2


def foldtriangle(triangle):
    newrow = []
    lastrowidx = len(triangle)-1
    # triangle is zero indexed
    for i, entry in enumerate(triangle[-2:-1][0]):
        option1 = entry + triangle[lastrowidx][i]
        option2 = entry + triangle[lastrowidx][i+1]
        if option1 > option2:
            newrow.append(option1)
        else:
            newrow.append(option2)
    result = triangle[:-2]
    result.append(newrow)
    return result


def getValue(triangle, coords):
    return int(triangle[coords[0]][coords[1]])


# load triangle file
fh = open('input', 'r')
rawinput = fh.readlines()
fh.close()

# break triangle var up into a 2d array so I can use it
parsedinput = []
for line in rawinput:
    # use map to convert the list of strings to a list of ints
    newline = map(int, line.split())
    parsedinput.append(newline)

# print triangle because visual learning
# don't because it's huge on this problem
#for line in parsedinput:
#    print line

pathlist = [[0, 0]]
for x in range(len(parsedinput)-1):
    pathlist.append(makechoice(parsedinput, pathlist[-1:][0]))

totalsum = 0
for coord in pathlist:
    totalsum += getValue(parsedinput, coord)
print 'totalsum:', totalsum
