class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = -1
        second_max = -1
        max_index = -1

        for i, num in enumerate(nums):
            if num > max_num:
                second_max = max_num
                max_num = num
                max_index = i
            
            elif num > second_max:
                second_max = num
        
        if second_max * 2 > max_num:
            return -1
        
        else:
            return max_index