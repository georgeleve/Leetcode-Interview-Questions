'''  
Final Comparison for Interview Readiness - Top K Frequent Elements
1. Sorting: O(N log N) Time, O(N) Space. Simple but not optimal.
2. Max-Heap: O(N + K log N) Time, O(N) Space.
3. Min-Heap: O(N log K) Time, O(N + K) Space. Preferred for scalability and distributed data. 
4. Bucket Sort: O(N) Time, O(N) Space. Fastest for single-machine data.
5. Quickselect: O(N) Average Time, O(N) Space. Distributed Scenario: Use Min-Heap so each server can compute a local Top-K before merging.
'''

'''
Αν τα δεδομένα σου είναι streaming (ρέουν συνεχώς), το Bucket Sort είναι άχρηστο, ενώ το Min-Heap είναι σωτήριο.

Αν έχεις περιορισμένη μνήμη αλλά γρήγορη CPU, το Quickselect είναι το εργαλείο σου.
Αναλύοντας όλες τις λύσεις, μαθαίνεις να επιλέγεις το σωστό εργαλείο για τη σωστή δουλειά.
'''

'''
1st solution
Create a hashmap with the frequency that eveery numbere appeears and then sort it 
based on frequency and return the k keys with the highest values
O(nlogn) time complexity | O(n) space complexity, where n is the number of elements in the input array.
'''

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Create a frequency map (Counter)
        # Time: O(N) - We visit every element in nums once.
        # Space: O(U) - To store unique elements and their counts.
        counter = Counter(nums)  
        
        # 2. Extract keys into a list
        # Time: O(U) - We iterate through the unique keys of the counter.
        # Space: O(U) - To create the new list of unique elements.
        unique_elements = list(counter.keys())
        
        # 3. Sort the unique elements (based on the frequency from the counter)
        # Time: O(U log U) - Python's Timsort on U elements.
        # Note: Each comparison calls `counter[x]`, which is O(1) on average.
        # Space: O(U) - Timsort requires O(U) extra space in the worst case.
        unique_elements.sort(key=lambda x: counter[x], reverse=True)
        
        # 4. Slice the first k elements
        # Time: O(k) - Creating a new list of size k.
        # Space: O(k) - To store the output list.
        return unique_elements[:k]


'''
# 2nd solution
        #create the hashmap  O(n) time complexity      O(n) space complexity
        #1->4  
        #2->4
        #3->2
         
        # O(N log N) time complexity   O(N) space complexity
        # put all of the values of the hashmap in the maxheap (key=number of times a number appears, value=number) 

        # pop k times to get the top k most frequent elements and put elements in the output array
        # O(K log N) Time Complexity

        #Total O(N log N) Time Complexity | O(N) space complexity

        If we make the heap using heapq.heapify(list_of_all_elements) the time compelxity is O(N)
        and so the total time compexity will become O(N + K*log(N))
'''


