x = "1"
id = 0
car = {}

class Cardat:
    def __init__(self,brand,year,color,milege):
        self.brand = brand
        self.year = year
        self.color = color
        self.milege = milege

#log in dat
while x == "1":
    id = id + 1
    print ("Car ", id)
    
    brand = str(input("Brand:"))
    year = int(input("Year: "))
    color = str(input("Color: "))
    milege = float(input("Milege in Km: "))
    car[id] = Cardat(brand,year,color,milege)

    x = str(input("type 1 to repeat, type any for search: "))

#seek for those who seek
while True:
    id = int(input("Search Car #: "))
    if id in car:
        print ("Car ", id, " specification:")
        print ("Brand: ", car[id].brand)
        print ("Year: ", car[id].year)
        print ("Color: ", car[id].color)
        print ("milege: ", car[id].milege, "km")
    
    else:
        print ("Car ID not found")
