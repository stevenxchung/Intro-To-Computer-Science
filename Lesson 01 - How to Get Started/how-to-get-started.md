## Lesson 1: How to Get Started

A web crawler is a program that collects content from the web. A web crawler finds web pages by starting from a seed page and following links to find other pages, and following links from the other pages it finds, and continuing to follow links until it has found many web pages.

### What is Programming?
* **Programming** is the core of computer science
* A **computer** is a machine that can execute a program. With the right program, a computer can do any mechanical computation you can imagine
* A **program** describes a very precise sequence of steps. Since the computer is just a machine, the program must give the steps in a way that can be executed mechanically. That is, the program can be followed without any thought
* A **programming language** is a language designed for producing computer programs. A good programming language makes it easy for humans to read and write programs that can be executed by a computer
* **Python** is a programming language. The programs that we write in the Python language will be the input to the Python interpreter, which is a program that runs on the computer. The Python interpreter reads our programs and executes them by following the rules of the Python language

### Grammar
Compared to a natural language, programming languages adhere to a strict grammatical structure. In English, even if a phrase is written or spoken incorrectly, it can still be understood with the help of context or other cues. On the other hand, in a programming language like Python, the code must match the language grammar exactly. The Python interpreter has no idea what to do with input that is not in the Python language, so it produces an error.

**Basic English Grammar Rules**:

* Sentence → Subject Verb Object
* Subject → Noun
* Object → Noun
* Verb → **Eat**
* Verb → **Like**
* Noun → **I**
* Noun → **Python**
* Noun → **Cookies**

* When programming language grammar is not followed the interpreter will return a **SyntaxError** message. This means that the structure of the code is inconsistent with the rules of the programming language

### Backus-Naur Form
The notation we used to describe the grammar is known as **Backus-Naur Form**, which was introduced in the 1950s by John Backus, the lead designer of the Fortran programming language at IBM.

* The purpose of Backus-Naur Form is to describe a programming language in a simple and concise manner. The structure of this form is:
* <Non-Terminal> → replacement
* The replacement can be any sequence of zero or more non-terminals or terminals
* **Terminals** never appear on the left side of a rule. Once you get to a terminal there is nothing else you can replace it with

### Python Expressions
An **expression** is something that has a value. Here are some examples of expressions in Python:
```python
3
1 + 1
7 * 7 * 24 * 60
```

### Processors
* A **processor** is the part of the computer that carries out the steps specified in a computer program. Sometimes people call the processor the "central processing unit" or CPU
* A processor has to be small to execute programs quickly. If your computer's processor were any larger than the size of a dollar bill, then you couldn't even send light from one end of the processor to the other before finishing the execution of a single step in a program

### Grace Hopper
* Grace Hopper was a pioneer in computing who was known for walking around with nanosticks. Nanosticks are pieces of wire that are the length light travels in a nanosecond, about 30 cm
* Hopper wrote one of the first programming languages, COBOL, which was for a long time the world's most widely used programming language. Hopper built the first compiler. A compiler is a program that takes as input a program in a programming language easy for humans to write and outputs a program in another language that is easier for computers to execute. The difference between a compiler and an interpreter like Python is that a compiler does all the work at once and creates a new program, whereas, the interpreter converts the source code one step at a time as the program runs
* When Grace Hopper started building the first compiler, most people did not believe it was possible for a computer program to produce other computer programs: "Nobody believed that I had a running compiler and nobody would touch it. They told me computers could only do arithmetic

### Variables
* A **variable** is a name that refers to a value. In Python, we can use any sequence of letters and numbers and underscores (_)when we want to make a variable name, so long as it does not start with a number. Here are some examples of valid variable names:

### Strings
* A **string** is a sequence of characters surrounded by quotes, either single or double.
```python
'I am a string!'
```

### Ada
* Augusta Ada King, Countess of Lovelace, 1815-1852, was arguably the world's first computer programmer. Grace Hopper wasn't the first person to think about using computers to do things other than arithmetic, but Ada probably was
* It might act upon other things besides number, were objects found whose mutual fundamental relations could be expressed by those of the abstract science of operations, and which should be also susceptible of adaptations to the action of the operating notation and mechanism of the engine...
* The "it" King is referring to is the Analytical Engine, a mechanical programmable computer that Charles Babbage designed. Although he did not succeed in building it in the 1840s, he did have a design for it, which Ada was thinking about programming to compose music

### Strings and Numbers
We can also use the plus operator (+) on strings, but it has a different meaning from when it is used on numbers. With string, plus means **concatenation**.

* `<string> + <string>` → outputs the concatenation of the two strings

### Indexing Strings
When you want to select sub-sequences from a string, it is called indexing. Use the square brackets [] to specify which part of the string you want to select: `<string>[<expression>]`

### Selecting Sub Sequences
You can select a sub-sequence of a string by designating a starting position and an end position. Python reads the characters positions starting at 0, so that if you consider the string 'udacity,' that has 7 characters, there are 7 positions: 0,1...6, with 'u' being in the 0 position.

* `<string>[<expression>]` → a one-character string
* `<string>[<start expression>:<stop expression>]` → a string that is a sub-sequence of the characters in the string, from the start position up to the character before the stop position. If the start expression is missing, the sub-sequence starts from the beginning of the string; if the stop expression is missing, the sub-sequence goes to the end of the string

### Finding Strings in Strings
The find method is a built in operation, or method, provided by Python, that operates on strings. The output of find is the position of the string where the specified sub-string is found.

* `<search string="">.find(<target string="">)`
* If the target string is not found anywhere in the search string, then the output will be -1

### Find with Number
In addition to passing in a target string to find, you can also pass in a number:

* `<search string="">.find(<target string="">, <number>)`
* The number input is the position in the search string where find will start looking for the target string. So, the output is a number giving the position of the first occurrence of the target string in the search string at, or after the input position. If there is no occurrence at or after that position, the output is -1

### Extracting Links
A **web page** is really just a long string of characters. Your **browser** renders the web page in a way that looks more attractive than just the string of characters. You can view the string of characters for any web page in your browser. How to do this depends on the browser you are using. For Chrome and Firefox, right-click anywhere on the page that is not a link and select "View Page Source". For Internet Explorer, right-click and select "View Source".
