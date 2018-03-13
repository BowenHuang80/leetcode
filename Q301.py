#301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.indexing(s)

        if (self.unmatchLP == 0 and self.unmatchRP == 0 ):
            return ''.join(self.ss)

        self.ans = []

        self.i, self.j = -1, -1
        pLP, pRP = [], []

        if self.unmatchLP >0 :
            pLP = [ i for i in range(self.lpp - self.unmatchLP, self.lpp, 1)] 
            self.i = 0
        if self.unmatchRP >0 :
            pRP = [ i for i in range(self.unmatchRP)]
            self.j = self.unmatchRP -1

        while (self.unmatchRP >0 and self.j>= 0) and (pRP[0] <= self.lastUnmatchRPIdx - self.unmatchRP +1 ) \
            or (self.unmatchLP >0 and self.i < self.unmatchLP and pLP[0] >= self.startUnmatchLPIdx) :
            tmpS = list(self.ss)
            for ij in range(self.unmatchRP):
                tmpS[ self.rpIdx[ pRP[ij] ] [0] ] = '' # remove ) @

            for ij in range(self.unmatchLP):
                tmpS[ self.lpIdx[ pLP[ij] ] [0] ] = '' # remove ( @

            self.ans.append((list(pLP), list(pRP), ''.join(tmpS)))

            if self.unmatchLP > 0:
                while self.i < self.unmatchLP:
                    pLPj = pLP[self.i]
                    lastIdx = self.lpIdx[pLPj][0]

                    if pLPj >= self.startUnmatchLPIdx + self.i:
                        pLPj -= 1
                        
                    # fast-forward to skip consecutive '(...('
                    while self.lpIdx[pLPj][0] == lastIdx -1:
                        lastIdx -= 1
                        pLPj -= 1
                    
                    if pLPj < self.startUnmatchLPIdx + self.i\
                        or ( self.i + 1 > self.lpIdx[pLPj][1] ) \
                        or ( self.lpIdx[pLPj][1] == 1 and self.lpIdx[pLPj+1][2] != 0) \
                        or ( self.lpp - self.lpIdx[pLPj+1][1] +1 - (self.unmatchLP -1- self.i ) \
                        > self.rpp - self.lpIdx[pLPj+1][2] ) :
                        self.i += 1 #illegal, move to next
                        continue
                    else:
                        pLP[self.i] = pLPj
                        for jj in range(self.i -1, -1, -1) : #cascading
                            pLP[jj] = pLP[jj+1] -1
                        self.i = 0
                        break

            # start to remove next ')' only when all '(' combinations are done
            if self.unmatchRP > 0 and (self.unmatchLP == 0 or self.i >= self.unmatchLP):
                while self.j >= 0:
                    pRPj = pRP[self.j]
                    lastIdx = self.rpIdx[pRPj][0]
                    #if pRPj < self.lastUnmatchRPIdx + 1 - self.unmatchRP + self.j \
                    if pRPj <= self.lastUnmatchRPIdx + 1 - self.unmatchRP + self.j \
                        or self.rpIdx[pRPj][1]  < self.rpIdx[pRPj][2] :
                        # fast-forward to skip consecutive ')' 
                        pRPj += 1

                    while pRPj + ( self.unmatchRP -1 -self.j) <= self.lastUnmatchRPIdx \
                        and self.rpIdx[pRPj][2] - self.j -1 <= self.rpIdx[pRPj][1] \
                        and self.rpIdx[pRPj][0] == lastIdx +1 :
                        lastIdx += 1
                        pRPj += 1

                    if pRPj + ( self.unmatchRP -1 - self.j) > self.lastUnmatchRPIdx \
                        or self.rpIdx[pRPj][2] - self.j -1 > self.rpIdx[pRPj][1] \
                        or self.rpIdx[pRPj-1][4] - self.j -1 == self.rpIdx[pRPj-1][3] :
                        self.j -= 1
                        continue
                    else:
                        pRP[self.j] = pRPj
                        for jj in range(self.j+1, self.unmatchRP) : #cascading
                            pRP[jj] = pRP[jj-1] +1

                        self.j = self.unmatchRP -1  # move to the end

                        # reset LP if any
                        if self.unmatchLP > 0 and self.i >= self.unmatchLP:
                            self.i = 0
                            #if self.unmatchLP >0 :
                            pLP = [ i for i in range(self.lpp - self.unmatchLP, self.lpp, 1)] 

                        break

        return self.ans

    def indexing(self, s):
        self.rp, self.lp, self.lpp, self.rpp =0,0,0,0

        self.rpIdx, self.lpIdx, self.otherIdx = [], [], []
        self.unmatchLP, self.unmatchRP = 0, 0
        self.startUnmatchLPIdx, self.lastUnmatchRPIdx = 0, 0
        ss = list(s)

        i = len(ss) -1
        while i >=0 and ss[i] != ')' :
            if ss[i] == '(':
                ss[i] = ''
            i -= 1

        for idx, ch in enumerate(ss):
            ch = ss[idx]
            if ch == '(' :
                self.lp +=1
                self.lpp +=1
                self.lpIdx.append((idx, self.lpp, self.rpp, self.lp, self.rp))

            elif ch == ')' :
                if self.lp == 0 and self.unmatchRP == 0:
                    ss[idx] = ''
                else:
                    self.rp +=1
                    self.rpp +=1
                    self.rpIdx.append((idx, self.lp, self.rp,  self.lpp, self.rpp))
                    if self.rp > self.lp :  # unmatched ')'
                        self.unmatchRP += 1
                        self.lastUnmatchRPIdx = self.rpp -1
                        self.startUnmatchLPIdx = self.lpp
                        self.lp = 0
                        self.rp = 0
            else:
                self.otherIdx.append(idx)    # inputs other than '()'


#       # remove dangling '(' from tail
#        idx = self.lpp -1
#        while (self.rpp == 0 or self.lpIdx[ idx ][0] > self.rpIdx[ self.rpp-1 ][0]) and idx >=0 :
#            ss[self.lpIdx[idx][0]] = ''
#            del(self.lpIdx[idx])
#            idx -= 1
#            self.lpp -= 1
#            self.startUnmatchLPIdx -= 1


        if( self.rpp > 0 ):
            lastRP = self.rpIdx[ self.rpp -1 ]
            self.unmatchLP = lastRP[1] - lastRP[2]

        self.ss = ss
        #return (lp, rp, maxUnmatch, lpIdx, rpIdx, otherIdx)

a = Solution()

#'*())*()*()*()*()*())))()((((((((((((()())()()*()*()*()*()*()*()*()*)(*)(*)(*)(*)*&&&&&&&&&&&*())))))))((((((((((()()())))))))))))()()()()*((()*())))))))))))()*)(*()(*)()*)(*()*()*()*)()*(&()(',
tests = ['())(v()(h','())((()))x)(v()(h','a))()(((k()((','))(((k()((','(((k()((','(())))a))f()f(d(((s)()((()f','(())))a))f()f(d(((s)','()a)f()f(d((s)','())a)f()f(d((s)', 'a(d(f)g','a()d)','())','(()','(a())', 'd(d)d(d)a', '())(()', '()(()((','(r(()()(', '', '()', '((', '))((', '))', '))a((bdd', '))a((', '(a)9fd0s)(F)D()D(F)S()F(D)()', '()))())))' ,  '()a((bdd)']

#print(a.removeInvalidParentheses('a()d)'))
for t in tests:
    #print(t, 
    a.removeInvalidParentheses(t)
    #)