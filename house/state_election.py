import random

def state_election(d,r):      
    wins = []

    for _ in range(100):
        votes = random.choices(["D", "R", "T"], [d*random.randint(100, 103),r*random.randint(100, 106),random.randint(0,1)], k=1)
        # print(votes.count("D"), votes.count("R"), votes.count("T"), len(votes))
        # print(round(((votes.count("D")/population) * 100), 2),round(((votes.count("R")/population) * 100), 2),round(((votes.count("T")/population) * 100), 2))
        if votes.count("D") > 0:
            wins.append("D")
        
        if votes.count("R") > 0:
            wins.append("R")

        if votes.count("T") > 0:
            wins.append("T")

    state_election_results = [wins.count("D"), wins.count("R"), wins.count("T")]

    return state_election_results