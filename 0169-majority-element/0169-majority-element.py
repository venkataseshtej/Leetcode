class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element= nums[0]
        c=1
        for i in range(1,len(nums)):
            if nums[i]==element:
                c+=1
            elif nums[i]!=element and c !=0:
                c-=1
            else:
                c=1
                element=nums[i]
        return element






        # l=len(nums)
        # c=Counter(nums)
        # for i in c:
        #     if c[i]> math.floor(l/2):
        #         return i
        

        