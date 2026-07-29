class Solution(object):
    def searchRange(self, nums, target):
        first = self.binarySearch(nums,target,True)
        last = self.binarySearch(nums,target,False)
        return [first, last]

    def binarySearch(self,nums,target,leftBian):
        left = 0
        right = len(nums)-1
        ans = -1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                ans = mid
                if leftBian:
                        right = mid - 1
                else:
                        left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    