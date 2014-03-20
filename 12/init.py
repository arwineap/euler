#!/usr/bin/env python

import sys


def genTri():
    i = 1
    while True:
        top = i*(i+1)
        yield top/2
        i += 1


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for idx, tri in enumerate(genTri()):
    if len(factors(tri)) >= 500:
        print "%d is the %dth triangle number and has %d factors" % (tri, idx, len(factors(tri)))
        sys.exit()
