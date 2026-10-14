class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        for num1 in arr1:
            if self.binary_search(arr2, num1, d):
                count += 1
        return count
    
    def binary_search(self, arr, target, d):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if abs(arr[mid] - target) <= d:
                return False
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return True