package go_solutions

import (
	"github.com/ChenzDNA/gtools/prints"
	"testing"
)

type LRUCache struct {
	cap  int
	size int
	m    map[int]*Node
	head *Node
	tail *Node
}

type Node struct {
	val  int
	key  int
	next *Node
	prev *Node
}

func Constructor146(capacity int) LRUCache {
	n := Node{}
	return LRUCache{cap: capacity, m: map[int]*Node{}, head: &n, tail: &n}
}

func (this *LRUCache) Get(key int) int {
	// fmt.Println("get",key)
	node, ok := this.m[key]
	if !ok {
		return -1
	}
	if node == this.tail {
		return node.val
	}
	node.prev.next = node.next
	node.next.prev = node.prev
	node.prev = this.tail
	this.tail.next = node
	this.tail = node
	return node.val
}

func (this *LRUCache) Put(key int, value int) {
	// fmt.Println("put",key,value)
	if this.Get(key) != -1 {
		this.m[key].val = value
		return
	}
	if this.size == this.cap {
		delete(this.m, this.head.next.key)
		this.head = this.head.next
		this.head.prev = nil
	} else {
		this.size += 1
	}
	newn := newNode(key, value)
	this.tail.next = newn
	newn.prev = this.tail
	this.tail = newn
	this.m[key] = newn
}

func newNode(key, val int) *Node {
	return &Node{key: key, val: val}
}

func Test146(t *testing.T) {
	cache := Constructor146(2)
	cache.Put(1, 1)
	cache.Put(2, 2)
	prints.ExpPrintln(
		cache.Get(1),
	)
	cache.Put(3, 3)
	prints.ExpPrintln(cache.Get(2))
	cache.Put(4, 4)
	prints.ExpPrintln(
		cache.Get(1),
		cache.Get(3),
		cache.Get(4),
	)
}
