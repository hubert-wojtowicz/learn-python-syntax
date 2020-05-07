course = "This is python course"
print(len(course))

course += course
print(len(course))
print(course[0])
print(course[-1])
print(course[-21])
print(course[0:4])
print(course[:4])
print(course[0:])
print(course[:])

## pythom strings are imutable as integers

message = 'This is "Course'
print(message)

#escape char
message1 = "This is \"Course"       
print(message1)

# other escapes \" \' \\ \n