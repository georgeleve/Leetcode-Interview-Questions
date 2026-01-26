# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(max(n,m)) Time Complexity, where n is number of elements in l1
# and m the number of elements in l2
# O(1) Space Complexity: the lenght of the new list is at most max(m,n)+1
# but we ddon't count the anser as part of the space complexity
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tmp = dummy
        curSum, carry = 0, 0

        while l1 or l2:
            if l1:
                curSum += l1.val
            if l2:
                curSum += l2.val

            if (curSum + carry) < 10:
                newNode = ListNode(curSum+carry) #put single digit
                carry = 0
            else:
                newNode = ListNode((curSum+carry)%10) #e.g. from 14 we keep the 4
                carry = 1 # sum+carry always <= 19 <= (9+9+1) so we don't have to do (sum+carry)//10 

            tmp.next = newNode
            tmp = tmp.next
            curSum = 0 #resetting for the next digit

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Add the last node if carry is 1
        if carry == 1:
            newNode = ListNode(1)
            tmp.next = newNode

        return dummy.next

if __name__ == "__main__":
    # Example usage:
	# Creating first number: 342 (represented as 2 -> 4 -> 3)
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	
	# Creating second number: 465 (represented as 5 -> 6 -> 4)
	l2 = ListNode(5, ListNode(6, ListNode(4)))
	
	solution = Solution()
	result = solution.addTwoNumbers(l1, l2)
	
	# Printing the result: should represent 807 (7 -> 0 -> 8)
	while result:
		print(result.val, end=" -> " if result.next else "")
		result = result.next
	print("")