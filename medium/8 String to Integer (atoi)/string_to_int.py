from distutils.command.clean import clean


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        cleanStr = ""
        isPositive = None
        hitFirstNonZero = False
        hitFirstDigits = False
        for i in range(0, len(s)):
            character = s[i]
            if not character.isdigit():
                if isPositive == None and not hitFirstDigits:
                    if character == "+":
                        isPositive = True
                    elif character == "-":
                        isPositive = False
                    else:
                        break
                else:
                    break
            else:
                if isPositive == None:
                    isPositive = True
                if character == "0" and not hitFirstNonZero:
                    pass
                else:
                    hitFirstNonZero = True
                    cleanStr = cleanStr + character

        if len(cleanStr) == 0:
            return 0

        two_magnitude_31_minus1 = "2147483647"
        neg_two_magnitude_31 = "2147483648"
        if len(cleanStr) > len(two_magnitude_31_minus1):
            if isPositive:
                return int(two_magnitude_31_minus1)
            else:
                return -1 * int(neg_two_magnitude_31)

        if len(cleanStr) < len(two_magnitude_31_minus1):
            if isPositive:
                return int(cleanStr)
            else:
                return -1 * int(cleanStr)
            
        for i in range(0, len(neg_two_magnitude_31)):
            maxDigit = neg_two_magnitude_31[i]
            myDigit = cleanStr[i]

            if i == len(neg_two_magnitude_31) - 1:
                if not isPositive:
                    if int(myDigit) > int(neg_two_magnitude_31[i]):
                        return -1 * int(neg_two_magnitude_31)
                else:
                    if int(myDigit) > int(two_magnitude_31_minus1[i]):
                        return int(two_magnitude_31_minus1)

            if int(myDigit) > int(maxDigit):
                if isPositive:
                    return int(two_magnitude_31_minus1)
                else:
                    return -1 * int(neg_two_magnitude_31)
            
            if int(myDigit) < int(maxDigit):
                break

        if not isPositive:
            cleanStr = "-" + cleanStr

        number = int(cleanStr)

        return number
