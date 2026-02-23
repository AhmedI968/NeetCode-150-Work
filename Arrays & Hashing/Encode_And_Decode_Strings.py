class Solution:

    def encode(self, strs: List[str]) -> str:
        # Delimiter might be in the string, it considers alll 256 valid ASCII characters
        # But still need something to determine length of each word and a delimiter 
        # So if the delimiter is in the word it reads from 5# for 5 letters and stops at next hash
        stringReturn = ""
        for string in strs:
            stringReturn += str(len(string)) + "#" + string 

        return stringReturn

    def decode(self, s: str) -> List[str]:
        listReturn = []
        i = 0

        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1
                
            length = int(s[i:j])
            j += 1

            listReturn.append(s[j:j+length])

            i = j + length

        return listReturn