# **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

details = {}

def addNameAge(name,age) :
     details[name] = age

def updateNameAge(name,age) :
     if name in details :
          details[name] = age
     else : 
        print(f"{name} does not exist in dictionary.")

def delNameAge(name) :
     if name in details :
          del details[name]

addNameAge("John",25)
print(details)
updateNameAge("John",26)
print(details)
delNameAge("John")
print(details)