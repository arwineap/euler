#!/usr/bin/env python


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def sumfactors(n):
    factorsL = factors(n)
    sumlist = []
    for factor in factorsL:
        if factor != n:
            sumlist.append(factor)
    resultlist = map(int, sumlist)
    return sum(resultlist)

resultlist = []
for x in range(2, 10000):
    oneway = sumfactors(x)
    if sumfactors(oneway) == x:
        if oneway != x:
            print "FOUND: %d, %d" % (oneway, x)
            resultlist.append(oneway)
            resultlist.append(x)

resultlist = set(resultlist)
print 'resultlist sum:', sum(resultlist)
