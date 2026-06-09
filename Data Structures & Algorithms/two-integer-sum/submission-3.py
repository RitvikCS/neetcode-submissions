class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new={}
        for i in range(len(nums)):
            if target-nums[i] not in new:
                new[nums[i]]=i
            else:
                x = new[target-nums[i]]
                return [x,i]
        return None
    
            

                