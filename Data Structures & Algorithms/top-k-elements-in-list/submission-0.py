class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hole = {}
        freq =[[] for i in range (len(nums)+1)]
        for c in nums:
            hole[c] = hole.get(c,0) + 1
        for c , f in hole.items():
            freq[f].append(c)
        res = []
        for i in range(len(freq) -1 , 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
        
        