# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    #print(sportTeams[1][0])

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True) # the [0] in t[1][0] is unnecessary...?
    print(sortedTeams)
    sortedTeams2 = sorted(sportTeams, key=lambda t: t[1], reverse=True)
    print(sortedTeams2)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(False) # top item removed... even w/ False
    print("Top team: ", tm, wl)
    # test = teams.popitem(False)
    # print(test)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    print(teams)

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    #b = OrderedDict({"a": 1, "c": 3, "b": 2, 'd': 4})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b) # changes after 3.7 confuses this... 
    # the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.
    # https://stackoverflow.com/questions/34305003/difference-between-dictionary-and-ordereddict


if __name__ == "__main__":
    main()
