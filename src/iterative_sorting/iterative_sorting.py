

crystal_pepsi = [4, 9, 2, 0, 5, 8, 11, 33, 4, 77, 1, 88, 26, 7]
bbq = [2, 3, 6, 2, 1, 4, 2, 5, 2, 7, 7, 2, 0, 1, 6]
pick_me = [4, 9, 2, 0, 1, 4, 2, 5, 2, 7, 7, 5, 8, 11, 33, 2, 0, 5, 8, 11, 33, 4, 4, 77, 1, 88, 26, 7]


# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)): # Maybe remove -1
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

print(selection_sort(pick_me))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_happened = True
    while swap_happened == True:
        swap_happened = False
        for bubba in range(0, len(arr) - 1):
            if arr[bubba] > arr[bubba +1]:
                swap_happened = True
                arr[bubba], arr[bubba +1] = arr[bubba +1], arr[bubba]

    return arr

print("\n °°oOo°oO°°°°oOo°oO°°°°oOo°oO°°°°oOo°oO°°\n",
    "°°oOo°oO°° Look at the pretty bubbles!!!°°oOo°oO°°\n\n",
 bubble_sort(crystal_pepsi),
  "\n\n°°oOo°oO°° Look at the pretty bubbles!!!°°oOo°oO°°\n",
  "°°oOo°oO°°°°oOo°oO°°°°oOo°oO°°°°oOo°oO°°\n\n")




# STRETCH: implement the Count Sort function below

def count_sort(arr):

    bean_counter = [0] * 200

    for bean_type in arr:
        if bean_type < 0:
            return "Error, negative numbers not allowed in Count Sort"
        bean_counter[bean_type] += 1

    for beans in range(1, len(bean_counter)):
        bean_counter[beans] += bean_counter[beans - 1]

    bean_can = [0] * len(arr)

    for ribs in range(0, len(arr)):
        bean_can[bean_counter[arr[ribs]] - 1] = arr[ribs]
        bean_counter[arr[ribs]] -= 1
    arr = bean_can
    return arr

print(count_sort(bbq))