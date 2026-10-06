class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Input: nums = [1, 2, 3, 3]
        seen = set()
        
        
        for num in nums:
            if (num in seen):
                return True;
            else:
                return False;
        
            
        