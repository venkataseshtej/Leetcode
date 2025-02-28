class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        l=0
        for r in range(n):
            if nums[r]:
                nums[l],nums[r]= nums[r],nums[l]
                l+=1
                # r+=1
        return nums






        """
        Do not return anything, modify nums in-place instead.
        """
        