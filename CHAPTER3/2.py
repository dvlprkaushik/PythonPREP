name = "Kaushik"

# 1. .lower() - Converts the string to lowercase
print(name.lower())  # Output: "kaushik"

# 2. .upper() - Converts the string to uppercase
print(name.upper())  # Output: "KAUSHIK"

# 3. .strip() - Removes any leading and trailing spaces
name_with_spaces = "  Kaushik  "
print(name_with_spaces.strip())  # Output: "Kaushik"

# 4. .replace(old, new) - Replaces a substring with another substring
print(name.replace("Ka", "Ta"))  # Output: "Taushik"

# 5. .find(substring) - Returns the index of the first occurrence of a substring
print(name.find("ush"))  # Output: 2

# 6. .startswith(prefix) - Checks if the string starts with a specific prefix
print(name.startswith("Kau"))  # Output: True

# 7. .endswith(suffix) - Checks if the string ends with a specific suffix
print(name.endswith("ik"))  # Output: True

# 8. .split(separator) - Splits the string into a list based on a separator
full_name = "Kaushik Kumar"
print(full_name.split())  # Output: ['Kaushik', 'Kumar']

# 9. .join(iterable) - Joins elements of an iterable with the string as a separator
words = ['Hello', 'World']
print(" ".join(words))  # Output: "Hello World"

# 10. .count(substring) - Counts the number of times a substring appears in the string
print(name.count("a"))  # Output: 1
