from states import states
from progress.bar import Bar
from state_election import state_election
from decimal import Decimal, ROUND_UP
from termcolor import colored
from datetime import date
import csv
from states import states
from terminaltables import AsciiTable, SingleTable
import random

def federal_election():
    results = {}
    output = {}
    wins = []
    ec_d = 0
    ec_r = 0
    simulations = 1000

    bar = Bar('Progress', max=simulations)
    for key, value in states.items():
        results[key] = []

    for _ in range(simulations):
        ec_temp_d = 0
        ec_temp_r = 0
        for key, value in states.items():
            n = state_election(int(value[1]), float(value[2]), float(value[3]), random.randint(2,4), float(value[5]), float(value[6]), float(value[7]))
            results[key].append(n)

            if n[0] > n[1]:
                ec_temp_d = ec_temp_d + n[3]
                ec_d = ec_d + n[3]

            if n[0] < n[1]:
                ec_temp_r = ec_temp_r + n[3]
                ec_r = ec_r + n[3]

            if n[0] == n[1]:
                ec_temp_r = ec_temp_r + n[3]
                ec_r = ec_r + n[3]

        if ec_temp_d > ec_temp_r:
            wins.append("D")

        if ec_temp_d < ec_temp_r:
            wins.append("R")

        if ec_temp_d == ec_temp_r:
            wins.append("T")

        bar.next()
    
    for key, value in results.items():
        output[key] = [0,0,0,0,0,0, "T"]

        for i in results[key]:
            output[key][0] += i[0]
            output[key][1] += i[1]
            output[key][2] += i[2]

            if i[0] > i[1]:
                output[key][3] += 1
            
            if i[0] < i[1]:
                output[key][4] += 1

            if i[2] > (i[1] + i[0]):
                output[key][5] += 1

            if i[0] == i[1]:
                output[key][4] += 1


    for i in results[key]:
        output[key][0] = round(output[key][0], 2)
        output[key][1] = round(output[key][1], 2)
        output[key][2] = round(output[key][2], 2)
        pass
    
    se_table_data = [
    [colored('STATE'), colored('D VOTES %', 'white', 'on_blue'), colored('R VOTES %', 'white', 'on_red'), colored('T VOTES %', 'grey', 'on_white'), colored('D WINS %', 'white', 'on_blue'), colored('R WINS %', 'white', 'on_red'), colored('T WINS %', 'grey', 'on_white'), "EC"]
    ]

    for key, value in output.items():
        name = ""
        if value[0] > value[1]:
            name = "D"
        
        if value[1] >= value[0]:
            name = "R"
        se_table_data.append([key, round(value[0]/1000, 2),  round(value[1]/1000, 2),  round(value[2]/1000, 2),  round(value[3]/10, 2),  round(value[4]/10, 2),  round(value[5]/10, 2), name])
    
    se_table = SingleTable(se_table_data)

    se_table.title = 'GE Simulation'
    print('Done')
    print (se_table.table)
    print(round(wins.count("D")/10, 0), round(wins.count("R")/10, 0), round(wins.count("T")/10, 0), ec_d/1000, ec_r/1000)

    today = date.today()
    with open('results/results-president-' + today.strftime("%m-%d-%Y") + '.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["id", "name", "ec", "party", "democrat", "republican", "third", "democrat_win", "republican_win", "third_win", "winner"])
        for key, value in output.items():
            democrat = round(value[0]/1000, 2)
            republican = round(value[1]/1000, 2)
            third = round(value[2]/1000, 2)
            democrat_win = round(value[3]/10, 2)
            republican_win = round(value[4]/10, 2)
            third_win = round(value[5]/1000, 2)
            winner = ""
            if democrat > republican:
                party = 3
                winner = "D"

                if democrat - republican > 5:
                    party = 2
                
                    if democrat - republican > 10:
                        party = 1

                    else:
                        pass

                else:
                    pass
            
            if republican > democrat:
                party = 4
                winner = "R"
                if republican - democrat > 5:
                    party = 5
                
                    if republican - democrat > 10:
                        party = 6

                    else:
                        pass

                else:
                    pass

            filewriter.writerow([key, states[key][0], states[key][1], party, democrat, republican, third, democrat_win, republican_win, third_win, name])
            
    print('outputted as results-president-' + today.strftime("%m-%d-%Y") + '.csv')

federal_election()