import math

class NumArray:
    """
    Binary Tree
    Time C:  O(logn)
    Space C: O(2n)
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.len = len(nums)
        self.table = [ None for i in range(2*self.len -1)]

        self.constructBT(nums, 0)


    def constructBT(self, nums, s):
        if len(nums) == 1 :
            self.table[s] = nums[0]
        else:
            mid = math.ceil(len(nums) / 2)
            self.table [ s ] = self.constructBT(nums[: mid], 2*s+1 ) + self.constructBT( nums[mid :], 2*s+2)

        return self.table[s]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        O(n/2)
        """
        pass

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        O(logn)
        """
        #sum(i,j) = sum(0,n) - sum(0, i-1) - sum(j+1, n)
        mid = math.ceil(self.len / 2)
        if j <= mid :
            sumRange(i, j) + sumRange()

        return 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

#constructBT([ 3, 0, 2, 4, 2, 4, 51, 21, 2, 9, 7, 4, 9, 0, -2], 0)
#n = 15
