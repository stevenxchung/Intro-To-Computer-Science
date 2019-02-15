## Lesson 18: How Programs Run

In this lesson we will learn about how computer scientists measure cost, which is mostly about understanding how the resources needed to run a program scale with the size of its input. We'll also learn about implementing and using a hash table, a data structure that will massively improve the performance of our search engine.

### Algorithms
* Are made up of procedures or well-defined sequence of steps that can be executed mechanically
* Guaranteed to always finish and produce correct result

### Cost
* Generally we measure cost by evaluating the effect of increasing the size of the input on the efficiency of the algorithm
* Cost is focused on optimizing run-time and space

### Evaluating Time Execution
* We can time the execution of code by using the following script:

```python
import time
# Wil use time imports from the python library to give accurate times of code execution
# Will return the result as well as the run-time of any given code
def time_execution(code):
  start = time.clock()
  result = eval(code)
  run_time = time.clock() - start
  return result, run_time

# Can use spin_loop() to test want happens when we increase n by plugging spin_loop() into time_execution()
def spin_loop(n):
  i = 0
  while i < n:
    i += 1
```

### Faster Lookups
* Given a keyword
* Store in a hash table which has an id and value associated with each entry
* Often a hash table at a certain key has a *bucket* (array with and index) of entries, that way we can store more than one value at a key entry in the hash table, however this means that our efficiency becomes linear for those lookups

### Hash Function
* In Python we can use ord() to return a number which maps to some character, we can use chr() to transform a number back into that character

### Modulus Operator
* We can use the modulus operator to help us keep keys in a certain range so that our hash table is not too big

### Testing Hash Functions
* We can test the distribution of hash functions using the hash function test below:

```python
def test_hash_function(func, keys, size):
  results = [0] * size
  keys_used = []
  for w in keys:
    if w not in keys_used:
      hv = func(w, size)
      results[hv] += 1
      keys_used.append(w)
  return results
```

### Dictionaries
* Use keys to look up values
* Store data in a set of key-value pairs
* Similar to lists, they are mutable
* A faster way to build a hash table
