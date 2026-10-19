import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        comm = ""
        minum = min(len(str1), len(str2))

        if len(str1) >= len(str2):
            big = str1
        else:
            big = str2

        for i in range(minum):
            if str1[i] != str2[i]: return ""
            comm += str1[i]

        strGCD = math.gcd(len(str1), len(str2))
        
        test = ""
        for i in range(int(len(big)/strGCD)): 
            test += comm[0:strGCD]

        if test != big: return""
        return comm[0:strGCD]


        