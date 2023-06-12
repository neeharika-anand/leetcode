# Link - https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                num = math.prod(nums[:i]) * math.prod(nums[i+1:])
                hashmap[nums[i]] = num
            else:
                num = hashmap[nums[i]]
            ans.append(num)

        return ans
