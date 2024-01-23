class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_counts = {}

        for num in nums:
            if num in element_counts:
                return True
            
            element_counts[num] = 1

        return False