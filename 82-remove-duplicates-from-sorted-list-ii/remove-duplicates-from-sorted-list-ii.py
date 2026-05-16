class Solution:
    def deleteDuplicates(self, head):
        from collections import Counter
        vals, curr = [], head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        
        for v in Counter(vals):
            if Counter(vals)[v] == 1:
                curr.next = ListNode(v)
                curr = curr.next

        return dummy.next