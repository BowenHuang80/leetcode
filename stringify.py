import base64
import sys

if len(sys.argv) != 3
  raise ValueError('usage: base64 encoded file.txt     decoded outputfile')
 
inFile = sys.argv[1]
outFile = sys.argv[2]

inFileData = open(inFile, 'r')
outFileData = open(outFile, 'wb')

outFileData.write(base64.b64decode(inFileData.read()))

inFileData.close()
outFileData.close()

print('Done!')

