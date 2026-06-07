class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        mranges = []
        if not nums:
            return [[lower, upper]]
        if lower < nums[0]:
            mranges.append([lower, nums[0]-1])
        i = 0
        while i < len(nums)-1:
            if nums[i+1]-nums[i]!=1:
                mranges.append([nums[i] + 1, nums[i + 1] - 1])
            i+=1
        if upper > nums[-1]:
            mranges.append([nums[-1]+1, upper])

        return mranges
