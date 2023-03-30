gameList = ["Minecraft", "Roblox"]
gameList.append("Bawl Stars")
#print(gameList)

gameList.insert(1, "Call Of Duty")
#print(gameList)

gameList.insert(0, "Valorant")
#print(gameList)


import time
def AnimatedTriangle():
    numList1 = []
    while True:
        for i in range(1,11, 1):
            numList1.insert(0, i)
            print(numList1)
            time.sleep(0.05)

        for i in range(len(numList1) - 1):
            del numList1[-1]
            print(numList1)
            time.sleep(0.05)


numList1 = [5, 18, 89, 1, 200, 16, 20, 201, -100]

def our_max_function(anyList):
    curr_max = 0
    for eachNum in anyList:
        if eachNum > curr_max:
            curr_max = eachNum
    return curr_max
print(max(numList1))

print(our_max_function(numList1))

def our_min_function(anyList):
    curr_min = our_min_function(anyList)
    for eachNum in anyList:
        if eachNum < curr_min:
            curr_min = eachNum
    return curr_min