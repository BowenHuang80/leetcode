
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
<<<<<<< HEAD

                            #for predCh in set(subS):
                            #    print("search in left:", s[:idx])   #dont' include current char to avoid "babc"
                            #    if s.find( predCh, 0, idx) != -1:
                            #        s[s.find( predCh, 0, idx) : idx]
                            #        print("found:", predCh)
                            #        subS = subS.replace( predCh, '')    #aggressive removing predCh, since it appears on the left side of current ch
                            chReducable = True
                            for predChar in set(subS):
                                 predChIdx = s.rfind(predChar, 0, idx)
                                 print( "predChIdx:", predChar, predChIdx)
                                 if predChIdx == -1:
                                    chReducable = False
                                    continue
                                 #"yic" "i" "occd" "q" "io" "r" "q"
                                 # greedy reduce between  predChar .grdy..   ch subS prev[ch]
                                 tmp = [ cc for cc in charSet if cc < predChar]
                                 print( tmp )
                                 for predChar2 in tmp:
                                    
                                    predChar2Idx = s.find(predChar2, predChIdx, idx)
                                    print("find ", predChar2, " in: ", s[predChIdx : idx], "? ", predChar2Idx)
                                    if predChar2Idx == -1:  # predChar ... predChar2<predChar ...  [current char] ... [ predChar in sub string]
                                        continue
                                    else:   #found a smaller char
                                        
                                        predChar2GreedierIdx = s.find(predChar2, 0, predChIdx)
                                        print("greedy find " , predChar2, " in ", s[:predChIdx], "? ", predChar2GreedierIdx)
                                        if predChar2GreedierIdx == -1:
                                            print(predChar2, " not reducable, hence ", predChar, " not reducable")
                                            chReducable = False
                                            break
                                        else:
                                            
                                            subS = subS.replace(predChar, '')
                                            print(predChar2, " reducable, hence ", predChar, " reducable => ", subS)


                            print( "aggressively reducd subS:", chReducable, subS)

                        if -1 == lexGetsBiggerPoint: #remove it, since something smaller exists between ch and end
                            print( "removed a:", s[:idx], s[idx+1:])
                            s = s[:idx] + s[idx+1:] #remove it
                            idx = s.find(ch)    #find next
                        elif subS != "":
                            #print( "removed b:", s[:idx], "right:",s[idx+1:])
                            #s = s[:idx] + s[idx+1:] #remove it
                            #idx = s.find(ch, idx)    #find next
                            print( "removed b:", s[:idx], "subS:", subS, "right:",s[lexGetsBiggerPoint:])
                            s = s[:idx] + subS + s[lexGetsBiggerPoint:] #remove it
                            idx = s.find(ch, idx)    #find next
                        else:
                            print( "keepit:", s[:idx+1], s[idx+1:])
                            s = s[:idx+1] +s[idx+1:].replace(ch, '') #keep it as the left-most char and fast-forward to the lex-chang point
                            idx = -1

        return s

#print("result: ciorhsaebpunvdyktzfjlgwq" , Solution().removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
#print("result: " , Solution().removeDuplicateLetters("beeaddbeb"))
#print("result: " , Solution().removeDuplicateLetters("bcabc"))
#print("result: " , Solution().removeDuplicateLetters("cbcacdcbc"))
#rint("result: hesitxyplovdqfkz" , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
print("result: " , Solution().removeDuplicateLetters("ccacbacba"))
#print("result: " , Solution().removeDuplicateLetters("ccacbaba"))
#print("result: " , Solution().removeDuplicateLetters("baab"))
