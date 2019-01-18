import unittest

def partition(a,start,end):
    # pivot to the end, simplest variant
    pivot = a[end]
    # left part of array: all < pivot
    left_end = start
    # right part of array: all >= pivot
    right_start = end
    while left_end < right_start:
        if a[left_end] < pivot:
            left_end += 1
        else:
            right_start -= 1
            a[left_end], a[right_start] = a[right_start], a[left_end]
    # left_end and right_start now point both to first element of the right
    # array, which will be the pivot position:
    a[end], a[right_start] = a[right_start], a[end]
    return right_start


def quicksort_i(a,start,end):
    print("sorting: "+str(start)+" to: "+str(end))
    print(str(a))
    if (end-start) > 0:
        pivot_index = partition(a,start,end)
        print(pivot_index)
        quicksort_i(a,start,pivot_index-1)
        quicksort_i(a,pivot_index+1,end)
    return a

def quicksort(a):
    return quicksort_i(a,0,len(a)-1)

class TestQuicksort(unittest.TestCase):

    def test_empty(self):
        a = []
        self.assertEqual([],quicksort(a))
    def test_one(self):
        a = [1]
        self.assertEqual([1],quicksort(a))
    def test_two(self):
        a = [4,2]
        self.assertEqual([2,4],quicksort(a))
    def test_two_sorted(self):
        a = [4,2]
        self.assertEqual([2,4],quicksort(a))
    def test_few(self):
        a = [4,2,6]
        self.assertEqual([2,4,6],quicksort(a))
    def test_more(self):
        a = [9,3,6,4,2,7,5,8,1]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9],quicksort(a))
    def test_sorted(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9],quicksort(a))
    def test_more_doubles(self):
        a = [9,3,6,4,3,7,3,7,3]
        self.assertEqual([3, 3, 3, 3, 4, 6, 7, 7, 9],quicksort(a))

if __name__ == '__main__':
    unittest.main()
