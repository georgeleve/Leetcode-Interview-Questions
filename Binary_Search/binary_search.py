class Solution(object):
    #returns the index of the array nums that we found the target if the target exists, else returns -1
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = left + ((right - left) // 2) #do this to avoid overflow if the sum of the integers right+left is bigger than 2^31
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #the array must be sorted before starting a binary search
target = 2
a = Solution()
print(a.binarySearch(nums, target))