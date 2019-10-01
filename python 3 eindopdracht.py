producten = {"chocola": 1.00,
             "koffie": 0.90,
             "frikandelbroodje": 1.50,
             "vivit": 1.20,
             "pepernoten": 1.50,
             "kaas": 2.00,
             "soep": 1.50,
             "appelflappen": 2.00}
mandje = {}
boodschappen_doen = True
inputt = ""
som = 0
def welkom():
   print(" ------welkom bij de supermarkt van Noah en Senna------")
def toon_menu():
   print ("kies 1 om de producten te zien")
   print ("kies 2 om je winkelmandje te zien")
   print ("kies 3 om producten uit je winkelmandje te verwijderen")
   print ("kies 4 om je subtotaal te zien")
   print ("kies 5 om producten aan je winkelmandje toe te voegen")
   print ("kies 6 om af te rekenen")


def toon_producten():
   for key in producten:
      print("")
      print(key)
      print(producten[key])
      print("")
def toon_mandje():
   for key in mandje:
      print("")
      print(key)
      print(mandje[key])
      print("")
def afrekenen():
   print("te betalen: ")
   som = sum(mandje.values())
   print(som)
   return False
def toevoegen():
   input0 = input("wat wil je toevoegen? ")
   if input0 in producten:
      ding = producten[input0]
      mandje[input0] = ding
      print(input0 + " toegevoegd voor €" + str(ding))
   else:
      print("dat product hebben wij niet")
def totaal():
      print("subtotaal: ")
      som = sum(mandje.values())
      print(som)
def verwijderen():
   input1 = input("welk product wil je verwijderen? ")
   if input1 in mandje:
      del mandje[input1]
      print(input1 + "uit mandje verwijderd")
   else:
      print("dat zit niet in je mandje ")
while boodschappen_doen == True:
     toon_menu()
     inputt = input("")
     if inputt == "1" :
        toon_producten()
     elif inputt == "2" :
         toon_mandje()
     elif inputt == "3" :
         verwijderen()
     elif inputt == "4" :
         totaal()
     elif inputt == "5" :
         toevoegen()
     elif inputt == "6" :
         boodschappen_doen = afrekenen()
     else:
         print("zeg een getal van 1 t/6 alsjeblieft")
