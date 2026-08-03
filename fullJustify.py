from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0
        
        for word in words:
            # Check if adding this word exceeds width
            if line_len + len(line) + len(word) > maxWidth:
                # Format current line
                spaces = maxWidth - line_len
                gaps = len(line) - 1
                
                if gaps == 0:
                    # Single word → left justify
                    res.append(line[0] + " " * spaces)
                else:
                    space_per_gap = spaces // gaps
                    extra = spaces % gaps
                    
                    new_line = ""
                    for i in range(gaps):
                        new_line += line[i]
                        new_line += " " * (space_per_gap + (1 if i < extra else 0))
                    new_line += line[-1]
                    
                    res.append(new_line)
                
                # Reset for next line
                line = []
                line_len = 0
            
            line.append(word)
            line_len += len(word)
        
        # Last line → left justified
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
