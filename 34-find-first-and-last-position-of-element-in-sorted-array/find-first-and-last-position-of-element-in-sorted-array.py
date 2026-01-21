class Solution:
    def searchRange(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(nums) and nums[left] == target:
                return left
            return -1
        
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right >= 0 and nums[right] == target:
                return right
            return -1
        
        first = find_first(nums, target)
        last = find_last(nums, target)
        return [first, last]