#Original solution was pretty dumb just using split, join, and a pseudorandom
#sequence asa delimeter. This solution feels safer to me

class Solution:

    def encode(self, strs: List[str]) -> str:
        #Handling edge case
        if not strs:
            return ""
        
        #Creating the encoding
        encoding = []
        firstLetterTracker = 0
        for s in strs:
            encoding.extend([str(firstLetterTracker),'+'])
            firstLetterTracker += len(s)
        encoding[-1] = "="

        #Stick the smushed string on the end
        return ''.join(encoding) + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        #edge case check
        if s == "":
            return []

        #Isolate encodings and smushed string
        [encodings,s] = s.split('=', maxsplit=1)
        startPos = [int(num) for num in encodings.split('+')]

        #Build return list
        ret = []
        for i in range(len(startPos)-1):
            ret.append(s[startPos[i] : startPos[i+1]])
        ret.append(s[startPos[len(startPos)-1]:])
        return ret