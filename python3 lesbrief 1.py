bedrijven = {"Apple": "Steve Jobs", "Microsoft": "Bill Gates"}
print("hier komt de maken van apple")
print(bedrijven["Apple"])
print("hier komt de maker van apple")
print(bedrijven["Microsoft"])

print("")
print("dit is opdracht 3")
print(bedrijven.keys())

print("")
print("nu komt opdracht 2")
del bedrijven["Apple"]
for key in bedrijven:
    print(key)
    
print("")
print("opdracht 4!!")
if "Microsoft" in bedrijven:
    print("microsoft zit erin!")

print("")
print("opdracht 5!!")
fruit = {"banaan": "geel", "appel": "rood"}
apps = {"spotify": "muziek", "netflix": "films"}
voorwerpen = {"bed": "slapen", "bank": "zitten"}
def alles(fruit, apps):
    return(fruit.update(apps))
def alles2(fruit, voorwerpen):
    return(fruit.update(voorwerpen))
alles(fruit, apps)
alles2(fruit, voorwerpen)
print(fruit)


