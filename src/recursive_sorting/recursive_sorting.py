tough = [0, 1, 2, 4, 4, 5, 7, 8, 9, 11, 26, 33, 77, 88]
quick = [0, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 6, 7, 7]
crystal_pepsi = [4, 9, 2, 0, 5, 8, 11, 33, 4, 77, 1, 88, 26, 7]

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    l=0
    r=0
    k=0

    while l < len(arrA) and r < len(arrB):
        if arrA[l] < arrB[r]:
            merged_arr[k] = arrA[l]
            l += 1
        else:
            merged_arr[k] = arrB[r]
            r += 1
        k += 1
    while l < len(arrA):
        merged_arr[k] = arrA[l]
        l += 1
        k += 1
    while r < len(arrB):
        merged_arr[k] = arrB[r]
        r += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) > 1:

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        l=0
        r=0
        k=0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[k] = left[l]
                l += 1

            else:
                arr[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1

    return arr

print(merge_sort(crystal_pepsi))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO



    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
