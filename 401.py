def countSetBits(n):
    count = 0
    while n:
        n &= (n-1)
        count+=1
 
    return count


def formatTime(timebits):
    hour = (timebits & 0b1111000000) >> 6
    minitue = (timebits & 0b0000111111)
    #print("%d:%02d"% (hour, minitue))
    print( "{:04b}".format(hour), "{:06b}".format(minitue))

class Solution:

    def red(self, fixedUpperBits, length, onBits):
        print(length, onBits)

        if onBits == 1:
            singleBitMask = 0b1;
            for  i in range(length):
                formatTime(fixedUpperBits | singleBitMask)
                singleBitMask <<=1
            #print("return 1")
            return

        elif onBits == length:
            lowerBits = 0
            for d in range( onBits ):
                lowerBits = (lowerBits << 1) | 0b1
            formatTime(fixedUpperBits | lowerBits)
            print("return 2")
            return

        else:
            start = 0
            for d in range( length-1 ):
                if d < onBits:
                    start |= 0b1
                start <<= 1

            formatTime( fixedUpperBits | start)

            while start > 0:
                start -= (0b1<<(length-onBits))
                print("newBase: ", "{:082b}".format( start), length - onBits, (onBits - countSetBits(start)))
                if (onBits - countSetBits(start)) <= (length - onBits):
                    self.red( fixedUpperBits | start, length - onBits,  onBits - countSetBits(start) )
                else:
                    print("return 3 b")
                    return


            #print("return 4")

    # Function to get no of set bits in binary
    # representation of passed binary no. */

    def readBinaryWatch(self, length2, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #start = (0b1111111111 >> (10 - num)) << num
        if length2 > 10:
            print("error, > 10")
        else:
            self.red( 0b0, length2, num)


so = Solution()

so.readBinaryWatch(10, 3)