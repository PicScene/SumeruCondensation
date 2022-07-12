package go_solutions

import (
	"github.com/ChenzDNA/gtools/prints"
	"testing"
)

type MagicDictionary struct {
	Lens  [101]int
	Words map[int][]string
}

func Constructor() MagicDictionary {
	return MagicDictionary{Lens: [101]int{}, Words: map[int][]string{}}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	lenn := len(dictionary)
	for i := 0; i < lenn; i++ {
		l := len(dictionary[i])
		this.Lens[l] += 1
		this.Words[l] = append(this.Words[l], dictionary[i])
	}
}

func (this *MagicDictionary) Search(searchWord string) bool {
	l := len(searchWord)
	if this.Lens[l] == 0 {
		return false
	}
	t := this.Words[l]
	for i := 0; i < this.Lens[l]; i++ {
		lenss := len(t[i])
		diff := 0
		for j := 0; j < lenss; j++ {
			if t[i][j] != searchWord[j] {
				diff += 1
			}
		}
		if diff == 1 {
			return true
		}
	}
	return false
}

func Test676(t *testing.T) {
	md := Constructor()
	md.BuildDict([]string{"hello", "leetcode"})
	prints.ExpPrintln(
		md.Search("hello"),
		md.Search("hhllo"),
		md.Search("hell"),
		md.Search("leetcoded"),
	)
}
