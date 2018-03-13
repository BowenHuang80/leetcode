
def printS(curSS):
    ss    =  'AB  C  D  E     F     G  H     I     J       KLM  N  O'
    uMask = 0b110010010010000010000010010000010000010000000111001001
    bM    = 0b100000000000000000000000000000000000000000000000000000
    r = []
    for idx,ch in enumerate(ss):
        if (uMask & curSS) & bM != 0 and ch != ' ':
            r.append(ch)
        bM >>= 1

    return ' '.join(r)

jumper =[
 0b011011111111111111111111111111111111111111111111111111   #  A
,0b101111011011111111111111111111111111111111111111111111   #  B
,0b111101111111011011111111111111111111111111111111111111   #  C
,0b110111101111111111011011011111111111111111111111111111   #  D
,0b111111111101101111101111111011011111111111111111111111   #  E
,0b111110111111111101110111111111111011011111111111111111   #  F
,0b111111110111111111111101111111111111111011111111111111   #  G
,0b111111111111110111111111101101111111111101011111111111   #  H
,0b111111111110111111111111111111101101111110101111111111   #  I
,0b111111111111111110111111111111111111101111110111111111   #  J
,0b111111111111111111111110111111111111111111111011111111   #  K
,0b111111111111111111111111111110111111111111111101011111   #  L
,0b111111111111111111111111110111111110111111111110101011   #  M
,0b111111111111111111111111111111110111111111111111110101   #  N
,0b111111111111111111111111111111111111110111111111111110   #  O
]


initS = 0b111111111111111111111111111111111111111111111111111111

ss =       'ABDACFBDGBEICEHCFJDEFDGKDHMEHLEINFIMFJOGHIHIJKLMLMNMNO'
uniMask = 0b110010010010000010000010010000010000010000000111001001

def getPossibleMove(ssbits):
    mask =     0b111000000000000000000000000000000000000000000000000000
    pattern = [0b110000000000000000000000000000000000000000000000000000, \
               0b011000000000000000000000000000000000000000000000000000]
    results = []

    for i in range(0, 54,3):
        if ssbits & mask == pattern[0]:
            results.append(ss[i:i+3])
        elif ssbits & mask == pattern[1]:
            results.append(ss[i:i+3][::-1])

        ssbits = (ssbits << 3) & 0x3fffffffffffff

#    if len(results) == 0:
#        print('no moves @ ', bin(ssbits))
#    else:
#        pass #print(results)
    return results

def isAnswer(ssbits):
    '''

    '''
    return bin(ssbits).count('1') == 1

def updateSS(ssbits, nextMove):
    '''
    ABF -> XXA
    '''
    ssbits &= jumper[ord(nextMove[0]) - 65] #clear
    ssbits &= jumper[ord(nextMove[1]) - 65] #clear
    ssbits |= jumper[ord(nextMove[2]) - 65] ^ 0x3fffffffffffff #set
    return ssbits

deadBranches = set()

def nextSS(ssbits, moves):
    returnFlag = False
    if bin(ssbits&uniMask).count('1') == 1 :
        print('answer:', moves)
        return True

    mvs = getPossibleMove(ssbits)
    #print( moves, mvs)
    for nextMove in mvs:
        #newSS = updateSS(ssbits, nextMove)
        newSS = ssbits
        newSS &= jumper[ord(nextMove[0]) - 65] #clear
        newSS &= jumper[ord(nextMove[1]) - 65] #clear
        newSS |= jumper[ord(nextMove[2]) - 65] ^ 0x3fffffffffffff #set

        if newSS in deadBranches:
            #print('hit dead end', printS(newSS))
            continue

        moves.append(nextMove)

        if nextSS(newSS, moves) :
            returnFlag = True
            #return True
            del(moves[-1])
        else:
            del(moves[-1])

    if len(moves) < 11 and returnFlag == False: # all moves failed
        deadBranches.add(ssbits)    # shortest branch

    return returnFlag  # if not allFail, then return Ture, so that it doesn't get pruned


print("start")
nextSS( initS & jumper[ord('F') - 65], [])
#for c in range(ord('A'), ord('O')+1):
#    if nextSS( initS & jumper[c - 65], []):
#        print('found', chr(c))
#    else:
#        print('no', chr(c), len(deadBranches))
    
#    deadBranches.clear()

