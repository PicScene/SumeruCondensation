package go_solutions

import (
	"github.com/ChenzDNA/gtools/prints"
	"math"
	"testing"
)

type MinStack struct {
	mins []int
	l    []int
}

func Constructor155() MinStack {
	return MinStack{l: make([]int, 0), mins: []int{math.MaxInt32}}
}

func (this *MinStack) Push(val int) {
	if !(val > this.mins[len(this.mins)-1]) {
		this.mins = append(this.mins, val)
	}
	this.l = append(this.l, val)
}

func (this *MinStack) Pop() {
	last := len(this.l) - 1
	minslast := len(this.mins) - 1
	if this.l[last] == this.mins[minslast] {
		this.mins = this.mins[:minslast]
	}
	this.l = this.l[:last]
}

func (this *MinStack) Top() int {
	return this.l[len(this.l)-1]
}

func (this *MinStack) GetMin() int {
	return this.mins[len(this.mins)-1]
}

func Test155(t *testing.T) {
	ms := Constructor155()
	ms.Push(-2)
	ms.Push(0)
	ms.Push(-3)
	prints.ExpPrintln(ms.GetMin())
	ms.Pop()
	prints.ExpPrintln(ms.Top(), ms.GetMin())

}
