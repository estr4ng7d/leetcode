'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
'''

if len(ransomNote)>len(magazine):
            return False
        
        
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)
                ransomNote=ransomNote.replace(i,'',1)
        if len(ransomNote)>0:
            return False
        return True
        
