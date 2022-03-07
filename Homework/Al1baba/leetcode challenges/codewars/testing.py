from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums).most_common(k)
        count_list = []
        for x in range(k):
            count_list.append(count[x][0])

        return count_list
