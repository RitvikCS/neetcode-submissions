class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        bucket = [[] for i in range(len(nums)+1)]
        for key,val in freq.items():
            bucket[val].append(key)
        c=0
        x = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                if c<k:
                    x.append(num)
                    c+=1
        return x