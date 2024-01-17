class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences_map = {}
        
        for num in arr:
            occurrences_map[num] = occurrences_map.get(num, 0) + 1
        
        unique_occurrences_set = set(occurrences_map.values())
        
        return len(unique_occurrences_set) == len(occurrences_map)