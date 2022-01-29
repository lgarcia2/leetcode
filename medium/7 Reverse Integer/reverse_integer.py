class Solution:
    def reverse(self, x: int) -> int:
        # special case
        if x == 0:
            return "0"

        # if number is negative, pop the '-' sign and tack it on the reversed str later
        xstr = f"{x}"
        negative = False
        if x < 0:
            negative = True
            xstr = xstr[1:len(xstr)]

        hitFirstNonZero = False
        reversedStr = ""
        for i in range(len(xstr)-1, -1, -1):
            if xstr[i] != "0":
                hitFirstNonZero = True
                reversedStr = reversedStr + xstr[i]
            if xstr[i] == "0" and hitFirstNonZero:
                reversedStr = reversedStr + xstr[i]

        # handle out of bounds
        max32IntStr = "2147483648"
        if len(reversedStr) > len(max32IntStr):
            return 0
        if len(reversedStr) == len(max32IntStr):
            for i in range(len(reversedStr)):
                if int(reversedStr[i]) < int(max32IntStr[i]):
                    break
                elif int(reversedStr[i]) > int(max32IntStr[i]):
                    return 0

        # handle negative numbers
        if negative:
            reversedStr = "-" + reversedStr

        return int(reversedStr)