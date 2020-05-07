# readonly list
point1 = (1, 2)
point2 = 1, 2

print(type(point1))
print(point1)
print(type(point2))
print(point2)

x = 1
print(type(x))
print(x)

x1 = 1,
print(type(x1))
print(x1)

empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

# tuple concatenation
p1 = (1, 2)
p2 = (3, 4)
p_con = p1 + p2

print(p_con)

# multiplication
multiplied_tuple = (1, 2) * 3
print(multiplied_tuple)

# tuple explicite
p_expl = tuple([1, 2])
print(p_expl)

p_expl_str = tuple("Hello wrold!")
print(p_expl_str)

# accessing elements
some_point = (1, 2, 3, 4)
print(some_point[1])
print(some_point[2:4])

if 3 in some_point:
    print(f"{3} exists in {some_point}")
    
# causing error
some_point[1] = 10