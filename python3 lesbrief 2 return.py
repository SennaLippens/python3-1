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
woord = input()
def reverse (woord):
    nieuw_woord = woord[::-1]
    print(nieuw_woord)
reverse(woord)

print("")
print("opdracht 3")
def is_priemgetal(num):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               print(num,"is geen priemgetal")
               break
        else:
           print(num,"is een priemgetal")
    else:
       print(num,"is geen priemgetal")
is_priemgetal(7)

print("")
print("opdracht 4")
woord = "acht"
def is_palindrome(woord):
    omgedraaid = woord[::-1]
    if omgedraaid == woord:
        print("het is een palindrome")
    else:
        print("het is geen palindrome")
is_palindrome(woord)

    
    
    


























