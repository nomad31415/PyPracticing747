from typing import Optional





class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next




class Solution:

	def splitPairs(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
		

		p =  head
		n = 0

		while p:
			n+=1
			p = p.next
		print(n)	
			


        






if __name__ == '__main__':

	
	
	l1 = ListNode(1)
	l2 = ListNode(2)
	l3 = ListNode(3)

	l1.next = l2
	l2.next = l3


	s = Solution()
	s.splitPairs(l1, 5)
