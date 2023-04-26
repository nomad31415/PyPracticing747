class Node:
	def __init__(self, val):
		self.data = val
		self.next = None


class MyTree:
	def __init__(self):
		self.head = None



	def  ls(self):
		p = self.head
		while p:
			print(p.data)
			p = p.next
			











if __name__ == '__main__':
	
	t1 = MyTree()

	v1 = Node("A")

	t1.head = v1

	v2 = Node("B")

	v3 = Node("C")


	t1.head.next = v2


	v2.next = v3

	t1.ls()




