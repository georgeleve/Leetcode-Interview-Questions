# https://www.youtube.com/watch?v=DfljaUwZsOk
# Deque always decreasing
# Use a queue  : acts like a Monotonic Queue (Monotonically Decreasing Queue)
# We remove from the left and add/remove from the right
# Example [1,1,1,1,1,4,5]   k = 6
# Time Complexity O(n) | Space Complexity O(n), where n is the number of elements in nums
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        # keep the indexes in the deque and not the values !!!
        q = deque()
        maxSlidingWindow = []
        for i in range(0, len(nums)):
            # Pop elements from the right if current element is bigger than previous elements
            # [1,1,1,1,1,4,5]   k = 6   We do not need the 1 here since   4 > 1
            # while the right most value in our deque is less than the current value that we are inserting
            while q and nums[i] > nums[q[-1]]:
                q.pop() # O(1)
            
            # add current index to the right of the deque | (add the 4)
            q.append(i)
            
            # if the element at the left of the queue is out of the window of size k
            # remove left val from window
            if q[0] + k - i == 0:
                q.popleft() # O(1)

            # if the window is of size >= k then add the max which will be the first in the deque
            if (i + 1) >= k:
                currentWindowMax = nums[q[0]] # we add the value (not the index)
                maxSlidingWindow.append(currentWindowMax)
    
        return maxSlidingWindow
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxSlidingWindow = []
        q = deque() # put the indexes and not the values
        l = r = 0
        maxSlidingWindow = []

        while r < len(nums):

            #pop smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # add current index
            q.append(r) 

            # if left is out of bounds, remove left value from the window
            # if left index > leftmost value of the queue (which is index)
            if l > q[0]:
                q.popleft()

            # our window is at least size k
            if (r + 1) >= k:
                currentWindowMax = nums[q[0]] # max is the left most position of the queue
                maxSlidingWindow.append(currentWindowMax)
                l += 1
            r += 1
        return maxSlidingWindow
            


'''
class Solution:
    # TIme Limit Exceded !!! O(k * (n-k)) Time Complexity
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        maxSlidingWindow = []
        l = 0
        r = k
        while r < len(nums)+1:
            currentWindowMax = max(nums[l:r])
            maxSlidingWindow.append(currentWindowMax)
            r += 1
            l += 1
        return maxSlidingWindow
'''