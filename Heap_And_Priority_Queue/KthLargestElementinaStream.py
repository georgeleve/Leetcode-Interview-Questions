'''
I chose a Min-Heap of size K to maintain the K largest elements seen so far. The root of the heap (at index 0) always represents the K-th largest element. This approach is optimal for streaming data because each new score is processed in logarithmic time $O(\log K)$, and we only store at most K elements at any given time after initialization.

Algorithm
Initialization
Insert all initial numbers into a min-heap.
If the heap size becomes greater than k, repeatedly remove the smallest element.
After this, the heap contains exactly k elements.
add(value)
Insert the new value into the min-heap.
If heap size > k:
Remove the smallest element (the heap root).
Return the heap's smallest element (the root), which is now the k-th largest.
'''

class KthLargest:
    # O(n) + O(n-k * logn) = O((n-k) * logn) Time Complexity | O(n) space compelxity
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        #make a min heap of size k and remove the extra elements
        self.minHeap = nums
        heapq.heapify(self.minHeap) #O(n) time | O(n) space - convert the list into a heap (in place)
        while len(self.minHeap) > self.k: # O(n-k * logn)
            heapq.heappop(self.minHeap)
    
    #Time complexity: O(m∗logk)
    # Space complexity: O(k)
    # Where m is the number of calls made to add().
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #O(logk)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #O(logk)
        return self.minHeap[0]  #O(1)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)