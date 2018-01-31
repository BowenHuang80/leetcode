
#316. Remove Duplicate Letters
"""
Given "bcabc"
Return "abc"

Given "cbcacdcbc"
Return "acdb"

Given "thesqtitxyetpxloeevdeqifkz"
Return "hesitxyplovdqfkz"

Given "ccacbaba"
Return "acb"
find the smallest letter and try to move it to the head
once it reaches the head, find the second smalled letter and move it to next to head
repeat
"""
import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = {}        
        charSet = sorted(set(s), reverse=True)
        print("start: ", s, charSet)
        for key, ch in enumerate(charSet):
            print("ch:", ch, "key:", key)

            idx = s.find(ch)
            while( -1 != idx ):
                print("idx: ", idx, s, len(s))
                if (idx < (len(s)-1) and ch < s[idx+1]): # or idx == len(s)-1:
                    s = s[:idx+1] + s[idx+1:].replace(ch,'')
                    print("remove", ch, s)
                    break
                else:
                    if -1 == s.find(ch, idx+1): #only apperance
                        #keep it, do nothing
                        print("last one ", ch, " in ", s)
                        break
                    else:
                        lexGetsBiggerPoint = -1
                        subS = ""
                        if key > 0:                            
                            for i in range(key):
                                print( "nextBiggerChar:", charSet[i])
                                lexGetsBiggerPoint = s.find( charSet[i], idx+1 )
                                if -1 != lexGetsBiggerPoint:
                                    #lexGetsBiggerPoint += idx
                                    break
                        
                        if -1 != lexGetsBiggerPoint:
                            subS = s[idx+1 : lexGetsBiggerPoint]
                            print( lexGetsBiggerPoint, "subS:", subS)

                            for predCh in set(subS):
                                print("search in left:", s[:idx])   #dont' include current char to avoid "babc"
                                if s.find( predCh, 0, idx) != -1:
                                    print("found:", predCh)
                                    subS = subS.replace( predCh, '')    #aggressive removing predCh, since it appears on the left side of current ch
                        
                            print( "aggressively reducd subS:", subS)

                        if -1 == lexGetsBiggerPoint: #remove it, since something smaller exists between ch and end
                            print( "removed a:", s[:idx], s[idx+1:])
                            s = s[:idx] + s[idx+1:] #remove it
                            idx = s.find(ch)    #find next
                        elif subS != "":
                            if ch < subS[0]:    #keep it
                                print( "keepit cc:", s[:idx+1], s[idx+1:])
                                s = s[:idx+1] + s[idx+1:].replace(ch, '') #keep it as the left-most char and fast-forward to the lex-chang point
                                idx = -1
                            else:
                                print( "removed b:", s[:idx], "right:",s[idx+1:])
                                s = s[:idx] + s[idx+1:] #remove it
                                idx = s.find(ch, idx)    #find next
                        else:
                            print( "keepit dd:", s[:idx+1], s[idx+1:])
                            s = s[:idx+1] +s[idx+1:].replace(ch, '') #keep it as the left-most char and fast-forward to the lex-chang point
                            idx = -1

        return s

print("result: ciorhsaebpunvdyktzfjlgwq" , Solution().removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
#print("result: " , Solution().removeDuplicateLetters("beeaddbeb"))
#print("result: " , Solution().removeDuplicateLetters("bcabc"))
#print("result: " , Solution().removeDuplicateLetters("cbcacdcbc"))
#print("result: " , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
#print("result: " , Solution().removeDuplicateLetters("ccacbacba"))
#print("result: " , Solution().removeDuplicateLetters("ccacbaba"))
#print("result: " , Solution().removeDuplicateLetters("baab"))
