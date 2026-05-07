class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)          
        nums[:] = nums[-k:] + nums[:-k]