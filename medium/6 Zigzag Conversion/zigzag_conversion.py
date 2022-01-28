class Solution:
    def convert(self, s: str, numRows: int) -> str:

        rowStrs = []
        currentZigRow = 0
        currentZagRow = numRows - 2
        for i in range(0, len(s)):
            if currentZigRow < numRows:
                print(f"zig {currentZigRow}")
                # down (zig)
                if len(rowStrs) > currentZigRow:
                    rowStrs[currentZigRow] = rowStrs[currentZigRow] + s[i]
                else:
                    rowStrs.append(s[currentZigRow])
                currentZigRow = currentZigRow + 1
            elif currentZagRow > 1:
                print(f"zag {currentZagRow}")
                # diagonal (zag)
                rowStrs[currentZagRow] = rowStrs[currentZagRow] + s[i]
                currentZagRow = currentZagRow - 1
            else:
                print(f"finish {currentZigRow}:{currentZagRow}")
                # finish last zag, then restart with zig
                rowStrs[currentZagRow] = rowStrs[currentZagRow] + s[i]
                currentZigRow = 0
                currentZagRow = numRows - 2
                if currentZagRow == 0:
                    # this is the case where the zag was the zig
                    # that is, if we reset to zig without zagging
                    currentZigRow = 1

        output = "".join(rowStrs)
        return output
