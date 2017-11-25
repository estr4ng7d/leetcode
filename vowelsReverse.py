#Reverse vowels of string.

vowels="aeiouAEIOU"
        emptyvowels=[]
        newstring=[]
        for i in s:
            if i in vowels:
                emptyvowels.append(i)

        j=len(emptyvowels)-1
        newstring=[]
        for i in range(0,len(s)):
            if s[i] in vowels:
                newstring.append(emptyvowels[j])
                j -= 1
            else:
                newstring.append(s[i])
        return(''.join(newstring))
