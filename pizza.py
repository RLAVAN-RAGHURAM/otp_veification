class Solution(object):

    def twoSum(self, nums, target):
        x=0
        k=0
        for i in range(len(nums)):
            if nums[x]+nums[k+1] ==target:
                z=[nums[x],nums[k+1]]
                return z
obg=Solution()
obg.twoSum([1,2,3,4,5],9)
