from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_keys = {}
        anagram = []

        def _create_dict_keys(s:str, strs_keys:dict):
            if not strs_keys:
                strs_keys[s] = []
                return
            
            for n in strs_keys:
                if Counter(s) == Counter(n):
                    return
                
            strs_keys[s] = []          
                
        def _append_to_dict(s:str, strs_keys:dict):
            for i in strs_keys.keys():
                if Counter(s) == Counter(i):
                    strs_keys[i].append(s)
            
        for s in strs:
            _create_dict_keys(s, strs_keys)
            
        for s in strs:
            _append_to_dict(s, strs_keys)
            
        for i in strs_keys.values():
            anagram.append(i)

        return anagram

        