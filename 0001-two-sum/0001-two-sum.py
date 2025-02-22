class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        n= len(nums)
        for i in range(n):
            for k in range(i+1,n):
                if nums[k]+ nums[i] == target :

                    res.append(i)
                    res.append(k)
        return res
        