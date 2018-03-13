MAX_DEEPTH = 11
deadBranches = set()
jumper =[
0x1bffffffffffff, 0x2f6fffffffffff, 0x3dfdbfffffffff, 0x37bff6dfffffff, 0x3ff6fbfb7fffff
,0x3effddffedffff, 0x3fdfff7fffbfff, 0x3fff7fedffd7ff, 0x3ffbffffb7ebff, 0x3fffeffffefdff
,0x3fffffbffffeff, 0x3ffffffeffff5f, 0x3ffffff7fbffab, 0x3fffffffdffff5, 0x3fffffffff7ffe]
ss = 'ABDACFBDGBEICEHCFJDEFDGKDHMEHLEINFIMFJOGHIHIJKLMLMNMNO'
initS = 0x3fffffffffffff
uniMask = '0x324820904101c9'

def getPossibleMove(ssbits):
    results = []
    for i in range(0, 54,3):
        if ssbits & 0x38000000000000 == 0x30000000000000:
            results.append(ss[i:i+3])
        elif ssbits & 0x38000000000000 == 0x18000000000000:
            results.append(ss[i:i+3][::-1])
        ssbits = (ssbits << 3) & 0x3fffffffffffff
    return results

def isAnswer(currentState):
    return bin(currentState & 0x324820904101c9).count('1') == 1

def nextSS(currentState, moves):
    returnFlag = False
    if isAnswer(currentState) :
        print(moves)    # answer
        return True

    mvs = getPossibleMove(currentState)

    for nextMove in mvs:
        newSS = currentState
        newSS &= jumper[ord(nextMove[0]) - ord('A')] #clear
        newSS &= jumper[ord(nextMove[1]) - ord('A')] #clear
        newSS |= jumper[ord(nextMove[2]) - ord('A')] ^ 0x3fffffffffffff #set

        if newSS in deadBranches:
            continue

        moves.append(nextMove)

        if nextSS(newSS, moves) :
            returnFlag = True

        del(moves[-1])

    if len(moves) < MAX_DEEPTH and returnFlag == False:
        deadBranches.add(currentState)
    return returnFlag

nextSS( initS & jumper[ord('F') - ord('A')], [])