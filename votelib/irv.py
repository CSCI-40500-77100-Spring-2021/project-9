import csv


def irv():
    # create a list from csv
    with open("tests\data\irv.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # remove extra list
    data.pop(-1)

    # remove first column of the data
    for x in data:
        x.pop(0)

    # store candidates then remove from data
    candidates = data[0]
    data.pop(0)

    # convert first row into integers
    for i in range(0, len(data[0])):
        data[0][i] = int(data[0][i])

    # calculate the winning number of votes needed
    winning_votes = int(sum(data[0]) / 2 + 1)

    # until winner is found, it will remain empty, while loser list increases
    winner = None
    loser = []

    # set all candidates to 0
    candidates = dict((k, 0) for k in candidates)

    while winner is None:
        # calculate first place votes
        for i in range(0, len(data[1])):
            candidates[data[1][i]] += data[0][i]

        for key in candidates:
            # if candidate has more winning votes, voting stops
            if candidates[key] >= winning_votes:
                winner = key
                return {'winner': winner, 'votes': candidates.get(winner)}

        # if not found, remove loser from candidate
        min_value = min(candidates.values())
        for keys in candidates:
            if candidates[keys] == min_value:
                loser.append(keys)

        for i in range(0, len(loser)):
            if loser[i] in candidates:
                del candidates[loser[i]]

        # remove losers from data and shift data up
        for i in range(0, len(loser)):
            for j in range(1, len(data)):
                for k in range(0, len(data[j])):
                    if data[j][k] == loser[i] and j + 1 != len(data):
                        data[j][k] = data[j + 1][k]
                        data[j + 1][k] = loser[i]

        # remove last list
        data.pop(-1)
        # reset vote count
        candidates = dict((k, 0) for k in candidates)




check = irv()

print(check)
