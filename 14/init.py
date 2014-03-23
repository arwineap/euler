#!/usr/bin/env python


def iseven(foo):
    if foo % 2 == 0:
        return True
    return False

def collatz(x):
    while x != 1:
        if iseven(x):
            x = x/2
            yield x
        else:
            x = (3 * x) + 1
            yield x

biggestcount = 0
biggestattempter = ""

for attempt in range(2, 999999):
    counter = 1
    for chain in collatz(attempt):
        counter += 1
    if counter > biggestcount:
        print "NEW RECORD! starter: %d counter %d" % (attempt, counter)
        biggestcount = counter
        biggestattempter = attempt

print "result: %d was the largest chain creator with: %d" % (biggestattempter, biggestcount)
