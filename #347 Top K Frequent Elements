'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''


nums, k = [1,1,1,2,2,3], 2
nums1, k1 = [1], 1


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hash_map = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        hash_map[num] = 1 + hash_map.get(num, 0)
    for a, b in hash_map.items():
        freq[b].append(a)

    top_freq = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            top_freq.append(n)
            if len(top_freq) == k:
                return print(top_freq)


topKFrequent(nums, k)
topKFrequent(nums1, k1)
