# https://leetcode.com/problems/k-closest-points-to-origin/submissions/1872609786/
# 973. K Closest Points to Origin

#https://neetcode.io/solutions/k-closest-points-to-origin

'''
maxheap (use a min heap and put the elements with a minus "-" because python only has a minheap)
Time Complexity O(n*logk) where n is the number of points and k is the input k
Space Complexity O(k) for the k elements in the heap
"I'll go with the Max-Heap approach maintaining a size of k. Even though heapify on a Min-Heap is $O(N)$,
the Max-Heap only uses $O(k)$ space, which is much more efficient for large-scale or streaming data.
I'll use negative distances to implement the Max-Heap logic since Python's heapq is a Min-Heap by default.
'''
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        kClosestPointsToOrigin = []

        for point in points: # O(n) time
            x1, y1 = point
            distance = -(x1**2 + y1**2)  # put minus "-" because its a max heap

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (distance, point)) # sort based on distance so put distance first - O(logk) time
            else:
                # if current distance is smaller (distance is bigger because of the minus) from the root of the heap
                if distance > maxHeap[0][0]:
                    heapq.heapreplace(maxHeap, (distance, point)) #O(logk) time

        # We return only the points 
        # O(k) time | O(k) space
        return [item[1] for item in maxHeap]

        #Another way to do it
        #while maxHeap:
        #    distance, point = heapq.heappop(maxHeap) #O(logk) time
        #    kClosestPointsToOrigin.append(point) #O(1) time
        #return kClosestPointsToOrigin

# If N and K were significantly larger and we had all the data in memory,
# I could optimize this to O(N) average time using Quickselect

#if "__name__" == "__main__":

'''
Quickselect Approach:
- Time Complexity: Average O(N), Worst-case O(N^2).
- Space Complexity: O(1) if we partition in-place, or O(N) for recursive stack.

Pros vs Cons:
1. Efficiency: Theoretically faster than Heap for very large N (O(N) vs O(N log K)).
2. Memory: More memory-efficient as it doesn't require a separate heap structure.
3. Stability: Risk of O(N^2) worst-case if the pivot selection is poor (though 
   randomized pivot mitigates this).
4. Practicality: In interviews, Heap is usually preferred because it's more 
   robust, handles streaming data (online processing), and is less prone to 
   implementation bugs (off-by-one errors) compared to Quickselect.

Note: For the given constraints (N = 10^4), the O(N log K) Heap approach is 
perfectly optimal and more reliable.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res