## Lesson 22: How to Have Infinite Power

This unit introduces what I think is the most fascinating and powerful idea in all of computing - recursive definitions. Understanding them requires some mind-bending gymnastics, but once you do, you will find elegant and powerful new ways to think about nearly all problems you encounter.

### Recursive Definitions
* There are generally two parts to the recursive definition:
  * Base case - a starting point, not defined in terms of itself and has the smallest input
  * Recursive case - defined in terms of *smaller* version of itself

### Recursive Procedures
Let's define a recursive procedure factorial(n) = n * (n-1) * (n-2) * ... * 1, where the second term to the nth term up to 1 is recursive
* The expression factorial(0) = 1 is the base case
* The expression factorial(n) = n * factorial(n-1) is the recursive case

### Recursive vs Iterative
Let's look at two ways to solve the palindrome problem:

* Recursive:
```python
def is_palindrome(s):
    if s == '':
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
```

* Iterative:
```python
def iter_palindrome(s):
    for i in range(0, len(s)/2):
        if s[i] != s[-(i + 1)]:
            return False
    return True
```

* As shown, the recursive solution is more readable than the iterative solution, this is sometimes an advantage to the programmer

### Divide and Be Conquered
As we saw in the bunnies quiz, as the input gets bigger, the number of times fibonacci is called increases exponentially:

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # The run-time efficiency here exponential, there is a better way to address this as we will see
```

### Page Rank
How do we measure page rank?
  * We randomly follow a path through many different web pages, whichever web page is hit the most is the most popular web page and consequently the web page which is hit the least is the least popular
  * We can measure page rank as the probability we will hit a specific web page when randomly navigating the web

We can define the page rank algorithm as follows:
  * Base case: rank(0, url) = 1/nPages
  * Recursive: rank(t, url) = (1 - d)/nPages + SUM(d * rank(t - 1, p)/(n outlinks from p))
    * p - inlinks to url
    * d - damping
    * ranks - ranks at time t - 1
    * new ranks - ranks at time t
