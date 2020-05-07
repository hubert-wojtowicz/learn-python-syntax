names = ["AJohn", "Marry"]

# found = False
# for name in names:
#     if(name.startswith("J")):
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")

#instead:

for name in names:
    if(name.startswith("J")):
        print("Found")
        break
else:
    print("Not found")