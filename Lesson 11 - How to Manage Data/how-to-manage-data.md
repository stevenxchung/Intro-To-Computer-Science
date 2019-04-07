## Lesson 11: How to Manage Data

In this lesson we will look at structured data and build a simple web crawler.

### Nested Lists
So far, all of the elements in our lists have been of the same type: strings, numbers, etc. However, there are no restrictions on the types of elements in a list. Elements of a list can be any type you want, you can also mix and match different types of elements in a list.

* An example of a nested list:
```python
mixed_up = ['apple', 3, 'oranges', 27, [1, 2, ['alpha', 'beta']]]
```
### Mutation
**Mutation** means changing the value of an object. Lists support mutation. This is the second main difference between strings and lists.

* Lists can be mutated, thus changing the value of an existing list. Here is a list:
```python
p = ['H', 'e', 'l', 'l', 'o']
```

* Mutate a list by modifying the value of its elements:
```python
p[0] = 'Y'
```

* This expression replaces the value in position 0 of p with the string 'Y'. After the assignment, the value of p has changed:
```python
print(p)
['Y', 'e', 'l', 'l', 'o']

p[4] = '!'
print(p)
['Y', 'e', 'l', 'l', '!']
```

### Aliasing
Now that you know how a mutation modifies an existing list object, you will really be able to see how this is differs from strings when you introduce a new variable:

```python
p = ['H', 'e', 'l', 'l', 'o']
p[0] = 'Y'
q = p
```

* Suppose we use an assignment statement to modify one of the elements of q:
```python
q[4] = '!'
```

* This also changes the value of p:
```python
print p
['Y', 'e', 'l', 'l', '!']
```

* After the **q = p** assignment, the names p and q refer to the same list, so anything we do that mutates that list changes that value both variables refer to

* It is called aliasing when there are two names that refer to the same object. **Aliasing** is very useful, but also can be very confusing since one mutation can impact many variables. If something happens that changes the state of the object, it affects the state of the object for all names that refer to that object

* **Strings are Immutable**. Note that we cannot mutate strings, since they are immutable objects. Try mutating a string in the interpreter: #!highlight python s = 'Hello' s[0] = 'Y' 'str' object does not support item assignment } **Mutable and Immutable Objects**. The key difference between mutable and immutable objects, is that once an object is mutable, you have to worry about other variables that might refer to the same object. You can change the value of that object and it affects not just variable you think you changed, but other variables that refer to the same object as well

### List Operations
There are many built-in operations on lists. Here are a few of the most useful ones here.

* **Append**. The append method adds a new element to the end of a list. The append method mutates the list that it is invoked on, it does not create a new list. The syntax for the append method is: `<''list''>.append(<''element''>)`

* **Concatenation**. The + operator can be used with lists and is very similar to how it is used to concatenate strings. It produces a new list, it does not mutate either of the input lists: `<''list''> + <''list''> → <''list''>`

* Length. The **len** operator can be used to find out the length of an object. The **len** operator works for many things other than lists, it works for any object that is a collection of things including strings. The output from **len** is the number of elements in its input: `len(<''list''>) → <''number''>`

### How Computer Store Data
In order to store data you need two things: 
  * (1) something that preserves state
  * (2) a way to read its state. Our storage mechanism needs to have more than one state, but two states is enough. We can think about this like a light switch, which is connected to a light bulb through some power source. When you turn the light switch on, the light bulb turns on:

* Flipping the switch changes the state of the light bulb. The light bulb has two different states: it can be on or off. This is what we need to store one bit of data. A **bit** is the fundamental unit of information. One bit is enough to decide between two options (for example, on or off for the light bulb). If you had enough light bulbs you could store many bits, which would be enough to be able to store any amount of digital data

* In addition to something that can change state, to read memory you also need something that can sense the state. In terms of a light bulb, that could be an eye or a light sensor, which could see if the light bulb was on or off. This is very similar to the way computers store data, but computers use much less energy and much less space than a light bulb to store one bit

* The fastest memory in your computer works like a switch. Data that is stored directly in the processor's memory, which is called the **register**, is stored like a switch, which makes it very fast to change and read its state. However, a register is like a light bulb in that when you turn the power off, you lose the state. This means that all the data stored in registers is lost when the computer is turned off

* Another way that computers store data is similar to a bucket. We could represent a one by a full bucket and represent a zero with an empty bucket. To check the state of the bucket, we could weigh the bucket or look at it to figure out whether it is full or empty

* The difference between buckets and light bulbs is that buckets leak a little, and water evaporates from the bucket. If you want to store data using a bucket, it will not last forever. Eventually, when all the water evaporates you will be unable to tell the difference between a zero and a one. Computers solve this problem using the digital abstraction. There are infinitely many different amount of water that could be in the bucket, but they are all mapped to either a 0 or a 1 value. This means it is okay if some water evaporates, as long as it does not drop below the threshold for representing a 1

* In computers, the buckets are holding electrons instead of water, and we call them **capacitors**. The memory in your computer that works this way is called **DRAM**

### DRAM
* A gigabyte means approximately a billion bytes. One byte is 8 bits

* A gigabyte is actually 2^30 bytes. This is very close to one billion, but in computing it is usually more convenient to use powers of two

* In Python, the exponentiation operator is denoted with two asterisks: `<''base''> ** <''power''> → <''base''><''power''>`

* Kilobytes, megabytes, gigabytes, and terabytes are the main units we use to talk about computer memory

* There are many different types of memory inside your computer, for example, registers, that were mentioned earlier as the fastest memory that is built right into the processor. What distinguishes different types of memory is the time it takes to retrieve a value (this is called **latency**), the cost per bit, and how long it retains its state without power

* For DRAM, the latency is about 12 nanoseconds (recall that there are one billion nanoseconds in a second). The cost of the 2 GB DRAM show is about 10 USD (approximately 7 euros)

### Hard Drives
Another type of memory in your computer is a **hard drive**. Inside the hard drive there are several disks that spin. The disks store data magnetically, and there is a read-head that can read data from the disks as well as write new data from the disk. Compared to DRAM, this is a very slow way of storing data since it involves spinning a physical disk and moving a read head, but it can store data for far less cost than DRAM. The other advantage of storing data on a hard drive is that it persists. The data is not lost even when the power is turned off.

* Where our DRAM was two gigabytes, this hard drive can store one terabyte, which is 500 times as much memory. A terabyte is close to a trillion bytes. This is enough memory to store about 100 hours of high quality video

* The latency for a hard drive is much higher than it is for DRAM. This is because the hard drive is moving physical things. It operates using disks, so you have to wait for the disk to spin and reach the read-head. Also, if the disk isn't in the right place then you might have to wait for the read-head to move. The average latency for a hard drive is about seven milliseconds (1 millisecond = 1/1000 of a second = 1 million nanoseconds).

### For Loops
In Python there is a more convenient way to loop through the elements of a list: the for loop. The syntax looks like this:
```python
for <''name''> in <''list''>:
  <''block''>
```

### Pop
The pop operation mutates a list by removing its last element. It returns the value of the element that was removed.
```python
<''list''>.pop() → element
```
