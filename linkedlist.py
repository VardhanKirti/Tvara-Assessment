/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null ||head.next==null){
            return null;
        }
        ListNode one=head;
        ListNode two=head;
        Boolean hasCycle=false;

         //detect if cycle exist
        while(two!=null && two.next!=null){
            one=one.next;
            two=two.next.next;

            if(one==two){   //cycle found
                hasCycle=true;
                break;
            }
        }
        //not cycle
        if(!hasCycle){
            return null;
        }
        //entry point of cycle
        one=head;
        while(one!=two){
            one=one.next;
            two=two.next;
        }
        return one;
    }
}