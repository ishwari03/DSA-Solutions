class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        pairs = []
        for num,freq in count.items():
            pairs.append([freq,num])
        pairs.sort(reverse=True)

        res = []
        for freq,num in pairs[:k]:  #slices the first k elements from sorted list 
            res.append(num)
        return res
        