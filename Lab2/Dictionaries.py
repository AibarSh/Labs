car = {"brand": "Ford", "model" : "Mustang", "year" : 2005}
print(car.get("model"))
car["year"] = 1980
car["colour"] = "Deep_blue"
car.pop("brand")
print(car)
