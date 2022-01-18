# Anagram Solver using Python!
### Yes! We made a anagram solver for you using the easiest language `Python`

<br>

# Basic Usage :
>### You can basically match two strings and only see if they are matched if we sort their letters...
## Example :
### Input :
```py
solver = Anagram()
x = solver.match('bgaladshne')
print(x)
```
### Output :
```py
(True, 'Bangladesh')
```
<br>

>### The **Anagram Class** also takes a parameter. It is a string and you have to define what type of data you want to solve. For Example if you want to solve an anagram of **capitals of countries** then your parameter should be **"capital"**. If **no paramter** is passed then by default it will take your input word as an anagram of a **country**.
<br>

## Example :
### Input :
```py
solver = Anagram('capital')
x = solver.match('hakad')
print(x)
```

### Output :
```py
(True, 'Dhaka')
```

# Pro Match Function :
>### Your anagram not always fully matches a word! You probably sometimes might need to find out the closest word matching your input word! So we made a pro match function that does this cool stuff and shows all the closest words having same length as a result! Example Below.

## Example:
### Input :
```py
solver = Anagram()
x = solver.pro_match('bgaladshne')
print(x)
```
### Output :
```py
[('bangladesh', 100.0), ('azerbaijan', 50.0), ('kazakhstan', 50.0), ('madagascar', 50.0), ('uzbekistan', 50.0), ('cabo verde', 40.0), ('kyrgyzstan', 40.0), ('luxembourg', 40.0), ('micronesia', 40.0), ('san marino', 40.0), ('seychelles', 40.0), ('tajikistan', 40.0), ('costa rica', 30.0), ('mauritania', 30.0), ('montenegro', 30.0), ('mozambique', 30.0)]
```
<br>

>### In the above Example the first item of the first tuple is the country's name and the next one shows how much did the name matched with your input word!

<br>

## The **pro match max** function :

>### As the pro match function returns multiple different words matching at different rates, You may want to get the most matching word and that is why we made a pro match max function that returns the results that matches the most.

<br>

## Example:
### Input :
```py
solver = Anagram()
x = solver.pro_match('bgaladshne')
print(x)
```

### Output :
```py
[('bangladesh', 100.0)]
```

# New Similarity Match Function :
>### Unfortunately we haven't completed it yet so we just added the pass function in the source code. We hope to complete that as soon as possible!

# Thank you :
>### If you find any bugs or have any suggestion for us, don't hesitate to mail us at tasawarshuddho@gmail.com!
>### Have a nice day! ;)
