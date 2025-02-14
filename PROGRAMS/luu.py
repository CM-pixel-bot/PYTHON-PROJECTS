BCA = {
    "name:": "charan",
    "usn:": "1ruabca240016",
}

# Printing values (for each key)
for key in BCA:
    print(BCA[key])

# Print keys
print("here are the keys:")
for key in BCA:
    print(key)

# Add new key-value pair
BCA["spec:"] = "AI/ML"

# Print values only once
print("here are the values:")
for values in BCA.values():
    print(values)

# Print keys and values (items) only once
print("here are the items (keys and values):")
for key, value in BCA.items():
    print(key, value)

# Print dictionary items, values, and keys just once
print("Dictionary items:", BCA.items())
print("Dictionary values:", BCA.values())
print("Dictionary keys:", BCA.keys())

# Check if the spec key exists
if "spec:" in BCA:
    print("it is AI/ML")
else:
    print("it is not AI/ML")

