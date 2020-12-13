import math

def getWinProbability(ra, rb):
    return 1 / (1 + 10 ** ((rb - ra) / 400))

def team_ratings(ratings):
    left = 1
    right = 10000
    for tt in range(100):
        r = (left + right) / 2
        rwinsProbability = 1
        for i in range(len(ratings)):
            rwinsProbability *= getWinProbability(r, ratings[i])

        rating = math.log10( (1 / rwinsProbability) - 1) * 400 + r
        if rating > r:
            left = r
        else:
            right = r
    return int((left + right) / 2.0)

