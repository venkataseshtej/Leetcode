class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for idx,i in enumerate(nums):
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1]= nums[abs(i)-1]* -1
        res=[]  
        for idx,i in enumerate(nums):
            if i >0:
                res.append(idx+1)
        return res



        