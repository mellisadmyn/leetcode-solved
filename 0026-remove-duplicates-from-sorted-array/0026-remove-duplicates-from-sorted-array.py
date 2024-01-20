class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_pointer = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pointer]:
                unique_pointer += 1
                nums[unique_pointer] = nums[i]

        return unique_pointer + 1