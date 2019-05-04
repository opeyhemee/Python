#Initialized dictionary called "thisdict"
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "Blue"
}


#Getting the value of model
print(thisdict["model"])
#print(thisdict.get("model"))


#Change the value of a dictionary key - model
thisdict["model"] = "Subway"

#loop through a dictionary without printing the values
for D in thisdict:
    print(D)

#loop through a dictionary and print the values
for D in thisdict:
    print(thisdict[D])

#You can also use the values() function to return values of a dictionary
for D in thisdict.values():
    print("Just values",D)

#Loop through both keys and values, by using the items() function
for x, y in thisdict.items():
  print(x, y)

#Check if a key is a dictionary
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("ko jo!")

  
#Print entire dictionary

print(thisdict)

print(len(thisdict))

#The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

#The pop() method removes the last item in the dictionary:
thisdict.popitem()
print(thisdict)

#del removes the specified item
del thisdict["brand"]
print(thisdict)


#Copy dictionary
myOlddict= thisdict.copy()
update = input("What is the year?: ")
myOlddict["year"] = update
print(myOlddict)


#clears the dic and returns curly braces
thisdict.clear()
print(thisdict)



"""

1. Use the Insert function from the previous assignment - Google "insert to a list function python"
2. Add all assignments and python files to Github
"""
