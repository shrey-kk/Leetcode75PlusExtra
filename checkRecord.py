class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count=0
        late_count=0
        for day in s:
            if day=="P":
                late_count=0
                continue
            elif day=="L":
                late_count+=1
            elif day=="A":
                absent_count+=1
                late_count=0
            if absent_count>1 or late_count>2:
                return False
        return True
            

                
            
            

        
