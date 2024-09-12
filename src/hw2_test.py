from hw2_debugging import merge_sort

def testsort1():
    # checking with 1 different element in an unsorted array
    to_sort = [1000, 1000, 1000, 1000, 1000, 100, 1000]
    expected_sort=[100, 1000, 1000, 1000, 1000, 1000, 1000]
    assert merge_sort(to_sort)==expected_sort

def testsort2():
    # checking with null array
    to_sort2=[]
    expected_sort2=[]
    assert merge_sort(to_sort2)==expected_sort2
    
def testsort3():
    # checking with a reverse sorted array
    to_sort3=[9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_sort3=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort(to_sort3)==expected_sort3
