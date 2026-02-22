class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Prolly a better solutio out there
        # Go through the array once and count number of frequncies then sort
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        pairs = list(freq.items())
        
        # Sort to get most numerous
        for i in range(len(pairs)):
            best = i
            for j in range(i + 1, len(pairs)):
                if pairs[j][1] > pairs[best][1]:
                    best = j
            pairs[i], pairs[best] = pairs[best], pairs[i]

        result = []
        for i in range(k):
            result.append(pairs[i][0])

        return result