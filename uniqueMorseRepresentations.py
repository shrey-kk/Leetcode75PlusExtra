from collections import deque
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha_to_idx={char:idx for idx,char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        morse_chars=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_to_idx={idx:char for idx,char in enumerate(morse_chars)}
        visited=set()
        for word in words:
            string=deque()
            for char in word:
                string.append(morse_to_idx[alpha_to_idx[char]])
            visited.add("".join(string))
        return len(visited)
