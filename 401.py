#88ms
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self._results = []
        self.helper( 0b0000000000, 10, num)

        return self._results

    def reject(self, ts):
        return (ts & 0b1111000000) >= 0b1100000000 or (ts & 0b0000111111 > 59)


    def outputTime(self, timebits):
        if self.reject(timebits):
            return
        
        self._results.append('%d:%02d' % (timebits  >> 6, timebits & 0b0000111111))

    def helper(self, fixedUpperBits, length, onBits):

        if self.reject(fixedUpperBits):
            return

        if onBits == 1:
            singleBitMask = 0b1;
            for  i in range(length):
                self.outputTime(fixedUpperBits | singleBitMask)
                singleBitMask <<=1
            return

        elif onBits == length:

            self.outputTime(fixedUpperBits | (2**onBits - 1))
            return

        else:
            start = 0
            for d in range( length-1 ):
                if d < onBits:
                    start |= 0b1
                start <<= 1

            self.outputTime( fixedUpperBits | start)

            while start > 0:
                newLength = length - onBits
                start -= 0b1<< newLength
                leftBits = onBits - bin(start).count('1')

                if leftBits <= newLength:
                    self.helper( fixedUpperBits | start, newLength,  leftBits )

        return