class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data


class llist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)




if __name__ == "__main__":
    f =  llist()
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")

    f.head = n1
    n1.next = n2
    n2.next = n3



    print(f)
