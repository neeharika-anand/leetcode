#Link - https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset=set(nums)
        return len(myset)!=len(nums)
