class Solution:
    def __init__(self):
        self.nest =''
    def removeDuplicateLetters(self, s):
        return self.removeDuplicateLettersOther1(s)


    def removeDuplicateLettersOther1(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

    def removeDuplicateLetters3(self, s):
        """
        :type s: str
        :rtype: str
 
        result =''
        ch = A
        charIdx = 0
        while len(charSet) != 0:
            ch = charSet[charIdx]
            #can ch be the first?
            if exists( max(idx(Z)) < min(idx(ch)) )?
                #ch can't be the frist
                charIdx  += 1
            else
                s = s[ : min(idx(ch)) +1].replace(ch, '') # remove all chars before ch to get max lexicographical value
                result += ch
                charSet.remove(ch) # ch is done
                charIdx  += 1

        """

        charSet = sorted(set(s))
        print("start: ", s, charSet)
        result = ''
        charIdx = 0

        maxIdx = [s.rfind(ch) for ch in charSet]        # [ max idx a, max idx b, ...]
        minIdx = { ch : s.find(ch) for ch in charSet}   # [ a: idx, b:idx, c:idx]
        print( maxIdx, minIdx)

        while len(charSet) != 0:
            print(charSet, charIdx, maxIdx)
            ch = charSet[charIdx]
            if min(maxIdx[charIdx:])  < minIdx[ch]:    # exists a letter bigger than ch, and only appears before ch
                charIdx +=1
            else:
                result += ch
                s = s[minIdx[ch] +1:].replace(ch, '')
                print(result, s)
                charSet.remove(ch)
                minIdx = { ch : s.find(ch) for ch in charSet}
                maxIdx = [s.rfind(ch) for ch in charSet]
                charIdx =0  # reset to the first letter

        return result

print("result: ciorhsaebpunvdyktzfjlgwq" , Solution().removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
print("result: adbe" , Solution().removeDuplicateLetters("beeaddbeb"))
print("result: abc" , Solution().removeDuplicateLetters("bcabc"))
print("result: acdb" , Solution().removeDuplicateLetters("cbcacdcbc"))
print("result: hesitxyplovdqfkz" , Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
print("result: " , Solution().removeDuplicateLetters("ccacbacba"))
print("result: " , Solution().removeDuplicateLetters("ccacbaba"))
print("result: " , Solution().removeDuplicateLetters("baab"))

