class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        suff = [1] * len(nums)
        preff = [1] * len(nums)

        for i in range(len(nums)):
            if i != 0:
                preff[i] = preff[i-1] * nums[i-1]
                suff[len(nums)-i-1] = suff[len(nums)-i] *nums[len(nums)-i]
            
        return [suff[i]*preff[i] for i in range(len(nums))]
            

