"""   Module implementing Merge Sort   """
import rand


def merge_sort(arr):
    """   Function implementing Merge Sort   """
    # Hello
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(
        merge_sort(arr[0:half]), merge_sort(arr[half:len(arr)]))


def recombine(left_arr, right_arr):
    """   Function combining 2 arrays   """
    left_index = 0
    right_index = 0
    count = 0
    merge_arr = [None] * \
        (len(left_arr) + len(right_arr))
    while left_index < len(
            left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[count] = left_arr[left_index]
            left_index += 1
            count = count + 1
        else:
            merge_arr[left_index +
                      right_index] = right_arr[right_index]
            right_index += 1
            count = count + 1

    for i in range(right_index, len(right_arr)):
        merge_arr[count] = right_arr[i]
        count = count + 1

    for i in range(left_index, len(left_arr)):
        merge_arr[count] = left_arr[i]
        count = count + 1
    return merge_arr


inputval = rand.random_array([None] * 20)
print(inputval)
outputval = merge_sort(inputval)

print(outputval)
