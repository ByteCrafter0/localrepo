nums = [1, 2, 3, 4, 5]

# Nested loops example
for i in range(len(nums)):
    for j in range(i , len(nums)):
        if nums[i] == nums[j]:
            print("Duplicate found!")  # O(n^2)
        else :
            print("no data found")
            break