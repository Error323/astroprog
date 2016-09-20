
# Week 3 - Tuesday

## Recap on previous assignment
Grading scheme 0,2,2,3,3 one point subtracted per mistake in a command or e.g. missing image. If only searching in 1 folder then 2 points are subtracted.

### Feedback week 2

    grep '# ' FILE | wc -l
    sort -r -n
   
## Python
Programming choice for this course is Python.
 
* Developed by Guido van Rossum at CWI
* Easy to learn language
* Concise code, fast results
* Very active, many libraries, good support
* Differences with C(++)?

### Hello World!
    
    echo print '"Hello World!"' > hello.py
    
* Shebang `#!/usr/bin/env python` lets the system know this should be executed as python script
* Executable bit `chmod +x`


```python
print "This is an interactive session!"
print "From here onwards I will keep programming in this session"
```

    This is an interactive session!
    From here onwards I will keep programming in this session


### Variables and basic data types

* `int`
* `float`
* `bool`
* `string`
* `None`


```python
a = 30
b = 11.34
c = 11
s = 'foo'
B = True
n = None

print (a/b)
print 30/11
print type(a)
print type(b)
print float(a/c)
print s
print 3*s + 'bar'
print b
```

    2.6455026455
    2
    <type 'int'>
    <type 'float'>
    2.0
    foo
    foofoofoobar
    11.34



```python
# Mutable and immutable
s = "Hello world!"
S = list(s)
u = s.upper()

print s, u
print s[0], s[2]
print S
S[2] = 'X'
print S
#print s[2], u[2]
# s[2] = 'X' ## CREATES AN ERROR, STRINGS ARE NOT MUTABLE! (Pretest)
#print S
#S[2] = 'X'
#print S
```

    Hello world! HELLO WORLD!
    H l
    ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
    ['H', 'e', 'X', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']



```python
# Literals
n = 11      # decimal
x = 013     # octal
y = 0xb     # hexadecimal
z = 0b1011  # binary

print n, x, y, z
print hex(n)
print oct(y)

r = 11.321
q = 1.1321e+1
print r, q, 1e-3
```

    11 11 11 11
    0xb
    013
    11.321 11.321 0.001



```python
# Casting variables or literals
print int(1.9)
print float(2/3)
print str(3.1415)
```

    1
    0.0
    3.1415



```python
# Boolean algebra
a = True
b = False
print a, b
print not a
print (a and b)
print (a or b)
print (a or not (a and b))

print 3 > 9
print "string1".upper() == "STRING1"
```

    True False
    False
    False
    True
    True
    False
    True



```python
# Datastructures contain your values

l = [4,2,'x']      # The List
t = (2,9,'y')      # The Tuple -- immutable
d = {2:'x', 'y':5} # The Dictionary
s = {2,3,2,2}      # The Set

D = {2:[3,2,6], 'x': (4,2,1)}

#print l, l[0]
#print t, t[1]
print D
print D['x']
L = [3,2,68,3.4,63]
print max(L)
print min(L)
#print s
```

    {'x': (4, 2, 1), 2: [3, 2, 6]}
    (4, 2, 1)
    68
    2



```python
# List slicing and indexing

s = list('abgdefd')
print s.index('d')
#print type(s)
#print s[0] # normal indexing
#print s[-1] # accessing last character
#print s[2:4]
#print s[:3], s[2:]
```

    3



```python
# looping over and over again....

l = [1,2,3,4,5,6]

#for v in l:
#    print (v+3)
    
#for i in range(10):
#    print i
    
#i = 0
#while i < len(l):
#    print l[i]
#    i = i + 1
    
#d = {1: 'a', 2: 'b', 3: 'c'}
#for k in d:
#    print k, d[k]

l = [(2,'x', 3), (5, 'z',5), (0, 'q',6)]
for a,b,c in l:
    print a, b, c
    
#for i in range(20):
#    print i
    
print range(10)
```

    2 x 3
    5 z 5
    0 q 6
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
# conditions make programs interesting



if 3 > 5:
    print "3 > 5"
else:
    print "no wait, 3 <= 5", (3 <= 5)
  
i = 4

if i == 0:
    print i
elif i == 2:
    print i
elif i == 4:
    print i
elif i == 6:
    print i
else:
    print "no no no no"
    
for i in range(10):
    if i % 2 == 0: # if i modulo 2 has a remainder of 0
        print i
```

    no wait, 3 <= 5 True
    4
    0
    2
    4
    6
    8



```python
# File I/O
f = open('myfile.txt', 'w')
f.write('This is written into the file\n')
f.write('And so is this\n')
f.close()

f = open('myfile.txt', 'r')
print f.read()
f.close()

## closing files is boring, we can simplify
# Scope
with open('myfile.txt', 'r') as f:
    words = 0
    lines = 0
    for line in f:
        lines += 1
        words += len(line.split(' '))
        
    print words, lines

```

    This is written into the file
    And so is this
    
    10 2

