class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setLength = len(set(nums))
        return setLength != len(nums)