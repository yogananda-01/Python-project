score=0
print('Welcome to the python quiz ')
print("1. What is the capital of India?")
print("a) Mumbai")
print("b) New Delhi")
print("c) Chennai")
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) New Delhi.\n")
    
print('2.Which program language are you learning currently')
print('a) java')
print('b) python')
print('c) HTML')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) Python.\n")

print("3.How many continents are there in the world ")
print('a) 8')
print('b) 6')
print('c) 5')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is a) 8.\n")
    
print('4.Which planet is known as red planet ')
print("a) Jupiter")
print('b) venus')
print('c) Mars')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) mars.\n")
    
print('5.what does cpu stands for')
print('a) Central processing unit')
print('b) computer processing unit ')
print('c) control processing unit')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is a) Central processing unit.\n")
    
print('6.which symbol is used for comment in python')
print('a) //')
print('b) #')
print('c) ~')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) #.\n")
    
print('7.Which keyword is used to create a function in python')
print('a) def')
print('b) function')
print('c) create')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) function.\n")
    
print('8.Write the output for:')
print("print(2+3)")
print('a) 6')
print('b) 5')
print('c) Error')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) 5.\n")
    
print('9.Which data type is used to dtore text in python')
print('a) int')
print('b) bool')
print('c) String')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) String.\n")
    
print('10.who developed python')
print('a) Guido van Rossum')
print('b) james Gosling')
print('c) Bill Gates')
answer = input("Enter your answer (a/b/c): ")

if answer.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is a) Guido van Rossum.\n")
    
print('quiz completed!!')
if score>8:
    print('Your Score = A+')
elif score>6:
    print('your Score = A')
elif score>5:
    print('Your score = B')
else:
    print('You need more practice')
