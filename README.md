# pythonCrashCourse
Learning notes for python through projects

[//]: # (By Gary Lam | June, 2021)


## Table of content
### Background
* [Data type and variable](#data-type-and-variable)
* [Basic loops](#basic-loops)
* [Advanced loops](#advanced-loop)
* [Simple Line Plot](#simple-line-plot)

## Background

### Data type and variable
|Data type|variable|
|---|----|
|Number|int, float, bool|
|String|str, chr|
|Container|list, dict, , set, tuple|

#### Interger
  ```python
  x = 1
  print(x)
  print(type(x))
  ```

#### Float
  ```python
  x = 1.5
  print(x)
  print(type(x))
  ```
  
#### String
  ```python
  say = "Hello Hong Kong"
  print(say)
  print(type(say))
  ```
  ```python
  str1 = "Welcome"
  str2 = "to Hong Kong"
  print(str1, str2)
  print(str1 + str2)
  ```
  
#### Casting
  ```python
  floatNum = 55.0
  intNum = int(floatNum)
  ```
  
  ```python
  stringNum = "55"
  intNum = int(stringNum)
  ```
  
#### Containers

#### List
  ```python
  list1 = [0]*10
  print(list1)

  list2 = ','.join(['This', 'is', 'a', 'list'])
  print(list2)

  print(list('Python is fun'))
  ```

#### Set
  ```python
  admins = {'Justin', 'Paul'}
  users = {'Billy', 'Apple', 'Justin'}

  # Is Justin in admin team?
  print('Justin' in admins)

  # Both in admins and users
  print(admins & users)
  ```

#### Dictionary
  ```python
  passwords = {'Justin' : 1234, 'Billy' : 'abcd'}
  print(passwords['Justin'])

  passwords['John'] = 1999
  print(passwords)
  print(passwords.keys())
  print(passwords.values())
  ```

#### Reference
https://openhome.cc/Gossip/CodeData/PythonTutorial/ContainerFlowComprehensionPy3.html

  ```python
  print('Enter your name:')
  name = input()

  if name == 'Gary':
      print ('Hello, welcome')
  else:
      print ('Hello, Guest')
  ``` 
  
Modify:
  ```python
  print('Enter your name:')
  name = input()

  if len(name) != 0:
      print ('Hello, ', name)
  else:
      print ('Hello, Guest')
  ```

comprehension
  ```python
  print('Enter your name:')
  name = input()

  print('Hello, ', name if name != '' else 'Guest')
  ```

### Basic Loops

#### While loop
  ```python
  print('Enter two numbers ...')
  m = int(input('Number 1: '))
  n = int(input('Number 2: '))
  
  # Greatest Common Divisor
  while n!= 0:
      r = m % n
      m = n
      n = r

  print ('GCD: {}'.format(m))
  ```

#### For loop

  ```python
  for i in range(0, 5):
      print('Hello world')

  for i in range(5):
      print('Hello world')
      
  for i in range(5, 0, -1):
    print('Hello world')
  ```

Simple loop:
  ```python
  n = int(input('Enter a number n:'))
  for i in range (0, n):
      print ('*', end="")
  ```

Nested loops:
  ```python
  n = int(input('Enter a number n:'))
  for j in range (0, n):
      for i in range(0, n):
          print ('*', end="")
      print("")
  ```

### Advanced loop

  ```python
  fruits = ['banana', 'apple', 'mango']

  for index in range(len(fruits)):
      print ('I like :', fruits[index])

  for index in fruits:
      print ('I like :', index)
  ```

  ```python
  numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
  odd_number = []

  for number in numbers:
      if number % 2 != 0:
          odd_number.append(number)

  print(odd_number)

  # Comprehension Version
  print([number for number in numbers if number % 2 != 0])
  ```

  ```python
  data1 = [name for name in ['AA', 'BB', 'CC']]
  print (data1)

  names = ['Apple', 'Billy', 'Calvin']
  passwords = [123, 456, 789]
  data2 = {name : password for name, password in zip(names, passwords)}
  print (data2)
  ```

### Simple Line Plot

Intro to pyplot
Reference: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

Installation
  ```python
  pip install atplotlib
  pip install numpy
  ```

Examples:
  ```python
  import matplotlib.pyplot as plt
  plt.plot([1, 2, 3, 4])
  plt.ylabel('some numbers')
  plt.show()
  ```
  
  ```python
  import matplotlib.pyplot as plt
  import numpy as np
  
  def f(t):
      return np.exp(-t) * np.cos(2*np.pi*t)

  t1 = np.arange(0.0, 5.0, 0.1)
  t2 = np.arange(0.0, 5.0, 0.02)

  plt.figure()
  plt.subplot(211)
  plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

  plt.subplot(212)
  plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
  plt.show()
  ```

```python
  import matplotlib.pyplot as plt
  import numpy as np

  mu, sigma = 100, 15
  x = mu + sigma * np.random.randn(10000)

  # the histogram of the data
  n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


  plt.xlabel('Smarts')
  plt.ylabel('Probability')
  plt.title('Histogram of IQ')
  plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
  plt.axis([40, 160, 0, 0.03])
  plt.grid(True)
  plt.show()
  ```
