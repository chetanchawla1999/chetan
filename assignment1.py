## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
Python is a high-level programming language that is known for its ease of readability. 
Python’s syntax is designed to be easy to read and understand resulting in fewer coding steps for developers than imposed by Java or C++. 
This makes it a great choice for beginners who are just starting to learn programming. 
Python is also portable, meaning that it can run on any platform, including Windows, Mac, Linux, and even Raspberry Pi. 
In addition, Python supports development in AI which is a rapidly growing field, and Python is a language that is well-suited for development in this area. 
With its high level of readability and portability, Python is an excellent choice for high-level programming.

Q2. Why is Python called a dynamically typed language?
Basically dynamically typed means we have to define the datatypeof the variable but in python we don't have to do that because in python, compiler
automatically identifies the type of the variable so we don't have to dyna,ically define the type of the variable.


Q3. List some pros and cons of Python programming language?
PROS:
--> It is a high level programming language so it is Easy to understand.
--> It is a dynamically typed programming language.
--> Python is an interpreted language.


CONS:
--> Python has speed limitations.
--> Python can have runtime errors.
--> Python consumes a lot of memory space. 

Q4. In what all domains can we use Python?
--Data Science
--Automation
--AI/ Machine Learning
--Application Development
--Console applications

Q5. What are variable and how can we declare them?
Variables are the basic unit of storage in a programming language. These variables consist of a data type, the variable name, and the value to be assigned to the variable.
For eg. x='Python'
This is a string variable.

Q6. How can we take an input from the user in Python?
x=input("Enter the input")

Q7. What is the default datatype of the value that has been taken as an input using input() function?
Default datatype will be string. 

Q8. What is type casting?
When we converts one type of variable into another type of variable then it is called type casting.
for eg- x='123'
y=int(x)

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Yes, We can input more than one value from the user by using this
x,y,z=input("enter the varibales: ")
print(x,y,z)

Q10. What are keywords?
Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.

Q11. Can we use keywords as a variable? Support your answer with reason.
No, because keywords are only meant for reserved purposes.

Q12. What is indentation? What's the use of indentaion in Python?
Python indentation refers to adding white space before a statement to a particular block of code.
 In another word, all the statements with the same space to the right, belong to the same code
 Statement (line 1), if condition (line 2), and statement (last line) belongs to the same block which means that after statement 1, if condition will be executed. and suppose the if condition becomes False then the Python will jump to the last statement for execution.
The nested if-else belongs to block 2 which means that if nested if becomes False, then Python will execute the statements inside the else condition.
Statements inside nested if-else belong to block 3 and only one statement will be executed depending on the if-else condition.

Q13. How can we throw some output in Python?
o=print("output")

Q14. What are operators in Python?
In Python, operators are special symbols that designate that some sort of computation should be performed. The values that an operator acts on are called operands. 
Here is an example: >>> >>> a = 10 >>> b = 20 >>> a + b 30. In this case, the + operator adds the operands a and b together.

Q15. What is difference between / and // operators?
| is a bitwise operator and compares each operands bitwise.

It is a binary OR Operator and copies a bit to the result it exists in either operands.

Assume integer variable A holds 60 and variable B holds 13 then  

(A | B) will give 61 which is 0011 1101.

Whereas || is a logical OR operator and operates on boolean operands. If both the operands are false, then the condition becomes false otherwise it is true. Assume boolean variable A holds true and variable B holds false then (A && B) is true.

| is to be used during bitwise operations and || is useful during logical operations.

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
a='iNeuron'
print(a*4)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
a=int(input("enter the number: "))
if a%2==0:
    print("EVEN")
else:
    print("ODD")
	
Q18. What are boolean operator?
Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused and productive results.
 This should save time and effort by eliminating inappropriate hits that must be scanned before discarding.

# Q19. What will the output of the following?
# ```
# 1 or 0 =1

# 0 and 0 =0

# True and False and True =False

# 1 or 0 or 0 =1
# ```

# Q20. What are conditional statements in Python?
Conditional Statement in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false. 
Conditional statements are handled by IF statements in Python.

# Q21. What is use of 'if', 'elif' and 'else' keywords?
It allows us to check for multiple expressions. If the condition for if is False , it checks the condition of the next elif block and so on. 
If all the conditions are False , the body of else is executed

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
a=int(input("Enter the age: "))
if a>=18:
	print("I can vote")
else: 
	print("I can't vote")

# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
even_numbers=[]
for i in numbers:
    if i%2==0:
        even_numbers.append(i)
print(even_numbers)
m=0
for l in even_numbers:
    m=m+l
print("The sum of even numbers from list is : ",m)


# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
lst=[]
n=int(input("enter the number of elements: "))
for i in range(0,n):
    ele=int(input("enter the number: "))
    lst.append(ele)
print("max num is : ",max(lst))

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
op=[]
for i in numbers:
    if i%5==0 and i<=150:
        op.append(i)
    elif i>500:
        break
print(op)
