# -*- coding: utf-8 -*-

import csv
from io import StringIO

def fptp(ballots: str):
    # create a csv reader from the string argument
    f = StringIO(ballots)
    reader = csv.reader(f, delimiter=',')

    # get the first row, which has candidate names
    row = next(f)
    candidates = row.strip().split(',')

    # set up the tally dictionary with every candidate having 0 votes
    tallies = {}
    for c in candidates:
        tallies[c] = 0

    # count votes based on index of x
    for line in reader:
        index = line.index('x')
        candidate = candidates[index]
        results[candidate] += 1

    # grab the key with the highest value
    winner = max(results, key=results.get)

    return {'winner': winner, 'tallies': tallies}
