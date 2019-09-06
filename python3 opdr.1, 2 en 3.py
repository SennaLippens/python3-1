bedrijven = {"Apple": "Steve Jobs", "Microsoft": "Bill Gates"}
print("hier komt de maken van apple")
print(bedrijven["Apple"])
print("hier komt de maker van apple")
print(bedrijven["Microsoft"])
print(bedrijven.keys())
print("")
print("nu komt opdracht 2")
del bedrijven["Apple"]
for key in bedrijven:
    print(key)

