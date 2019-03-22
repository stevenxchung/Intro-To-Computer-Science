## Lesson 5: How to Repeat

The next step towards building your search engine is to extract all of the links from a web page. In order to write a program to extract all of the links, you need to know these two key concepts: procedures and control.

* **Procedures** - a way to package code so it can be reused with different inputs
* **Control** - a way to have the computer execute different instructions depending on the data (instead of just executing instructions one after the other)

In this unit, you will learn three important programming constructs: procedures, **if statements**, and **while loops**. Procedures, also known in Python as “functions,” enable you to abstract code from its inputs; if statements allow you to write code that executes differently depending on the data; and while loops provide a convenient way to repeat the same operations many times. You will combine these to solve the problem of finding all of the links on a web page.

### Motivating Procedures
**Procedural abstraction** is a way to write code once that works on any number of different data values. By turning our code into a procedure, we can use that code over and over again with different inputs to get different behaviors.

### Introducing Procedures
* A procedure takes in inputs, does some processing, and produces outputs

* For example, the **+** operator is a procedure where the inputs are two numbers and the output is the sum of those two numbers. The **+** operator looks a little different from the procedures we will define since it is built-in to Python with a special operator syntax. In this unit you will learn how to write and use your own procedures

* Here is the Python grammar for writing a procedure:
```python
def <name>(<parameters>):
  <block>
```

* The keyword **def** is short for “define”
* `<name>` is the name of a procedure. Just like the name of a variable, it can be any string that starts with a letter and followed by letters, number and underscores

* `<parameters>` are the inputs to the procedure. A parameter is a list of zero or more names separated by commas: `<name>, <name>,...` Remember that when you name your parameters, it is more beneficial to use descriptive names that remind you of what they mean. Procedures can have any number of inputs. If there are no inputs, the parameter list is an empty set of closed parentheses: ()

* After the parameter list, there is a : (colon) to end the definition header. The body of the procedure is a `<block>`, which is the code that implements the procedure. The block is indented inside the definition. Proper indentation tells the interpreter when it has reached the end of the procedure definition

### Return Statement
* A **return** statement can have any number of expressions. The values of these expressions are the outputs of the procedure

* A **return** statement can also have no expressions at all, which means the procedure procedures no output. This may seem silly, but in fact it is quite useful. Often, we want to define procedures for their side-effects, not just for their outputs. Side-effects are are visible, such as the printing done by a print statement, but are not the outputs of the procedure

### Using Procedures
In order to use a procedure, you need the name of the procedure, followed by a left parenthesis, a list of the procedure’s inputs (sometimes called operands or arguments), closed by right parenthesis:

`<procedure>(<input>,<input>, …)`

* Think of procedures as mapping inputs to outputs. This is similar to a mathematical function. Indeed, many people call procedures in Python like the ones we are defining “functions”. The reason I prefer to call them procedures is that they are quite different from mathematical functions. The main differences are:
  * A mathematical function always produces the same output given the same inputs. This is not necessarily the case for a Python procedure, which can produce different outputs for the same inputs depending on other state (we will see examples in Unit 3). 
  * A mathematical function is a pure abstraction that has no associated cost. The cost of executing a Python procedure depends on how it is implemented. (We will discuss how computer scientists think about the cost of procedures in Unit 5.)
  * A mathematical function only maps inputs to outputs. A Python procedure can also produce side-effects, like printing.
* Procedures are a very important concept and the core of programming is breaking problems into procedures, and implementing those procedures.

### Equality Comparisons
Python provides several operators for making comparisons:
* `< less than`
* `> greater than`
* `<= less than or equal to`
* `== equal to`
* `!= not equal to`

* All of these operators act on numbers, for example:
  * `<number> <operator> <number>`
* The output of a comparison is a **Boolean: True** or **False**

### If Statements
An **if statement** provides a way to control what code executes based on the result of a test expression. Here is the grammar of the if statement:
```python
if <TestExpression>:
  <block>
```

* In this statement, the code in the `<block>` runs only if the value of the test expression is True. Similar to procedures, the end of the if statement block is determined by the indentation.

### Or
An **or** expression gives the logical or (disjunction) of two operands. If the first expression evaluates to **True**, the **value** is True and the second expression is not evaluated. If the value of the first expression evaluates to **False** then the value of the **or** is the value of the second expression:

* `<Expression> or <Expression>`

### While Loops
**Loops** are a way of executing something over and over.

* The syntax for the **while** loop is very similar to the **if** statement:
```python
while <TestExpression>:
  <Block>
```
* In contrast to an **if** statement where the block executes either 0 or 1 times depending on whether the test expression is **True** or **False**, a while loop executes any number of times, continuing as long as the test expression is **True**

### Break
**Break** gives us a way to break out of a loop, even if the test condition is true. The typical structure of the loop with a break looks like this:
```python 
while <TestExpression>:
  <Code>
    if <BreakTest>:
      break # stop executing the while loop
    <More Code>
<After While>
```
* The **break** statement jumps out of the loop to `<After While>`
