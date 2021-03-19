# iterative implementation of binary search in Python
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1
 
# Test array
arr = [2, 3, 4, 10, 40]
item = 10
 
# Function call
result = binary_search(arr, item)

print("Item: " + str(item))
if result != -1:
    print("Index: " + str(result))
else:
    print("Index: Not found")
print(binary_search_recursive([0, 1, 2, 3], 2))
