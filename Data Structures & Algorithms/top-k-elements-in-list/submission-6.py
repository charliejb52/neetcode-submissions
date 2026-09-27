class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        counts = dict(sorted(counts.items(), key=lambda item: item[1]))

        return list(counts.keys())[::-1][0:k]
        