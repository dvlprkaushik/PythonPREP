# Tuple definition
t = (1, 2, 2, 3, 3, 3)

# .count(value) - Counts occurrences of a value
print(t.count(2))  # Output: 2

# .index(value, start, end) - Finds the index of the first occurrence of a value
print(t.index(3))  # Output: 3

# len(tuple) - Returns the number of elements in the tuple
print(len(t))  # Output: 6

# tuple(iterable) - Converts an iterable into a tuple
lst = [4, 5, 6]
t2 = tuple(lst)
print(t2)  # Output: (4, 5, 6)
