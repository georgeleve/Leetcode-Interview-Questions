# https://www.youtube.com/watch?v=XEmy13g1Qxc

import heapq
from typing import List

#Time O(nlogk) | Space O(k), wherre n is the length of the array nums.
# we keep a minheap of size k and then we return the root which is the smallest of the elements in the heap of size k.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [3,2,1,5,6,4]  k=2         output=5
        # 1st: sort array using timsort, return nums[len(nums)-k]  O(nlogn) average time, O(n) best case,
        # for the mergin O(n) space)

        # 2nd: maxheap: put all elements in heap using heapify O(n) time and then pop k times O(k log n)
        #and return the kth+1 pop
        # Time complexity O(n + k*logn) | Space O(n)

        # 3rd: minheap     return heapq.nlargest(k, nums)[-1]    
        # Time Complexity O(n*logk) where n is the nums of elements in the input list | Space Complexity O(k) 
        minHeap = []
        
        for num in nums:
            # for every element put it in a minheap
            heapq.heappush(minHeap, num)
            # if len(minHeap) > k: pop from the minheap (keep always a heap of size k)
            if len(minHeap) > k:
                heapq.heappop(minHeap) #pop the smallest element, which is the root.
        
        # return the smallest element of the minHeap of size k which is the kth largest element
        return minHeap[0]

        # 4rth solution
        # solve it using quickselect for O(n) average time complexity
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)