import pandas as pd
from csv import reader, writer

base = pd.read_csv('Foodsort1.csv')

# Read in the columns
time = base['timetag']
name = base['name']
people = base['people']
id = base['id']
rest = base['resteraunt']
rank = []

# Loop to read through the time and add it as a sum
# All done very manually. Could use regex as well. 
for i in range(time.size):
    s = 0
    t = time[i]
    if 'hours ago.' in t:
        if t[1].isdigit():
            s += 60* (int(t[0])*10 + int(t[1]))
        else:
            s += 60 * (int(t[0]))
    elif len(t) > 22:
        if t[1].isdigit():
            s += 60* (int(t[0])*10 + int(t[1]))
        else:
            s += 60 * (int(t[0]))

        for i in range(12, 25):
            if sum(map(t[i:].count, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) > 1:
                if t[i].isdigit() and t[i + 1].isdigit():
                    s += 10*int(t[i]) + int(t[i + 1])
            else:
                if t[i].isdigit():
                    s += int(t[i])
    else:
        if t[1].isdigit():
            s += 10*int(t[0]) + int(t[1])
        else:
            s += int(t[0])



    #Multiply by negative 1
    rank.append(-1*s)

#Heuristic factor (122) to multiply by the number of people who have eaten the past two days
pplrank = []
for i in range(id.size):
    pplrank.append(122*(people[i]))

newHer = {}
for i in range(id.size):
    newHer[id[i]] = (pplrank[i] + rank[i]), name[i], rest[i], people[i], time[i]

# Creates CSV file from dictionary 
print(len(newHer))
with open('Foodsort1.csv') as rdr:
    with open('heurestic.csv', 'w') as wrt:
        csv_writer = writer(wrt)
        csv_reader = reader(rdr)
        row = ['id','name', 'resteraunt', 'people', 'time', 'heurestic']
        csv_writer.writerow(row)
        for k, v in newHer.items():
            l = []
            l.append(k)
            l.append(v[1])
            l.append(v[2])
            l.append(v[3])
            l.append(v[4])
            l.append(v[0])
            csv_writer.writerow(l)


