from collections import Counter

def count_palindrome_pairs(parent, s):
    counter = 0
    n = len(parent)
    paths = [[] for _ in range(n)]
    
    for i in range(1, n):
        paths[i] = paths[parent[i]] + [s[i]]
        
    for i in range(n):
        for j in range(i+1, n):
            path = Counter(paths[j] + paths[i])
            odd = sum(v % 2 for v in path.values())
            if odd <= 1:
                counter += 1
                
    return counter