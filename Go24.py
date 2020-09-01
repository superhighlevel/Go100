import math
pos=[0,0]
while True:
    Input_mov = input()
    if not Input_mov:
        break
    Mov = Input_mov.split(" ")
    Direct = Mov[0]
    Steps = int(Mov[1])
    if Direct == "UP":
        pos[0]+=Steps
        print(pos)
    elif Direct == "DOWN":
        pos[0]-=Steps
        print(pos)
    elif Direct == "RIGHT":
        pos[1]+=Steps
        print(pos)
    elif Direct == "LEFT":
        pos[1]-=Steps
        print(pos)
    else:
        pass
print(pos)
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))


