import csv
import matplotlib.pyplot as plt
import numpy as np


boxers = []


with open('boxers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        boxers.append(row)

# get heavy boxers
heavy =[]

for boxer in boxers:
    if boxer[3] == "heavy":
        heavy.append(boxer)


# get middle boxers
middle =[]

for boxer in boxers:
    if boxer[3] == "middle":
        middle.append(boxer)

# plot heavy boxers
xaxis = []
yaxis = []

for boxer in heavy:
    xaxis.append(boxer[1])
    yaxis.append(float(boxer[2]))

# 
mxaxis = []
myaxis = []

for boxer in middle:
    mxaxis.append(boxer[1])
    myaxis.append(float(boxer[2]))

plt.plot(xaxis, yaxis)
plt.plot(mxaxis, myaxis)
plt.ylim(0, 500)
plt.show()

print(heavy)
print(middle)