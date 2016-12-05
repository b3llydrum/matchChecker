#! /usr/bin/env python3

from Levenshtein import distance
from pprint import pprint

def checker(list, lDist):
    matches = []
    for i in range(len(list)):
        for j in list[i + 1:]:
            if distance(list[int(i)], j) <= int(lDist):
                matches.append({
                    'nameA' : list[i],
                    'nameB' : j,
                    'lDist' : lDist
                    })
    pprint(matches)
