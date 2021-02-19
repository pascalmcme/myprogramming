car = {"make": "ford","price":"123","owner": {"firstname":"Fred"}}

print(car)
print(type(car))

make = car['make']
notmake = car.get("dsadsa") #check if it exists
print(notmake)
print(make)


'''  # comment out
car["model"] = "focus"
print(car)
print(car["owner"]["firstname"])

'''