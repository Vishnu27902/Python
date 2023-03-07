from collections import Counter
s1="nameless"
s2="salesmen"

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    return Counter(s1)==Counter(s2)
print(anagram(s1,s2))