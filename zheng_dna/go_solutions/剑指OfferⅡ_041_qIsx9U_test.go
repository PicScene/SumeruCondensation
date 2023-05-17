package go_solutions

import (
	"github.com/ChenzDNA/gtools/prints"
	"testing"
)

type MovingAverage struct {
	Nums []int
	L    int
	Sum  int
}

/** Initialize your data structure here. */
func ConstructorOffer041(size int) MovingAverage {
	return MovingAverage{Nums: make([]int, size)}
}

func (this *MovingAverage) Next(val int) float64 {
	lenn := len(this.Nums)
	this.Sum += val - this.Nums[this.L%lenn]
	this.Nums[this.L%lenn] = val
	this.L += 1
	if !(this.L < lenn) {
		return float64(this.Sum) / float64(lenn)
	}
	return float64(this.Sum) / float64(this.L)
}

func TestOffer041(t *testing.T) {
	obj := ConstructorOffer041(3)
	prints.ExpPrintln(
		obj.Next(1),
		obj.Next(10),
		obj.Next(3),
		obj.Next(5),
	)
}
