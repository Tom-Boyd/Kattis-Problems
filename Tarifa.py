import sys

readin = []
for i in sys.stdin:
    readin.append(int(i))

X = readin[0]
monthVals = readin[2:]

dataAvailable = X
for value in monthVals:
    dataAvailable += (X - value)

print(dataAvailable)
    


    
