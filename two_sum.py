class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        cnt = len(nums)
        for i in range(cnt):
            complement = target - nums[i]
            if complement in nMap:
                return [i, nMap[complement]]
            nMap[nums[i]] = i