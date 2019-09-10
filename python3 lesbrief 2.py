print("lesbrief 2 van python 3")
print("opdracht 1")
def hoizeggen():
    for i in range(10):
        print("hooii")
hoizeggen()

print("")
print("opdracht 2")
def tafelvan5():
    for i in range(10):
        print((i+1)*5)
tafelvan5()

print("")
print("opdracht 3")
def hoihoi(getal):
    for i in range(getal):
        print("heey")
hoihoi(7)

print("")
print("opdracht 4")
def heyheyhey(woord, getal):
    for i in range(getal):
        print(woord)
heyheyhey("hatshu", 3)

print("")
print("opdracht 5")
iets = ['h', 'e', 'y', 'y']
lengte = len(iets)
def halvekerstboom(getal, x):
    for i in range(getal):
        print(x[i] * (i+1))
halvekerstboom(lengte, iets)
