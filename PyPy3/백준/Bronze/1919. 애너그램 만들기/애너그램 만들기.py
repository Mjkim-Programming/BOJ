from collections import Counter
    
word1 = input()
word2 = input()

count1 = Counter(word1)
count2 = Counter(word2)
    
all_chars = set(count1.keys()) | set(count2.keys())
    
deletions = 0
for ch in all_chars:
    deletions += abs(count1.get(ch, 0) - count2.get(ch, 0))
        
print(deletions)