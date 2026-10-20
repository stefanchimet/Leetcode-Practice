class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        if len(word1)>=len(word2):
            for i in range(len(word2)):
                word += word1[i]
                word += word2[i]
            word += word1[len(word2):]
        
        if len(word2)>len(word1):
            for i in range(len(word1)):
                word += word1[i]
                word += word2[i]
            word += word2[len(word1):]

        return word