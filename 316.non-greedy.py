#316. Remove Duplicate Letters
"""
Given "bcabc"
Return "abc"

Given "cbcacdcbc"
Return "acdb"

"thesqtitxyetpxloeevdeqifkz"

"hesitxyplovdqfkz"
"hesqitxyplovdfkz"

find the smallest letter and try to move it to the head
once it reaches the head, find the second smalled letter and move it to next to head
repeat
"""
class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = {}        
        print("s: ", s)

        if s== None or len(s) <= 1:
            return s

        tmp = sorted(set(s))
        head = tmp[0]
        # use head as Anchor, 
        headLeft = s[:s.find(head)]                    #find left-most index of head
        headRight = s[s.find(head)+1:].replace(head, '') #remove the rest Anchor
        print(headLeft, head, headRight)
        #eliminating all duplicates to expose the Anchor
        #for ch in sorted(set(headRight), reverse=True):
        for ch in tmp[1:]:
            if headLeft < headLeft.replace(ch, ''):
                headRight =headRight.replace(ch, '')
            else:
                headLeft = headLeft.replace(ch, '')

        print("2", headLeft, head, headRight)
        #end up with a "" or max-lexi string on the left side, 
        #repeat on the left part, then right part
        
        re = self.removeDuplicateLetters(headLeft) + head + self.removeDuplicateLetters(headRight)
        print("min-str:%s" % re)
        return re

#print("result: " , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
print("result: " , Solution().removeDuplicateLetters("bcabc"))