# pythonCrashCourse
Learning notes for python through projects

[//]: # (By Gary Lam | June, 2021)


## Table of content
### Background
* [Data type and variable](#data-type-and-variable)

## Background

### Data type and variable
|Data type|variable|
|---|----|
|Number|int, float, bool|
|String|str, chr|
|Container|list, dict, , set, tuple|

#### Examples

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
  passwords = {'Justin' : 1234, 'Billy' : 9999}
  print(passwords['Justin'])

  passwords['John'] = 1999
  print(passwords)
  print(passwords.keys())
  print(passwords.values())
  ```

#### Reference
https://openhome.cc/Gossip/CodeData/PythonTutorial/ContainerFlowComprehensionPy3.html

```python
```
