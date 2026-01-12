"""
Reverse a Linked List: Given the head of a singly linked list, reverse the list and return the new head.
"""

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedList:
    def __init__(self, head=None):
        self.head = head

    def reverse_list(self):
        prev = None
        curr = self.head

        while curr:
            next_element = curr.next
            curr.next = prev
            prev = curr
            curr = next_element

        return prev  # Returns the new head


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_standard(self):
        # 1. Setup: Create 1 -> 2 -> 3 manually
        node3 = ListNode(3)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)  # Head

        # 2. Execute
        solver = ReverseLinkedList(node1)
        new_head = solver.reverse_list()

        # 3. Assert (Check Node by Node)
        # Expected: 3 -> 2 -> 1
        self.assertEqual(new_head.val, 3)  # Check first value
        self.assertEqual(new_head.next.val, 2)  # Check second value
        self.assertEqual(new_head.next.next.val, 1)  # Check third value
        self.assertIsNone(new_head.next.next.next)  # Ensure tail is None

    def test_empty(self):
        solver = ReverseLinkedList(None)
        new_head = solver.reverse_list()
        self.assertIsNone(new_head)


if __name__ == "__main__":
    unittest.main()
