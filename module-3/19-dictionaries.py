point = {"x": 1, "y": 2}
#only immutable object for keys
print(point)

"""
set(..)
list(..)
tuple(..)
dict(..)
"""

point1 = dict(x=1, y=2) # "x=1" is so called key-word argument
print(point1["y"])
point1["y"] = 100
print(point1["y"])
point1["z"] = 200
print(point1)

if "z" in point1:
    print("z in point1")
    
print(point1.get("h")) # safe get -> not found return None
print(point1.get("h", 0)) # return default if not found

del point1["z"]
print(point1.get("z"))

print("iterate over dictionary keys...")
for key in point1:
    print(key)

print("iterate over dictionary...")
for item in point1.items():
    print(item)

print("iterate over dictionary with tuple extraction...")
for key, val in point1.items():
    print(key, "-", val)
