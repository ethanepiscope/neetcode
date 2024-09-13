#Notes: lambda function raaaaah

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ret = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        useful = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            ret.append(useful[i][0])
        return ret