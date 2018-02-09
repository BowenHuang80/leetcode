# Range Sum Query - Mutable
import math
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.len = len(nums)

        if len(nums) == 0 :
            return

        self.depth = math.ceil(math.log(self.len, 2))
        self.table = [ None for i in range(2**(self.depth+1) -1)]
        
        self.constructBT(nums, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        #node = self.len + i
        #var = val - self.table[node]
        if self.len == 0 or i >= self.len or i < 0:
            return
        
        var = val - self.nums[i]
        self.nums[i] = val
        
        self.updateBT(i, var, 0, self.len-1, 0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.len == 0:
            return None

        return self.sumRangeBT(i,j, 0, self.len-1, 0)

    def constructBT(self, nums, root):
        if len(nums) == 1 :
            self.table[root] = nums[0]
        else:
            mid = math.ceil(len(nums) / 2)
            self.table[root] = self.constructBT(nums[: mid], 2*root+1 ) + self.constructBT( nums[mid :], 2*root+2)

        return self.table[root]

    def updateBT(self, node, var, btI, btJ, root):

        if node >= btI and node <= btJ :
            self.table[root] += var
            if btI != btJ :
                mid = math.floor((btI + btJ) /2)
                self.updateBT(node, var, btI, mid, 2*root+1)
                self.updateBT(node, var, mid+1, btJ, 2*root+2)

        
    def sumRangeBT(self, i, j, btI, btJ, root):
        if btI >= i and btJ <= j :  # whole tree @ root
            return self.table[root]
        
        elif j < btI or i > btJ:
            return 0

        else:
            mid = math.floor( (btI + btJ) /2)
            return self.sumRangeBT( i, j, btI, mid, 2*root + 1 ) + self.sumRangeBT(i, j, mid+1, btJ, 2*root + 2)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

#constructBT([ 3, 0, 2, 4, 2, 4, 51, 21, 2, 9, 7, 4, 9, 0, -2], 0)
#n = 15
#sumRange(0,2) =>
#0,2, 0, 7, 1
#
#0,2, 0, 3, 3                +  (0 = 0,2, 4, 7, 4 )
#(3=0,2, 0,1, 7) +  0,2,2,3,8
#                   (2 = 0,2,2,2,17) + (0 = 0,2,3,3,18 )

