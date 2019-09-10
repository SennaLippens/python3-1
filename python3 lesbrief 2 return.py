print("dit worden de opdrachten bij return van python lesbrief 2")
print("")

print("opdracht 1")
g1 = int(input("getal 1: "))
g2 = int(input("getal 2: "))
g3 = int(input("getal 3: "))
def max_van_3(g1, g2, g3):
    if g1 > g2:
        if g1 > g3:
            print("getal 1 is de grootste")
    elif g2 > g1:
        if g2 > g3:
            print("getal 2 is de grootste")
    else:
        print("getal 3 is de grootste")
max_van_3(g1, g2, g3)

print("")
print("opdracht 2")
woord = "hey"
def reverse (woord):
    nieuw_woord = woord[::-1]
    print(nieuw_woord)
reverse(woord)
    
    
    
    
