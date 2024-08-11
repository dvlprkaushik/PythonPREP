# Create a set of toys
toys = {"car", "ball", "doll" ,"ball","ball"}

print(toys)

# Add a new toy to the set
toys.add("teddy bear")

print(toys)  # Output: {'car', 'ball', 'doll', 'teddy bear'}

# Remove a toy from the set
toys.remove("doll")

print(toys)  # Output: {'car', 'ball', 'teddy bear'}

# Remove a toy without causing an error if it's not there
toys.discard("doll")

print(toys)  # Output: {'car', 'ball', 'teddy bear'}  # No error even if 'doll' is not present

# Remove and return an arbitrary toy from the set
removed_toy = toys.pop()

print(removed_toy)  # Output: (an arbitrary toy, e.g., 'car')
print(toys)  # Output: {'ball', 'teddy bear'}  # 'car' has been removed

# Remove all toys from the set
toys.clear()

print(toys)  # Output: set()  # The set is now empty

# UNION & INTERSECTION 

# Your set of toys
your_toys = {"car", "ball", "doll"}

# Your friend's set of toys
friend_toys = {"doll", "teddy bear", "blocks"}

# Union of both sets (all unique toys)
all_toys = your_toys.union(friend_toys)
print("Union (All Unique Toys):", all_toys)  
# Output: {'car', 'ball', 'doll', 'teddy bear', 'blocks'}

# Intersection of both sets (toys you both have)
common_toys = your_toys.intersection(friend_toys)
print("Intersection (Common Toys):", common_toys)  
# Output: {'doll'}
