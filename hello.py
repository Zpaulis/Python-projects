print ("Hello")
food = "kartupelis"
print (food)
print (type(food))
print (food[0])
print (food[-1])
print (len(food))
for c in food:
    print (c, end = " - ")
print ("EOF")
print (food[2:4])
print (food, food[::2])
print (food, food[::-1])
new_food = food.replace("p", "m")
print (new_food)
big_food = "LIELS " + food
print (big_food, big_food.lower().count("l"))
print ("Pauls" > "Paulis")
print (food.find("t"))
print (food.index("t"))
print (food.isalpha())