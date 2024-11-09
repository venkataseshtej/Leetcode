class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        # last_num = -187
        for i in range(1, len(nums)):
            if nums[index] != nums[i]: 
                index += 1
                nums[index] = nums[i]
                # last_num = nums[i]
            else:
                continue
        return index+1