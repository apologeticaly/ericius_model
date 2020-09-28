from states import states
from decimal import Decimal

def state_election():
    for key, value in states.items():
        id = key
        name = value[0]
        ec = value[1]
        d_2016_votes = int(value[2])
        r_20156_votes = int(value[3])
        t_2016_votes = int(value[4])
        d_2016_votes_p = (Decimal(value[2]) / Decimal(value[5]))
        r_2016_votes_p = (Decimal(value[3]) / Decimal(value[5]))
        t_2016_votes_p = (Decimal(value[4]) / Decimal(value[5]))
        total_2016_votes = value[5]
        past_5 = value[6]
        
        

        print(d_2016_votes_p * 100)


state_election()