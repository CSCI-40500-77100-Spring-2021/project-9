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
        tallies[candidate] += 1

    # get max value
    max_value = tallies.get(max(tallies))

    # get winners and ties
    winners = {key for key, val in tallies.items() if val == max_value}

    # report metrics data
    record_usage()

    return {'winners': winners, 'tallies': tallies}
