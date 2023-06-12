class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        hashmap={}
        result=[]
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)
        result = sorted(hashmap, key = lambda x: hashmap[x], reverse = True)
        return result[:k]