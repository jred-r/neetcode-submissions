class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {
        // 1. Return type must accept null (e.g., if the list becomes empty)
        const dummy: ListNode = new ListNode(0, head);
        let left: ListNode = dummy;
        let right: ListNode | null = head;

        // Move right pointer n steps ahead
        while (n > 0 && right) {
            right = right.next;
            n -= 1;
        }

        // Move both pointers until right reaches the end
        while (right) {
            left = left.next!; // Use ! because left.next is guaranteed to exist here
            right = right.next;
        }

        // 2. Fix the deletion logic: skip the target node by mutating its 'next' reference
        if (left.next) {
            left.next = left.next.next;
        }

        return dummy.next;
    }
}
