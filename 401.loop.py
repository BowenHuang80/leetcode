
from datetime import datetime

def readBinaryWatch(num):
    return ['%d:%d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]


print(datetime.utcnow())
print(readBinaryWatch(5))
print(datetime.utcnow())