class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        mapping = defaultdict(int)
        for i in range(len(nums)):
            remaining = target - nums[i]
            if nums[i] in mapping:
                result.append(mapping[nums[i]])
                result.append(i)
                return result
            else:
                mapping[remaining] = i
        return result