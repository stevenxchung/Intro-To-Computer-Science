## Lesson 21: Q&A

### Hash Tables
*Q: How does Python determine how many buckets a dictionary has as it grows?*
A: For a typical hash function the goal is to keep the load factor below 1. For Python's dictionary implementation, if the number of keywords is greater than 2/3 of the hash table size, the table is resized.

### Rehashing
*Q: Keeping users in mind in a real-world scenario, how should one roll-out a new rehashed table without shutting down services?*
A: There are many things to keep in mind such as what happens if data is added during rehashing? One strategy is to make a copy of the hash table on another computer, and once rehashing is complete on that computer then do the roll-over.

### Importing Libraries
*Q: How do imports work in Python?*
A: Imports are a way Python refers to another set of code (mostly reusuable code) which may have been developed by other users. This allows us to abstract away details and keep our main code clean.

### Programming Literacy
*Q: What if everyone was programming literate?*
A: If everyone was programming literate, perhaps the world would be more efficient (think about all the repetitive things in life which could be automated by machines).
