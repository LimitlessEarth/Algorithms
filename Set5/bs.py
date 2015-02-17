class BinarySearch:
        NOT_FOUND = -1
 
        def binarySearch(self, arr, searchValue, left, right):
                if right < left:
                        return self.NOT_FOUND
 
                mid = (left + right) / 2
                if searchValue > arr[mid]:
                        return self.binarySearch(arr, searchValue, mid + 1, right)
                elif searchValue < arr[mid]:
                        return self.binarySearch(arr, searchValue, left, mid - 1)
                else:
                        return mid
 
        def search(self, arr, searchValue):
                left = 0
                right = len(arr) - 1
                return self.binarySearch(arr, searchValue, left, right)
 
if __name__ == '__main__':
        bs = BinarySearch()
        a = [1, 2, 3, 5, 9, 11, 15, 66]
        print bs.search(a, 5)
