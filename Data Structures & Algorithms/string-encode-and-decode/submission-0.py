class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for n in strs:
            encoded_string = encoded_string + str(len(n)) + "&" + n
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        n = 0
        while n < len(s):
            num = ''
            m = n
            while s[m] != "&":
                m += 1
            length = int(s[n:m])
            decoded_strs.append(s[m+1:m+length+1])
            n = m + length + 1
            
        return decoded_strs
