# Insertion sort algorithm in decreasing order
def decreasing_insertion_sort(arr):
    # Traverse through the array size
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Compare the key with the previous elements
        while i >= 0 and key > arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        # Insert the key at the correct position
        arr[i + 1] = key
    return arr

# Path: main.py
if __name__ == "__main__":
    arr = [17, 14, 18, 4, 8]
    print("The original array is: ", arr)
    print("The sorted arrat in monotonically decreasing order is: ",decreasing_insertion_sort(arr))