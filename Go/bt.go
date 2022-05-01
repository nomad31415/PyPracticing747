package main

import (
	"fmt"
	"io"
	"os"
)

type Node struct {
	data  int64
	left  *Node
	right *Node
}

type Tree struct {
	root *Node
}

func (t *Tree) insert(d int64) *Tree {

	if t.root == nil {
		t.root = &Node{data: d, left: nil, right: nil}
	} else {

		t.root.insert(d)
	}
	return t

}

func (n *Node) insert(d int64) {
	if n == nil {
		return

	} else if d < n.data {

		if n.left == nil {
			n.left = &Node{data: d, left: nil, right: nil}
		} else {
			n.left.insert(d)
		}

	} else {

		if n.right == nil {
			n.right = &Node{data: d, left: nil, right: nil}
		} else {
			n.right.insert(d)
		}
	}

}

func print(w io.Writer, node *Node, ns int, ch rune) {
	if node == nil {
		return
	}

	for i := 0; i < ns; i++ {
		fmt.Fprint(w, " ")
	}
	fmt.Fprintf(w, "%c:%v\n", ch, node.data)
	print(w, node.left, ns+2, 'L')
	print(w, node.right, ns+2, 'R')
}

func main() {

	tree := &Tree{}
	tree.insert(100).
		insert(-20).
		insert(-50).
		insert(-15).
		insert(-60).
		insert(50).
		insert(60).
		insert(55).
		insert(85).
		insert(15).
		insert(5).
		insert(-10)
	print(os.Stdout, tree.root, 0, 'M')
}
