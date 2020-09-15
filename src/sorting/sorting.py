# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0

    # Your code here
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    
    if i < len(arrA):
        merged_arr.extend(arrA[i:])
    elif j < len(arrB):
        merged_arr.extend(arrB[j:])

    # while loop breaks once either list breaks so if it does and anything left on either list, append all of it to merged_arr

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    mid = len(arr) // 2
    r = arr[:mid]
    l = arr[mid:]

    if len(l) < 2 and len(r) < 2:
        return merge(l, r)
    else:
        return merge(merge_sort(l), merge_sort(r))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

