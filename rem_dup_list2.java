class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;
        while (curr != null) {
            boolean isDup = false;
            while (curr.next != null && curr.val == curr.next.val) {
                isDup = true;
                curr = curr.next;
            }
            if (isDup) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }
        return dummy.next;
    }
}
