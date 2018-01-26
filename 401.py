class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #10-bit
        start = (0b0000001111111111 >> (10 - num))
        while :
            formatTime(start)
            start <<=1
         
        
    def formatTime(self, timebits):
        hour = (timebits & 0b01111000000) >> 6
        minitue = (timebits & 0xb0000111111)
        print("%d:%02d"% (hour, minitue))