class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Thought process
        # Sort each word, then group them??
        # Use dictionary to look them up

        solution = {}

        for word in strs:
            keyDict = ''.join(sorted(word))
            if keyDict not in solution:
                solution[keyDict] = []
            solution[keyDict].append(word)
        
        return list(solution.values())

        # Works but maybe change the key, as sorting might be a unnecessary step
        