import random

f = open("example.csv", "w")

numGenerated = input("Enter the number of CSV values you would like to generate: ")
numGenerated = int(numGenerated)

for i in range(0,numGenerated):
    f.write(str(random.randrange(500)))
    day = random.randrange(7)
    if(day == 0):
        f.write(",Sunday")
    elif(day == 1):
        f.write(",Monday")
    elif(day == 2):
        f.write(",Tuesday")
    elif(day == 3):
        f.write(",Wednesday")
    elif(day == 4):
        f.write(",Thursday")
    elif(day == 5):
        f.write(",Friday")
    else:
        f.write(",Saturday")
    f.write("\n")
    
f.close()
