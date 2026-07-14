
# create dictonary( dictonary = key : value )
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# accessing items
print(thisdict["model"])
print(thisdict.get("model"))

  # 1. accesing keys
x = thisdict.keys()
print(x)

  # 2. accessing values
x = thisdict.values()
print(x)

  # 3. accessing items
x = thisdict.items()
print(x)

# change item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# add and remove item
# add item
thisdict["color"] = "red" # use a  nw index key and assign a value to it
print(thisdict)

# remove item
 # 1. pop() - removes item with the specified key name
thisdict.pop("model")
print(thisdict)

 # 2. popitem() - method removes the last inserted item
thisdict.popitem()
print(thisdict)
 
 # 3. del - removes the item with the specified key name
del thisdict["year"]
print(thisdict)

 # 4. clear() - empties the dictionary
thisdict.popitem()
print(thisdict)

# loop through a dictonary
mydict = {"name":"Nilee",
          "age":34,
          "country":"India"}

 # 1. keys
for x in mydict.keys():
  print(x)

  # 2. values
for x in mydict.values():
  print(x)

  # 3. items
for x, y in mydict.items():
  print(x , y)

# copy  a dictionary
copy_mydict = mydict.copy() #using copy()
print(copy_mydict)

copy_mydict = dict(mydict) #using dict()
print(copy_mydict)

# nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# access items in nested dictionaries
print(myfamily["child2"]["name"])

# loop through nested dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])