'''
BEST SOLUTION
3rd solution | O(N log K) Time Compexity where N >= K | O (N + K) Space Complexity for hashmap and the heap
Where N is the number of elements in the input array and K is the input number k

create a hashmap with the frerquencies, then create a min heap and push only k elements.
for the rest of the elements if the root frequency (which is the min frequency) element < current element 
then pop it and replace it with the current element
After we do this with all of the elements pop until the heap is empty and return the output array
'''
import heapq
from typing import List
from collections import Counter

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKElements = []

        # Create a hashmap to count the number of times a number appears (frequencies)
        # O(N) time complexity | O(N) space complexity, where N is number of elements in the array
        # we can also use this: counter = Counter(nums)
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # We create a minHeap and we only add k elements
        # O(k log(k)) Time Complexity | O(k) space complexity
        # If heap size is > k , we check if the frequency (that a number appears)
        # is bigger than the minFrequency of the root of the heap (We access the root with O(1) Time Complexity).
        # If yes, we pop the root and add the current (number, frequency)
        # so the heap always maintains size = k
        # O(n log k) * 2 = O(n log k) Time Comlexity | O(K) Space Complexity since heap size = K
        # Use the min-heap to keep the K most frequent elements O(N log K)
        minHeap = []
        for num, freq in counter.items():
            if len(minHeap) < k:
                # we put (freq, num) so we sort the heap based on the frequency
                heapq.heappush(minHeap, (freq, num)) # O(log K)
            else:
                # if the current freq is bigger than the smallest of the heap (which is in the root of the min-heap)
                if minHeap and freq > minHeap[0][0]: #O(1)
                    heapq.heapreplace(minHeap, (freq, num)) # O(log K)
                    #heapq.heappop(minHeap) # O(log K)
                    #heapq.heappush(minHeap, (freq, num)) # O(log K)
        
        # pop from the heap of size = k (O(K log K) Time) | O(K) Space
        # and add the values in the output array | O(K) Time | O(K) Space
        # and the elements will appear sorted in the output array.
        while minHeap:
            freq, num = heapq.heappop(minHeap) #O(log K)
            topKElements.append(num) #O(1)
        return topKElements

        #The extraction of elements using a while loop with heappop takes O(K log K) time.
        # However, since the problem allows any order in the output, I can simply iterate over
        # the heap array in O(K) time to optimize the final step
        # We can also do this instead: return [item[1] for item in minHeap] in O(K) Time and O(K) Space
        # but the elements will be unsorted in the output array

if  __name__ == "__main__":
    topKFrequent = Solution2().topKFrequent([1,1,1,2,2,3], 2)
print(topKFrequent)  #Output: [1,2]

'''
BEST SOLUTION
# 4rth Solution (Only efficient when N (array size) fits comfortably in memory.
Not ideal for distributed large-scale data where N is massive).
Bucket Sort | O(N) Time Complexity | O(N) Space Complexity
Create an array where index is the frequency and value is a list of numbers that appear in that frequency
'''
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKElements = []

        counter = Counter(nums)

        bucket = [[] for i in range(0, len(nums)+1)]

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket)-1, 0, -1):
            currentList = bucket[i]
            for num in currentList:
                topKElements.append(num)
                if len(topKElements) == k:
                    return topKElements

        return topKElements
'''


'''
5fth solution - Quickselect - Time Complexity O(n) | Space Complexity O(n) where n is the number of elements in the input array.
Time Complexity: Average O(N), where N is the number of unique elements.
Building the map is O(M) where M is total input size.
Space Comlexity: O(N) to store the frequencies and the unique elements array.

Time: O(N) average, O(N^2) worst-case
Space: O(N) (for map) + O(1) extra (in-place)
'''

'''
import collections
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1. Move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 2. Move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            return store_index

        def select(left, right, k_smallest):
            if left == right: return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                select(left, pivot_index - 1, k_smallest)
            else:
                select(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # We want the (n - k)th most frequent element to partition the top k
        select(0, n - 1, n - k)
        return unique[n - k:]
'''

'''
Μια τελευταία πινελιά για την "Distributed" ερώτηση: Αν ποτέ σε ρωτήσουν στην Oracle: 
"Ποια λύση θα διάλεγες αν τα nums ήταν 100 Terabytes μοιρασμένα σε 100 servers;"
Η απάντηση: Θα διάλεγες τη Λύση 3 (Min-Heap).Γιατί: Κάθε server μπορεί να υπολογίσει το δικό του
 "τοπικό" Top-K ανεξάρτητα. Μετά, στέλνεις μόνο K στοιχεία από κάθε server σε έναν κεντρικό (Master Node). 
 Ο κεντρικός node θα έχει να διαχειριστεί μόνο 100 times K στοιχεία αντί για όλο το N.Σύγκριση: Το Bucket Sort (Λύση 4) θα αποτύγχανε παταγωδώς γιατί κανένας server δεν θα είχε ολόκληρη την εικόνα των συχνοτήτων (global frequency counts).
'''