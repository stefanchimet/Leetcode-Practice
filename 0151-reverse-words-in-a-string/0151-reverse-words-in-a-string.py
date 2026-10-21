class Solution:
    def reverseWords(self, s: str) -> str:
        sentence =[]
        word = []

        for char in s.strip():
            if char !=" ":
                word.append(char)

            elif char == " " and word:
                sentence.insert(0,"".join(word))
                word.clear()
        
        sentence.insert(0,"".join(word))

        print(sentence)
        return " ".join(sentence)