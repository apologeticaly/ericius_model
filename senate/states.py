import csv
with open('priors/states_simple_.csv', mode='r') as infile:
    reader = csv.reader(infile)
    states = {rows[0]:rows[1:11] for rows in reader}
    del states['id']