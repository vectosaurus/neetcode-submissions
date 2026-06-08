invariant = """
iterate over each position and see how many words
including that position have until now have words matching the criteria. for the ranges in queries, 
simply subtract the counts at those positions to get the answer
"""

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        summr = {}
        summr[0] = 0
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i, word in enumerate(words, start=1):
            if (word[0] in vowels) and (word[-1] in vowels):
                count += 1
            summr[i] = count
        print(summr)
        counts = []
        for q_start, q_end in queries:
            counts.append(summr[q_end+1]-summr[q_start])
        return counts

