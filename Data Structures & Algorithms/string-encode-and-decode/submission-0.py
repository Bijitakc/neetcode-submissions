class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for each in strs:
            encoded_str += f"{len(each)}#{each}"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            seperator = s.find("#", i)
            length = int(s[i:seperator])
            word = s[seperator+1:seperator+1+length]
            res.append(word)
            i = seperator+1+length
        return res
