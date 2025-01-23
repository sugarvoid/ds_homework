from classes import OrderedRecordArray


def second(x: list):  # Key on second element of record
    return x[1]


maxSize = 10  # Max size of the array
arr = OrderedRecordArray(maxSize, second, resizable=True)  # Create the array object
# Insert 10 items
for rec in [
    ("a", 3.1),
    ("b", 7.5),
    ("dog", 5),
    ("d", 3.1),
    ("e", 1.4),
    ("f", -1.2),
    ("g", 0.0),
    ("h", 7.5),
    ("i", 7.5),
    ("j", 6.0),
    ("i", 7.5),
    ("j", 6.0),
]:
    arr.insert(rec)
print("Array containing", len(arr), "items:\n", arr)
# Delete a few items, including some duplicates
for rec in [("g", 0.0), ("g", 0.0), ("b", 7.5), ("i", 7.5)]:
    print("Deleting", rec, "returns", arr.delete(rec))

print("Array after deletions has", len(arr), "items:\n", arr)

for key in [4.4, 6.0, 7.5]:
    print(
        "find(",
        key,
        ") returns",
        arr.find(key),
        "and get(",
        arr.find(key),
        ") returns",
        arr.get(arr.find(key)),
    )
