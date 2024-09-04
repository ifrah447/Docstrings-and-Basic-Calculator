# day 29 docstrings
# docstrings are the string literals that appears just right after the defination of a function,method,class or module.
def sum(a,b):
  '''hello this program is for the summation of two numbers. this is doc string in python don't take it as a comment '''
  print("sum of two numbers are: ",a+b)
  print(f"the number {a} is my lucky number while {b} is his lucky number")
print(sum.__doc__)
sum(2,4)
def calculator():
  '''this is a calculator program which contain docstring module'''
  a=float(input("enter the first number: "))
  b=float(input("enter the second number: "))
  print("press 1 for addition")
  print("press 2 for subtraction")
  print("3 for multiplication")
  print("4 for division")
  print("5 for modulus")
  print("6 for floor division")
  print("7 for exponential")
  choice=int(input("enter your choice: "))
  if choice==1:
    print(a+b)
  elif choice==2:
    print(a-b)
  elif choice==3:
    print(a*b)
  elif choice==4:
    print(a/b)
  elif choice==5:
    print(a%b)
  elif choice==6:
    print(a//b)
  elif choice==7:
    print(a**b)
  else:
    print("you make an invalid choice")
print(calculator.__doc__)
calculator()
# PEP8 is a document that provide guidelines and best practices on how to write python code. PEP stands for Python Enhancement Proposal and there are several of them. A PEP is a document that describes the new features proposed for python and documents aspects of python, like design and style for the community
# the zen of python is a poem by Tim Peters which describes the importance of code readability it can be seen by writting ""import this""" in python shell
