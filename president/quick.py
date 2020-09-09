import random

def state(d,r,t,population):
    votes = random.choices(["D", "R", "T"], [d*random.uniform(1, 1.025),r*random.uniform(1, 1.025),t*random.uniform(1, 1.025)], k=population)
    # print(votes.count("D"), votes.count("R"), votes.count("T"), len(votes))
    # print(round(((votes.count("D")/population) * 100), 2),round(((votes.count("R")/population) * 100), 2),round(((votes.count("T")/population) * 100), 2))
    if votes.count("D") > 0:
        return "D"
    
    if votes.count("R") > 0:
        return "R"

    else:
        return "T"

def sim():
    wins = []
    for _ in range(10000):
        wins.append(state(d=47.5,r=47.5,t=5,population=1))
    print(wins.count("D"), wins.count("R"), wins.count("T"))

sim()
