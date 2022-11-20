import time
import datetime
import pandas as pd
import sys
import random
from csv import reader, writer
# Create two heurestic algorithms:
# Searching for more recent purchases - Call this Fresh Algorithm
# Searching for more purchases in last 24 hours - Call this Popular Algorithm
# and one query/search


foodDishes = pd.read_csv('Food.csv')
id, name = foodDishes["id"], foodDishes["name"]
locations = ['Hogwarts', 'Leaky Cauldron', 'The Burrow', 'Shell Cottage', 'Godrics Hollow', 'Diagon Alley', 'Hogsmeade', 'Kings Cross', 'Gringots', 'Ollivanders']
numPeople = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
numPeople2 = ['1', '2', '3']
numPeople3 = ['0', '1', '2', '3', '4', '5', '6', '7']


lisCol = ['Resteraunt']
lisColNum = ['People who Purchased']
lisColTime = ['Time Tag']
for i in range(id.size):
    lisCol.append(random.choice(locations))
    rand = random.randint(1, 2880)
    oupt = str(rand) + ' minutes'
    if rand > 60:
        oupt = str(rand//60) + ' hours'
        if rand % 60 != 0:
            oupt += ' and ' + str(round(rand%60)) + ' minutes'
    oupt += ' ago.'
    lisColTime.append(oupt)
    if i <= 1000:
        lisColNum.append(random.choice(numPeople))
    if i> 1000 and i <= 9000:
        lisColNum.append(random.choice(numPeople2))
    if i > 9000:
        lisColNum.append(random.choice(numPeople3))


with open('Food.csv', 'r') as rdr, \
    open('Foodsort1.csv', 'w', newline='') as wrt:
    csv_reader = reader(rdr)
    csv_writer = writer(wrt)
    for row in csv_reader:
        if row[0] == 'id':
            row.append('Resteraunt')
            row.append('People')
            row.append('Time Tag')
        else:
            index = int(row[0])
            row.append(lisCol[index])
            row.append(lisColNum[index])
            row.append(lisColTime[index])
        csv_writer.writerow(row)

df = pd.read_csv('heurestic2.csv')
for i in range(len(df)):
    df.loc[i, 'id'] = i + 1
df.to_csv('heurestic2.csv')

    
