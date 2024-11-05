import bisect

numbers = [2, 4, 6, 8, 10]

# Find the index to insert 7
index = bisect.bisect_left(numbers, 7)
print(index)  # Output: 3

# Insert 7 at the found index
bisect.insort_left(numbers, 7)
print(numbers)  # Output: [2, 4, 6, 7, 8, 10]