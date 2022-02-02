class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # simplest case
        if len(s) == 0: return 0
        
        longestSubstr = ""
        tempLongest = ""
        for i in range(0, len(s)):
            currentChar = s[i]
            tempLongest = self.getFirstNonrepeatingSubstr(s[i:])
            if len(tempLongest) > len(longestSubstr):
                longestSubstr = tempLongest

        return len(longestSubstr)     

    def getFirstNonrepeatingSubstr(self, s: str) -> str:
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s
        nonrepeating = ""
        for i in range(0, len(s)):
            current_char = s[i]
            if current_char in nonrepeating:
                return nonrepeating
            else:
                nonrepeating = nonrepeating + current_char
        return nonrepeating


        

                
            
            
            
                
        