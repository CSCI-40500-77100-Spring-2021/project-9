# -*- coding: utf-8 -*-
import csv
from io import StringIO


def fptp(ballots: str):
    f = StringIO(ballots)
    reader = csv.reader(f, delimiter=',')
    row1 = next(f)
    row1 = row1.strip()
    row1 = row1.split(",")
    results = {}

    for names in row1:
        names = names.strip()
        results[names] = 0

    for line in reader:
        index = line.index("x")
        candidate = row1[index]
        results[candidate] += 1

    winner = max(results, key=results.get)

    return {"winner": winner,
            "tallies": results,
            }
