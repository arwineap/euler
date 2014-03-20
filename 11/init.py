#!/usr/bin/env python


def genDowns(grid, returnsize):
    try:
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                returnL = []
                returnL.append(entry)
                for x in range(1, int(returnsize)):
                    returnL.append(grid[i+x][j])
                yield returnL
    except IndexError:
        pass


def genRight(grid, returnsize):
    try:
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                # first one is entry
                # next one: grid[i+1][j]
                # next one: grid[i+2][j]
                # next one: grid[i+3][j]
                resultL = []
                resultL.append(entry)
                for x in range(1, int(returnsize)):
                    resultL.append(grid[i][j+x])
                yield resultL
    except IndexError:
        pass


def genDright(grid, returnsize):
    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            # first one is entry
            # next one: grid[i+1][j+1]
            resultL = []
            resultL.append(entry)
            for x in range(1, int(returnsize)):
                try:
                    resultL.append(grid[i+x][j+x])
                except IndexError:
                    pass
            if len(resultL) == returnsize:
                yield resultL

print "Project Euler problem 11: Of these four products, which is the largest?"

fh = open('input', 'r')
input = fh.readlines()
fh.close()

grid = []

for line in input:
    grid.append(map(int, line.split()))

biggestDown = 0
for factors in genDowns(grid, 4):
    product = factors[0] * factors[1] * factors[2] * factors[3]
    if product > biggestDown:
        biggestDown = product

print "biggestDown: %d" % biggestDown

biggestRight = 0
for factors in genRight(grid, 4):
    product = factors[0] * factors[1] * factors[2] * factors[3]
    if product > biggestRight:
        biggestRight = product

print "biggestRight: %d" % biggestRight

biggestDright = 0
for factors in genDright(grid, 4):
    product = factors[0] * factors[1] * factors[2] * factors[3]
    if product > biggestDright:
        biggestDright = product

print "biggestDright: %d" % biggestDright

mirrorgrid = []
for row in grid:
    mirrorgrid.append(row[::-1])

biggestDleft = 0
for factors in genDright(mirrorgrid, 4):
    product = factors[0] * factors[1] * factors[2] * factors[3]
    if product > biggestDleft:
        biggestDleft = product

print "biggestDleft: %d" % biggestDleft
