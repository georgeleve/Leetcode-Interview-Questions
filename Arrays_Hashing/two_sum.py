# https://leetcode.com/problems/two-sum/

class Solution(object):
    def __init__(self) -> None:
        pass

    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(0, len(nums)):
            if target-nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            hashmap[nums[i]] = i
        return False

nums = [3,2,4]
target = 6
s = Solution()
print(s.twoSum(nums, target))