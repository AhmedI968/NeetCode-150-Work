class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for i in s:
            counter[i] = counter.get(i, 0) + 1

        for char in t:
            if char not in counter:
                return False
            counter[char] -= 1
            if counter[char] < 0:
                return False
        return True