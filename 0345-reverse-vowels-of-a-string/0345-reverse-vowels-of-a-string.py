class Solution:
    def reverseVowels(self, s: str) -> str:
        #solution 2
        all_vowels = set("aeiouAEIOU")

        left = 0
        right = len(s)-1
        chars = list(s)

        while left < right:
            if chars[right] in all_vowels and chars[left] in all_vowels:
                chars[right], chars[left] = chars[left], chars[right]
                left+=1
                right-=1
            if chars[left] not in all_vowels:
                left+=1
            if chars[right] not in all_vowels:
                right-=1
        
        return "".join(chars)

        #soltuion 1
        vowels = ["a", "e", "i", "o", "u"]
        t = []
        x=""

        for i in range(len(s)):
            if s[i].lower() in vowels:
                t.append(s[i])

        t.reverse()

        print(t)

        for i in range(len(s)):
            if s[i].lower() in vowels:
                x += t.pop(0)
            else:
                x+=s[i]
    
        return x





        