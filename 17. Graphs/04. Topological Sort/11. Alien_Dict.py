"""
269. Alien Dictionary
Hard


There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
sorted lexicographically
by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.


"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Do the following
        1. first try to build the adjency list for the words 
        2. To do the above, take the words in the order presented and find the connections
        3. Then build the indegree counter, rebuild the topological sorted order
        """
        from collections import defaultdict, deque

        if not words:
            return ""
        adj_mapper = defaultdict(list)
        seen_chars = set([])

        prev = words[0]
        curr = None
        _ = [seen_chars.add(c) for c in words[0]]
        for word in words[1:]:
            curr = word
            # find the first character position of difference
            prev_len = len(prev)
            curr_len = len(curr)
            if prev==curr:
                continue
            counter = 0
            min_len = min(prev_len, curr_len)
            _ = [seen_chars.add(c) for c in word]
            while counter < min_len:
                if prev[counter] != curr[counter]:
                    adj_mapper[prev[counter]].append(curr[counter])
                    break
                counter += 1
            if counter == min_len and counter == curr_len:
                return ""
            prev = curr
        
        indegree_counter = [0 for _ in range(27)]
        for char in adj_mapper:
            for neighbor in adj_mapper[char]:
                char_pos = ord(neighbor) - ord("a")
                indegree_counter[char_pos] += 1
        
        queue = deque([])
        for char in seen_chars:
            char_pos = ord(char) - ord("a")
            if indegree_counter[char_pos] == 0:
                queue.append((char_pos, char))
        
        topo_chars = []
        while queue:
            char_pos, char = queue.pop()
            topo_chars.append(char)
            for neighbor in adj_mapper[char]:
                new_char_pos = ord(neighbor) - ord("a")
                indegree_counter[new_char_pos] -= 1
                if indegree_counter[new_char_pos] == 0:
                    queue.append((new_char_pos, neighbor))
        print(f"Topo chars :: {topo_chars}")
        print(f"Seen chars :: {seen_chars}")
        if len(topo_chars) == len(seen_chars):
            return "".join(topo_chars)
        return "" 

        

        




