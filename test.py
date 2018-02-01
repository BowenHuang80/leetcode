s = "yciccqiorq"
s2 = "yioccdqiorq"
charSet = sorted(set(s), reverse=True)

idx = s.find('q')
subS = "io"

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


print(chReducable, subS)