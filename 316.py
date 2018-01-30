#316. Remove Duplicate Letters
"""
Given "bcabc"
Return "abc"

Given "cbcacdcbc"
Return "acdb"


find the smallest letter and try to move it to the head
"""
class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = {}        
        print("s: ", s)

        for i, ch in enumerate(s):
            if ch not in idx:
                idx[ch] = i
            oldIdx = idx[ch]
            oldLexOrder = ''.join([ ch for idx,ch in sorted((y,x) for x,y in idx.items()) ])
            idx[ch] = i
            newLexOrder = ''.join([ ch for idx,ch in sorted((y,x) for x,y in idx.items()) ])
            
            print( "old: ", oldLexOrder , "  new: ", newLexOrder)

            if oldLexOrder > newLexOrder:
                greedyLeft = self.removeDuplicateLetters( oldLexOrder + s[i+1:])
                greedyRight = self.removeDuplicateLetters( newLexOrder + s[i+1:])
                print( "greedyLeft: ", greedyLeft , "  greedyRight: ", greedyRight)
                if greedyLeft < greedyRight:
                    print("revert to ", oldLexOrder)
                    idx[ch] = oldIdx  #revert


        print("min-str:%s" % ''.join([ ch for key,ch in sorted((y,x) for x,y in idx.items())]) )
        return ''.join([ ch for key,ch in sorted((y,x) for x,y in idx.items())])

print("result: " , Solution().removeDuplicateLetters("bcabc"))