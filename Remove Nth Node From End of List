/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy_head = new ListNode(0); // create dummy node head
        dummy_head.next = head;
        
        ListNode slow = dummy_head, fast = dummy_head;
        
        for(int i = 0; i <= n; i++)
            fast = fast.next;
        
        while(fast != null){
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next; // delete node
        return dummy_head.next; // return head of the list
    }
}
