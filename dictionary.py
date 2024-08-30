# Dictionaries
# Putting values in key-value pairs.
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

# Same dictionary with constructor function:

band2 = dict(vocals="Plant", guitar="Page")
print(band)
print(band2)

# Checking the type

print(type(band))
print(len(band))

# Accessing items in a dictionary - by key

print(band["vocals"])
print(band.get("guitar"))

# List all keys

print(band.keys())

# List all values

print(band.values())

# List of key-value pairs as tuples

print(band.items())

# Verify if a key exists in a dictionary

print("guitar" in band)
print("trianble" in band)

# Change values

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove Items

print(band.pop("bass"))
print(band)

# Let's add a new value again:

band["drums"] = "Bonham"
print(band)

# Removes the last item or in this case key-value pair added to the dictionary
print(band.popitem())
print(band)

# Delete or Clear Items

band["drums"] = "Bonham"
del band["drums"]
print(band)

# Clearing or emptying out an entire dictionary

band2.clear()
print(band2)

# delete an entire dictionary
# del band2
print(band2)

# How not to copy: = below only creates a reference

band2 = band  # creates a reference= refers to same place in the memory
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["Drums"] = "Dave"
# print(band)

# This above is not how you want to create a Copy

# Copying Dictionaires: Right Way

band2 = band.copy()
band2["Drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# Creating Copies using the constructor function dict()

band3 = dict(band)
print("Good Copy!")
print(band3)

# Nested Dictionaries

member1 = {
    "name": "plant",
    "instrument": "vocals"

}
member2 = {
    "name": "page",
    "instrument": "guitars"

}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No Duplicates allowed

nums = {1, 2, 2, 3}
print(nums)

# True is dupe of 1 and zero is a dupe of false.

# worth noting that 1 was before true and true is dupe of 1 so it ignored the dupe true and vice versa with false.
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# checking if a value is in a set

print(2 in nums)

# but you cannot refer to an element in the set with an
# index position or a key

# Adding a new value to a set

nums.add(8)
print(nums)

# Add elements from one set to another set

morenums = {5, 6, 7}
nums.update(morenums)
print(morenums)
print(nums)

# Update can be used with lists, tuples, and dictionaries too.

# Merge two sets to createa new set

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates from both sets

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)

one.isdisjoint(two)
print(one)

one.issuperset(two)
print(one)
