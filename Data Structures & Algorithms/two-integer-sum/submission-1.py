class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       checkAdds = set()
       
       for i, row in enumerate(nums):
        for j, value in enumerate(nums):
            if (nums[i] + nums[j] == target and i != j):
                result = [i,j]
                return result
            
 