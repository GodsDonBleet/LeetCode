class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            # Swap
            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

sol = Solution()
swapped_head = sol.swapPairs(head)

printList(swapped_head)

'''
1 2 3 4

first.next = second.next

first.next (node 1’s next) now points to node 3 (skipping node 2).
Result: 1 -> 3 -> 4

second.next = first

second.next (node 2’s next) points back to node 1, reversing the pair.
Result: 2 -> 1 -> 3 -> 4

current.next = second

current.next (dummy’s next) points to node 2, completing the swap.
Result: dummy -> 2 -> 1 -> 3 -> 4

current = first

Move current pointer to node 1 (which is now the second node in the swapped pair).

'''