# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
    # base case
    if end >= start:

        # set the mid point
        mid = (start + end) // 2

        # if the target is the mid point
        if arr[mid] == target:
            return mid

        # if target is smaller than mid, it has to be to the left subarray of the mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        
        # else target is in the right subarray of the mid
        else:
            return binary_search(arr, target, mid + 1, end)
    
    # or the target is not in the array
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


