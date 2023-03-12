# Operations onSet

# create set
a = set([1, 2, 3, 4, 5])
b = set([2, 4, 6, 8, 10])

print("set a is: ", a)
print("set b is: ", b)

# Intersection of set

result1 = a.intersection(b)
print("Intersection of set a & b is: ", result1)

# Union of set

result2 = a.union(b)

print("Union of set a & b is: ", result2)

# set difference

result3 = a.difference(b)

print("set difference is: ", result3)

result3 = b.difference(a)

print("set difference is: ", result3)

# symmetric difference

result4 = a.symmetric_difference(b)

print("symmetric difference is: ", result4)

# clear set

result5 = a.clear

print("After clear set a: ", result5)


# Thanks for Watching

