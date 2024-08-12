# Example dictionary
my_dict = {"a": 1, "b": 2}

# .get(key, default) - Returns the value for the specified key, or default if key is not found
print(my_dict.get("a"))          # Output: 1
print(my_dict.get("c", "Not Found"))  # Output: Not Found

# .keys() - Returns a view of all the keys in the dictionary
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

# .values() - Returns a view of all the values in the dictionary
print(my_dict.values())  # Output: dict_values([1, 2])

# .items() - Returns a view of all key-value pairs in the dictionary
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

# .update(other_dict) - Updates the dictionary with key-value pairs from another dictionary or iterable
my_dict.update({"b": 3, "c": 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# .pop(key, default) - Removes the specified key and returns its value, or default if key is not found
print(my_dict.pop("a"))  # Output: 1
print(my_dict)  # Output: {'b': 3, 'c': 4}

# .popitem() - Removes and returns the last key-value pair
print(my_dict.popitem())  # Output: ('c', 4)
print(my_dict)  # Output: {'b': 3}

# .clear() - Removes all key-value pairs from the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# .copy() - Returns a shallow copy of the dictionary
my_dict = {"a": 1, "b": 2}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}
