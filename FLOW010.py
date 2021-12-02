x=int(input())
for i in range(x):
    y=input()
    if y=="b" or y=="B":
        print("BattleShip")
    elif y=="c" or y=="C":
        print("Cruiser")
    elif y=="d" or y=="D":
        print("Destroyer")
    else y=="f" or y=="F":
        print("Frigate")
    
