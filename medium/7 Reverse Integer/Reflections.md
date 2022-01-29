
# 'Reverse Integer' - Problem Reflections

### 2022-01-29
This medium was pretty easy. The only issues I ran into with this problem were dealing with the '0' case, abiding by the constraints, and python syntax.

### What I did

This problem was easy, and reflecting on it now, I could have made my solution even simpler. My process, at its core, to convert the int to a string so I could iterate through it easier, iterate through the string in reverse order putting the reversed letters on another string, and finally converting the reversed string to an integer. There were some edge cases to consider though. Negative numbers didnt reverse well, the negative sign ('-') always had to be on the left of the reversed string. I added special handling for that. Numbers that ended in 0's should not have their reversed number start with zeros. I added special handling for that. As I mentioned there were three minor details that slowed me down.

First, the '0' case. Since my handling dealt with zero's on the ends of numbers, and a single zero has a zero at its beginning and end, I was removing the whole number! Luckily this was only one case in all of numbers, so it was very easy to write an if statement to account for it.

Second, when the reversed number was smaller than -2^31 or bigger than 2^31-1 then I had to return 0. This wasnt as striaght forward since I can't say whether someone would be running this on a 32bit or 64bit interpreter and whether the int would be 32 bits or 64. If it was 32 bits, I couldnt exactly convert my string to an int to **then** try to compare it. I had to do a comparison manually. That is, compare the length of the string representation of the numbers, then compare each digit (from most significant to least significant) to see if it was within range. It was a bit of an annoying constraint, but I understand why its there and writing the code wasn't terrible.

Last, I still have to Google Python syntax from time to time. Things that I didn't know off the top of my head were: 
- making substrings from strings
- doing a for loop in reverse

I also could have simply used python's built in 'reverse' function to reverse my string rather than for-looping through it, but again, I didn't have that method memorized.

Regardless, the problem was still pretty easy to go through and get right. With all this in mind, my solution has the following time complexities.
- O(n) best case - The main function loops through all the characters in the string representation of the number once, for an O(n) operation. 
- O(2n) (reduces to O(n)) worst case - The main function loops through all the characters in the string representation of the number once, for an O(n) operation, if the number is right on the edge of being out of bounds, it must be manually compared to the out of bounds number

### What I would change

Try and use pythons built-in reverse function to make the code simpler

### Take-Away's

There's still a couple python syntax things I need to keep up with

