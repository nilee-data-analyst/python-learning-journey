# accessing items without using keys() & values() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict: # returns key names
    print(x)

for x in thisdict: # returns values
    print(thisdict[x])

# The del keyword can also delete the dictionary completely is not used properly
del thisdict["model"] # reloves item with specified keyname
print(thisdict)
# -----------------------------------------------------------------------

del thisdict
print(thisdict) # this will cause an error because "thisdict" no longer exists.

