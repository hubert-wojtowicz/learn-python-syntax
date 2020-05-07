course = "   Python Programming   "
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip()) #rstrip, lstrip

print(course.find("pro")) #-1 not fund
print(course.find("Pro")) # found
print(course.replace(" ", "-"))
print("Programming" in course)
print("Programming" not in course)
