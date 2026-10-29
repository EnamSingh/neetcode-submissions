class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angraMap = {} # key = sorted version of word / Value = list of words that matched the sorted version

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in angraMap:
                angraMap[sortedWord] = []
            
            angraMap[sortedWord].append(word)
        
        return list(angraMap.values())