# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or head.next is None:
            return

        first_half = head
        second_half = None

        half = head
        fast = head

        while fast:
            # increment half by one, fast by two
            before_half = half
            half = half.next
            fast = fast.next
            if fast:
                fast = fast.next

        # cut the two halfs of the linked list in half
        before_half.next = None

        # reverse the second half
        prev = None
        curr = half
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second_half = prev

        # stitch the two lists together:


        while first_half:
            temp = first_half.next

            first_half.next = second_half
            if second_half:
                second_half = second_half.next
                first_half.next.next = temp
                first_half = first_half.next.next
            else:
                first_half = first_half.next




        