class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range (n):
            temp=abs(nums[i])
            if nums[temp]<0:
                res=temp
                break
            else:
                nums[temp]*=-1
        for i in range (n):
            if nums[i]<0:
                nums[i]*=-1
        return(res)
        