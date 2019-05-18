## Lesson 25: Q&A

### Pythonic
*Q: What does it mean to be Pythonic?*
A: It means to implement a solution to a problem in a clever way by leveraging Python's syntax, however some of these solutions are not easily readable for beginners.

### Python Versions
*Q: Why are we using Python 2 in this class if there is Python 3, is what we are learning already outdated?*
A: Syntactically, Python 2 is a little outdated (there are only subtle differences between Python 2 and Python 3), however the main concepts of Computer Science remain the same no matter what programming language is used.

### Using Recursion
*Q: When would we use recursion to solve a problem versus using a while loop?*
A: Generally, using a while loop is more efficient since there is no overhead of calling a function again and again, however some solutions are simpler to solve with recursion (makes code more readable as well), one must evaluate the trade-offs depending on the problem.

### Recursion in Other Languages
*Q: Could recursive calls be more efficient than iterative calls in some programming languages?*
A: The problem with recursive calls is that you need a new stack frame to keep track of each recursive call, once the solution is found, the function now has to go back through each case to produce the answer and this takes too much space. There are ways to optimize the recursive call however, languages like Lisp and Scheme that optimize the way recursive calls are handled but iterative calls are still more space-efficient.

### Page Rank
*Q: How much different is the Page Rank algorithm discussed in this class versus the algorithm used by Google?*
A: The Page Rank algorithm discussed in this class is actually not too different than the one used by Google, however the algorithm they use today is a lot more complicated and massive in size.

### Challenges in Search
*Q: What are the major problems search engines are trying to solve today?*
A: Search engines are continuing to improve their search algorithm and find ways to respond to queries that are more complex, there is a lot of controversy between sites and page ranking that we have to keep in mind when adjusting the ranking algorithm.

### International Characters
*Q: How does a search engine address searching in a different language?*
A: Headers in web pages identify what language a website is using, there a many ways to use those headers to optimize our search algorithm to return what we want.
