
# 'Zigzag Conversion' - Problem Reflections

### 2022-01-28
This medium was relatively simple. However, this was one that I overthought so it took me longer than it should have. The good news, is that the code is straight-forward with a minor exception for handling a case where we're only doing two rows (or less)

### What I did

Like I mentioned, I overthought this problem at first. I was thinking of different ways to go through the string and mathematically pop out the specific letters by index. I looped through the string and tried to do fancy modulo's, it made things complex and I kept having to re-think things after I got incorrect results. 

Finally, I gave up and rethought the problem from the beginning. This was another one where the base case was probably the easiest. I just went through the string and reproduced the conditions to print the zig-zag string (without necessarily printing things)I placed the letters in each row in a string in an array. That is, I would go through and when I found a letter that belonged in row 0, I would append the letter to a string I had in an array at position 0 (i.e. myStr[0] = mystr[0]) + myLetter). That worked fantastically and was so much simpler than my previous solutions.

I did run into an issue with the string "ABCD" and rows=2. To do my zig-zag algorithm, I made vertical columns the zig and diagonal columns the zag. To avoid confusion, any letter that could belong to a zig or zag, I considered a zig. This meant I had to have special handling for the last row of a zig and I had to have a condition to avoid my zag ending from a zig's start. The problem I had was that in this specific case (ABCD, 2), my zag was always out of bounds, so the letter "D" was getting inappropriately assigned. I added a condition to ensure that the zag wasnt out of bounds. 

With all this in mind, my solution has the following time complexities.
- O(n) - The main function loops through all the characters in the string once, for an O(n) operation. 


### What I would change

Maybe better clarify that one odd condition for my ABCD 2 case

### Take-Away's

I learned to initialize an empty array in python you can do: `myArray = [None] * 5`. I didn't end up using that because I haven't made up my mind whether I like that yet or not.
I also learned that you should always consider the base case! Do the simple thing first!

