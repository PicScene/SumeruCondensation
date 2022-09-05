'''
Author: 七画一只妖
Date: 2022-04-21 18:16:20
LastEditors: 七画一只妖
LastEditTime: 2022-04-21 18:18:07
Description: file content
'''
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        ans = ''
        for i in range(len(words)):
            word = words[i]
            head = word[0]
            if head.lower() in ['a', 'e', 'i', 'o', 'u']:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            tail = 'a' * (i + 1) 
            word += tail
            ans += word + ' '
        
        return ans.strip()


a = Solution
print(a.toGoatLatin(a,"I speak Goat Latin"))