
# 'Longest Substring Without Repeating Characters' - Problem Reflections

### 2021-05-02
This was a bit more of an involved medium. The problem concept wasn't complex but reasoning through the looping required thought. Splitting off part of the problem to a separate function made the reasoning much easier. I think my solution looks nice and is easy to reason against, but I think there might be a faster solution. At some point I may revisit this to find it

### What I did

To solve the problem, I started at the beginning of the string and looped through it. For each character I encountered, I found 'that character's longest non-repeating substring'. I made a method out of that idea so it could live in isolation. I left the responsibility of comparing the longest substring and the 'discovered' substring to the main function. I'm pretty happy with the separation of concerns in this problem. After reflecting on this problem and some other functions I've written professionally I want to remember to maintain that idea of using small functions to isolate ideas. If you've heard of S.O.L.I.D principles, this idea is the 'S' the 'Single Responsibility Principle'. Its a good idea and I really like it, but sometimes I get caught in the weeds of implementing the thing I'm developing and don't take time to reflect and simplify. 

With all this in mind, my solution has the following time complexities.
- O(n log n) - The main function loops through all the characters in the string, for an O(n) operation. For each of those characters I also loop through the substring's characters. That substring loop will progressively get smaller for each iteration.


### What I would change

I think the solution could be faster so I would try to re-think another algorithm to use.

### Take-Away's

Despite trying to remember the syntax for looping through a string. I forgot it again so I had to look it up from my old code. Hopefully if I do this enough I'll remember it. 

Its always a good to break down the problem. I initially wrote this code as one big function. I had an error that was hard to think through, so I broke down the problem into separate functions to de-complexify the problem. It ran successfully my first time after that.

