#Link - https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):  
        hashmap={}
        for i,n in enumerate(nums): #gives both index and value
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]=i #hashmap maps value to index
        return
