# Link - https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def hashfunc(s):
        #     count=[]
        #     for i in range(0,26):
        #         count.append(0)
        #     for i in s:
        #         count[ord(i)-ord('a')]+=1
        #     return str(count)

        # hashmap={}
        # result=[]
        # for s in strs:
        #     subhash=hashfunc(s)
        #     if subhash in hashmap:
        #         hashmap[subhash].append(s)
        #     else:
        #         hashmap[subhash]=[]
        #         hashmap[subhash].append(s)

        # return list(hashmap.values())
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
