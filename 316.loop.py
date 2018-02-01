
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
import re
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = {}        
        print(s)
        #s = ''.join(re.compile(r'([a-z])\1').split(s))  #remove adjacent duplicates
        charSet = sorted(set(s), reverse=True)

        for key, ch in enumerate(charSet):
            #print("processing:", ch, "key:", key)

            idx = s.find(ch)
            while( -1 != idx ):
                if idx < (len(s)-1) and ch == s[idx+1]:
                    s = s[:idx] + ' ' + s[idx+1:] # remove immediate twin
                    print(s, "twin")
                else:
                    if -1 == s.find(ch, idx+1): # search again, only apperance
                        #keep it, do nothing
                        print("last ", ch, " in ", s)
                        break
                    else:
                        lexGetsBiggerPoint = -1
                        subS = ""
                        
                        if key > 0:
                            for i in reversed(range(key)): #include itself
                                #print( "nextBiggerChar:", charSet[i])
                                lexGetsBiggerPoint = s.find( charSet[i], idx+1 )
                                if -1 != lexGetsBiggerPoint:
                                    #lexGetsBiggerPoint += idx
                                    break
                        
                        if -1 != lexGetsBiggerPoint:
                            subS = s[idx+1 : lexGetsBiggerPoint]
                            print( "subS:", subS)

                            #for predCh in set(subS):
                            #    print("search in left:", s[:idx])   #dont' include current char to avoid "babc"
                            #    if s.find( predCh, 0, idx) != -1:
                            #        s[s.find( predCh, 0, idx) : idx]
                            #        print("found:", predCh)
                            #        subS = subS.replace( predCh, '')    #aggressive removing predCh, since it appears on the left side of current ch
                            chReducable = True
                            for predChar in set(subS.replace(' ', '')):
                                predChIdx = s.rfind(predChar, 0, idx)
                                if predChIdx == -1:
                                    chReducable = False
                                    continue
                                #print( "predChIdx:", predChar, predChIdx)
                                 #"yic" "i" "occd" "q" "io" "r" "q"
                                 # greedy reduce between  predChar .grdy..   ch subS prev[ch]
                                tmp = [ cc for cc in charSet if cc < predChar]
                                #print( tmp )
                                for predChar2 in tmp:
                                    
                                    predChar2Idx = s.find(predChar2, predChIdx, idx)
                                    #print("find ", predChar2, " in: ", s[predChIdx : idx], "? ", predChar2Idx)
                                    if predChar2Idx == -1:  # predChar ... predChar2<predChar ...  [current char] ... [ predChar in sub string]
                                        continue
                                    else:   #found a smaller char
                                        
                                        predChar2GreedierIdx = s.rfind(predChar2, 0, predChIdx) # in reverse to find the cloest char
                                        #print("greedy find " , predChar2, " in ", s[:predChIdx], "? ", predChar2GreedierIdx)
                                        if predChIdx != 0 and predChar2GreedierIdx == -1:
                                            #print(predChar2, " not reducable, hence ", predChar, " not reducable")
                                            chReducable = False
                                            break
                                        else:
                                            #print(subS)
                                            subS = subS.replace(predChar, ' ')
                                            #print(subS, " removed: ", predChar)
                                            print( "subS:", subS)
                                            break


                            #print( "aggressively reducd subS:", chReducable, subS)

                        if -1 == lexGetsBiggerPoint: #remove it, since something smaller exists between ch and end
                            s = s[:idx] + " " + s[idx+1:]
                            print(s, "a")
                            idx = s.find(ch, idx)    #find next
                        elif subS != "":
                            #print( "removed b:", s[:idx], "right:",s[idx+1:])
                            #s = s[:idx] + s[idx+1:] #remove it
                            #idx = s.find(ch, idx)    #find next
                            s = s[:idx] + " " + subS + s[lexGetsBiggerPoint:]
                            print(s, "b")
                            idx = s.find(ch, idx)    #find next
                        else:
                            s = s[:idx+1] +s[idx+1:].replace(ch, " ") #keep it as the left-most char and fast-forward to the lex-chang point
                            print(s, "c")
                            idx = -1

            print(s)

        return s

print("result: ciorhsaebpunvdyktzfjlgwq" , Solution().removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk").replace(' ', ''))
#print("result: " , Solution().removeDuplicateLetters("beeaddbeb"))
#print("result: abc" , Solution().removeDuplicateLetters("bcabc"))
#print("result: acdb" , Solution().removeDuplicateLetters("cbcacdcbc"))
#print("result: hesitxyplovdqfkz" , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
#print("result: abc" , Solution().removeDuplicateLetters("ccacbacba"))
#print("result: acb" , Solution().removeDuplicateLetters("ccacbaba"))
#print("result: ab" , Solution().removeDuplicateLetters("baab"))


