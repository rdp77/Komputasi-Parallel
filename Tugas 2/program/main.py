import random

def SoalA():
    result = []
    for i in range(0,10):
        if i%2==0:
            result.append(i)
    print(i)  

def SoalB():
    result = []
    for i in range(50,60):
        if i%2==1:
            result.append(i)
    print(result)

def SoalC():
    result = []
    for i in range(0,5):
        result.append(random.randrange(100,500))
    print(result)

SoalA()
SoalB()
SoalC()