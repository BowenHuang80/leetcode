class Solution:
    def __init__(self):
        self.nest =''

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        charSet = sorted(set(s), reverse=True)
        print("start: ", s, self.nest) #charSet)

        for key, y in enumerate(charSet):
            idx1 = s.find(y)
            idx2 = s.find(y, idx1+1)
            print("y:", y, idx1, idx2)
            while idx1 != -1 and idx2 != -1: # found y, and not the last one
                """
                idxZ = -1                   #idxZ = s.find( Z, idx1, idx2)            
                
                for Z in charSet[:key]:
                    idxZ = s.find(Z, idx1, idx2 )
                    if -1 != idxZ:
                        print("Z:",Z)
                        break

                
                #idxX = s.find( X, idx1, idx2)
                idxX = -1
                for X in charSet[key+1:]:
                    idxX = s.find(X, idx1, idx2 )
                    if -1 != idxX:
                        print("X:",X)
                        break  
                """

                idxZ = [ idxZ for idxZ in [s.find(Z, idx1, idx2) for Z in charSet[:key]] if idxZ != -1]
                idxX = [ idxX for idxX in [s.find(X, idx1, idx2) for X in charSet[key+1:]] if idxX != -1]
                print(idxZ, idxX)

                if len(idxZ) != 0:
                    if len(idxX) == 0 or min(idxX) > max(idxZ):
                        #yZy #yZXy  => yZ
                        #remove_yZy(s, idx2)
                        s = s[0:idx2] + s[idx2:].replace(y, '')
                        print("yZy =>yZ", s, y, idx1, idx2, idxX, idxZ)
                        break
                    else:
                        #yXZy => [XZy | y'X'Z] , where 'X' will be removed later
                        self.nest += 'a'
                        greedy_XZy = self.removeDuplicateLetters( s[:idx1] + s[idx1+1:])
                        self.nest = self.nest[:-1]

                        if self.nest == 'a':
                            print("greedy_XZy:", greedy_XZy)
                            return

                        self.nest += 'b'
                        greedy_yXZ = self.removeDuplicateLetters( s[:idx2] + s[idx2+1:])
                        self.nest = self.nest[:-1]

                        print(self.nest, greedy_XZy, greedy_yXZ)
                        if greedy_XZy < greedy_yXZ:
                            #remove_yXZy(s, idx1) # remove 1st y
                            s = s[:idx1] + s[idx1+1:]
                            idx1 = idx2-1
                            idx2 = s.find(y, idx1+1)
                            print("yXZy => XZy", s, y, idx1, idx2, idxX, idxZ)
                            continue
                        else:
                            #remove_yXZy(s, idx2) # remove 2nd y, and the rest
                            s = s[:idx2] + s[idx2:].replace(y, '')
                            print("yXZy => XZy", s, y, idx1, idx2, idxX, idxZ)
                            break
                elif len(idxX) != 0:
                    # yXy => Xy
                    #remove_yXy(s, idx1)
                    s = s[:idx1] + s[idx1+1:]
                    idx1 = idx2-1
                    idx2 = s.find(y, idx1+1)
                    print("yXy=>Xy", s, y, idx1, idx2, idxX, idxZ)
                    continue # while idx1 != -1
                
                else: #yy
                    print("yy", s, y, idx1, idx2, idxX, idxZ)
                    s = s[:idx1] + s[idx1+1:]
                    idx1 = idx2-1
                    idx2 = s.find(y, idx1+1)
                    print("yy2", s, y, idx1, idx2, idxX, idxZ)
                    continue # while idx1 != -1

        return s
print("result: ciorhsaebpunvdyktzfjlgwq" , Solution().removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
#print("result: adbe" , Solution().removeDuplicateLetters("beeaddbeb"))
#print("result: abc" , Solution().removeDuplicateLetters("bcabc"))
#print("result: acdb" , Solution().removeDuplicateLetters("cbcacdcbc"))
print("result: hesitxyplovdqfkz" , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
#print("result: " , Solution().removeDuplicateLetters("ccacbacba"))
#print("result: " , Solution().removeDuplicateLetters("ccacbaba"))
#print("result: " , Solution().removeDuplicateLetters("baab"))

