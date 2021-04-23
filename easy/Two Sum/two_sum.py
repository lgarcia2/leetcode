# problem setup
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my code
        for i in range (0,len(nums)):
            first_num = nums[i]
            for j in range (0,len(nums)):
                second_num = nums[j]
                if j == i:
                    continue
                elif (first_num + second_num) == target:
                    return [i, j]
                else: 
                    continue
            