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
# New Ultra Pro Match and Ultra Pro Match Max Function :
>### It tries to match with all words in the database. It can be the most useful to you! Here we are giving an example for ultra pro match function. The ultra pro match max function returns the closest match like pro match max function.
## Example:
### Input :
```py
solver = Anagram()
x = solver.ultra_pro_match('bgaladshne')
print(x)
```

### Output :
```py
[(100.0, 'bangladesh'), (63.63636363636363, 'netherlands'), (60.0, 'grenada'), (60.0, 'senegal'), (60.0, 'thailand'), (54.54545454545454, 'afghanistan'), (54.54545454545454, 'el salvador'), (54.54545454545454, 'new zealand'), (54.54545454545454, 'switzerland'), (53.84615384615385, 'guinea-bissau'), (50.0, 'albania'), (50.0, 'algeria'), (50.0, 'angola'), (50.0, 'argentina'), (50.0, 'azerbaijan'), (50.0, 'bahamas'), (50.0, 'bahrain'), (50.0, 'barbados'), (50.0, 'belarus'), (50.0, 'botswana'), (50.0, 'bulgaria'), (50.0, 'ghana'), (50.0, 'guatemala'), (50.0, 'honduras'), (50.0, 'iceland'), (50.0, 'indonesia'), (50.0, 'ireland'), (50.0, 'kazakhstan'), (50.0, 'lebanon'), (50.0, 'lithuania'), (50.0, 'madagascar'), (50.0, 'maldives'), (50.0, 'palestine'), (50.0, 'singapore'), (50.0, 'slovenia'), (50.0, 'sri lanka'), (50.0, 'uganda'), (50.0, 'uzbekistan'), (45.45454545454545, 'philippines'), (45.45454545454545, 'saint lucia'), (45.45454545454545, 'south sudan'), (43.75, 'marshall islands'), (41.66666666666667, 'burkina faso'), (41.66666666666667, 'saudi arabia'), (41.66666666666667, 'sierra leone'), (40.909090909090914, 'bosnia and herzegovina'), (40.0, 'andorra'), (40.0, 'armenia'), (40.0, 'australia'), (40.0, 'belgium'), (40.0, 'bhutan'), (40.0, 'cabo verde'), (40.0, 'cambodia'), (40.0, 'canada'), (40.0, 'denmark'), (40.0, 'estonia'), (40.0, 'eswatini'), (40.0, 'finland'), (40.0, 'gabon'), (40.0, 'gambia'), (40.0, 'germany'), (40.0, 'guinea'), (40.0, 'guyana'), (40.0, 'hungary'), (40.0, 'israel'), (40.0, 'kyrgyzstan'), (40.0, 'lesotho'), (40.0, 'liberia'), (40.0, 'luxembourg'), (40.0, 'malaysia'), (40.0, 'micronesia'), (40.0, 'mongolia'), (40.0, 'namibia'), (40.0, 'nepal'), (40.0, 'nicaragua'), (40.0, 'nigeria'), (40.0, 'north macedonia'), (40.0, 'pakistan'), (40.0, 'poland'), (40.0, 'rwanda'), (40.0, 'san marino'), (40.0, 'serbia'), (40.0, 'seychelles'), (40.0, 'slovakia'), (40.0, 'somalia'), (40.0, 'sudan'), (40.0, 'suriname'), (40.0, 'sweden'), (40.0, 'tajikistan'), (40.0, 'venezuela'), (38.46153846153847, 'liechtenstein'), (36.36363636363637, 'north korea'), (36.36363636363637, 'south korea'), (35.294117647058826, 'equatorial guinea'), (35.0, 'united arab emirates'), (33.33333333333333, 'dominican republic'), (33.33333333333333, 'solomon islands'), (33.33333333333333, 'south africa'), (33.33333333333333, 'turkmenistan'), (31.57894736842105, 'antigua and barbuda'), (31.57894736842105, 'trinidad and tobago'), (31.25, 'papua new guinea'), (30.434782608695656, 'vatican city (holy see)'), (30.0, 'austria'), (30.0, 'belize'), (30.0, 'benin'), (30.0, 'bolivia'), (30.0, 'brazil'), (30.0, 'brunei'), (30.0, 'burundi'), (30.0, 'cameroon'), (30.0, 'chad'), (30.0, 'chile'), (30.0, 'china'), (30.0, 'colombia'), (30.0, 'costa rica'), (30.0, 'czechia'), (30.0, 'dominica'), (30.0, 'ecuador'), (30.0, 'ethiopia'), (30.0, 'france'), (30.0, 'georgia'), (30.0, 'india'), (30.0, 'japan'), (30.0, 'jordan'), (30.0, 'kenya'), (30.0, 'laos'), (30.0, 'latvia'), (30.0, 'libya'), (30.0, 'malawi'), (30.0, 'malta'), (30.0, 'mauritania'), (30.0, 'moldova'), (30.0, 'montenegro'), (30.0, 'mozambique'), (30.0, 'niger'), (30.0, 'palau'), (30.0, 'panama'), (30.0, 'paraguay'), (30.0, 'portugal'), (30.0, 'romania'), (30.0, 'samoa'), (30.0, 'spain'), (30.0, 'taiwan'), (30.0, 'tanzania'), (30.0, 'tonga'), (30.0, 'tunisia'), (30.0, 'ukraine'), (30.0, 'vanuatu'), (30.0, 'vietnam'), (30.0, 'zambia'), (30.0, 'zimbabwe'), (28.57142857142857, 'saint kitts and nevis'), (28.57142857142857, 'sao tome and principe'), (28.57142857142857, 'united kingdom'), (27.27272727272727, 'congo, republic of the'), (27.27272727272727, 'timor-leste'), (25.0, 'central african republic'), (25.0, 'myanmarnaypyidaw'), (25.0, 'saint vincent and the grenadines'), (25.0, 'united states of america'), (24.242424242424242, 'congo, democratic republic of the'), (20.0, 'croatia'), (20.0, 'cuba'), (20.0, 'djibouti'), (20.0, 'egypt'), (20.0, 'eritrea'), (20.0, 'greece'), (20.0, 'haiti'), (20.0, 'iran'), (20.0, 'italy'), (20.0, 'jamaica'), (20.0, 'kiribati'), (20.0, 'mali'), (20.0, 'mauritius'), (20.0, 'monaco'), (20.0, 'nauru'), (20.0, 'norway'), (20.0, 'oman'), (20.0, 'qatar'), (20.0, 'russia'), (20.0, 'syria'), (20.0, 'tuvalu'), (20.0, 'uruguay'), (20.0, 'yemen'), (15.384615384615385, "cote d'ivoire"), (10.0, 'comoros'), (10.0, 'cyprus'), (10.0, 'iraq'), (10.0, 'kosovo'), (10.0, 'kuwait'), (10.0, 'mexico'), (10.0, 'peru'), (10.0, 'togo'), (10.0, 'turkey'), (0.0, 'fiji'), (0.0, 'morocco')]
```
# New Similarity Match Function :
>### It just matches letter by letter. May be less useful to you...
## Example:
### Input :
```py
solver = Anagram()
x = solver.similarity_match('bgaladshne')
print(x)
```

### Output :
```py
[('ghana', 40.0), ('italy', 40.0), ('barbados', 37.5), ('bhutan', 33.33333333333333), ('brazil', 33.33333333333333), ('uganda', 33.33333333333333), ('philippines', 30.0), ('bahamas', 28.57142857142857), ('bahrain', 28.57142857142857), ('belarus', 28.57142857142857), ('burundi', 28.57142857142857), ('finland', 28.57142857142857), ('grenada', 28.57142857142857), ('iceland', 28.57142857142857), ('ireland', 28.57142857142857), ('bulgaria', 25.0), ('chad', 25.0), ('iran', 25.0), ('iraq', 25.0), ('oman', 25.0), ('benin', 20.0), ('bosnia and herzegovina', 20.0), ('chile', 20.0), ('china', 20.0), ('egypt', 20.0), ('india', 20.0), ('kenya', 20.0), ('libya', 20.0), ('malta', 20.0), ('samoa', 20.0), ('spain', 20.0), ('syria', 20.0), ('tonga', 20.0), ('belize', 16.666666666666664), ('brunei', 16.666666666666664), ('france', 16.666666666666664), ('jordan', 16.666666666666664), ('norway', 16.666666666666664), ('poland', 16.666666666666664), ('rwanda', 16.666666666666664), ('taiwan', 16.666666666666664), ('belgium', 14.285714285714285), ('bolivia', 14.285714285714285), ('comoros', 14.285714285714285), ('denmark', 14.285714285714285), ('germany', 14.285714285714285), ('hungary', 14.285714285714285), ('vanuatu', 14.285714285714285), ('botswana', 12.5), ('cambodia', 12.5), ('slovakia', 12.5), ('tanzania', 12.5), ('thailand', 12.5), ('zimbabwe', 12.5), ('guatemala', 11.11111111111111), ('indonesia', 11.11111111111111), ('singapore', 11.11111111111111), ('afghanistan', 10.0), ('bangladesh', 10.0), ('burkina faso', 10.0), ('cabo verde', 10.0), ('costa rica', 10.0), ("cote d'ivoire", 10.0), ('dominican republic', 10.0), ('el salvador', 10.0), ('kazakhstan', 10.0), ('kyrgyzstan', 10.0), ('madagascar', 10.0), ('mozambique', 10.0), ('myanmarnaypyidaw', 10.0), ('netherlands', 10.0), ('north korea', 10.0), ('north macedonia', 10.0), ('papua new guinea', 10.0), ('saint vincent and the grenadines', 10.0), ('san marino', 10.0), ('south korea', 10.0), ('south sudan', 10.0), ('tajikistan', 10.0), ('trinidad and tobago', 10.0), ('united arab emirates', 10.0), ('united kingdom', 10.0), ('united states of america', 10.0), ('uzbekistan', 10.0), ('albania', 0.0), ('algeria', 0.0), ('andorra', 0.0), ('angola', 0.0), ('antigua and barbuda', 0.0), ('argentina', 0.0), ('armenia', 0.0), ('australia', 0.0), ('austria', 0.0), ('azerbaijan', 0.0), ('cameroon', 0.0), ('canada', 0.0), ('central african republic', 0.0), ('colombia', 0.0), ('congo, democratic republic of the', 0.0), ('congo, republic of the', 0.0), ('croatia', 0.0), ('cuba', 0.0), ('cyprus', 0.0), ('czechia', 0.0), ('djibouti', 0.0), ('dominica', 0.0), ('ecuador', 0.0), ('equatorial guinea', 0.0), ('eritrea', 0.0), ('estonia', 0.0), ('eswatini', 0.0), ('ethiopia', 0.0), ('fiji', 0.0), ('gabon', 0.0), ('gambia', 0.0), ('georgia', 0.0), ('greece', 0.0), ('guinea', 0.0), ('guinea-bissau', 0.0), ('guyana', 0.0), ('haiti', 0.0), ('honduras', 0.0), ('israel', 0.0), ('jamaica', 0.0), ('japan', 0.0), ('kiribati', 0.0), ('kosovo', 0.0), ('kuwait', 0.0), ('laos', 0.0), ('latvia', 0.0), ('lebanon', 0.0), ('lesotho', 0.0), ('liberia', 0.0), ('liechtenstein', 0.0), ('lithuania', 0.0), ('luxembourg', 0.0), ('malawi', 0.0), ('malaysia', 0.0), ('maldives', 0.0), ('mali', 0.0), ('marshall islands', 0.0), ('mauritania', 0.0), ('mauritius', 0.0), ('mexico', 0.0), ('micronesia', 0.0), ('moldova', 0.0), ('monaco', 0.0), ('mongolia', 0.0), ('montenegro', 0.0), ('morocco', 0.0), ('namibia', 0.0), ('nauru', 0.0), ('nepal', 0.0), ('new zealand', 0.0), ('nicaragua', 0.0), ('niger', 0.0), ('nigeria', 0.0), ('pakistan', 0.0), ('palau', 0.0), ('palestine', 0.0), ('panama', 0.0), ('paraguay', 0.0), ('peru', 0.0), ('portugal', 0.0), ('qatar', 0.0), ('romania', 0.0), ('russia', 0.0), ('saint kitts and nevis', 0.0), ('saint lucia', 0.0), ('sao tome and principe', 0.0), ('saudi arabia', 0.0), ('senegal', 0.0), ('serbia', 0.0), ('seychelles', 0.0), ('sierra leone', 0.0), ('slovenia', 0.0), ('solomon islands', 0.0), ('somalia', 0.0), ('south africa', 0.0), ('sri lanka', 0.0), ('sudan', 0.0), ('suriname', 0.0), ('sweden', 0.0), ('switzerland', 0.0), ('timor-leste', 0.0), ('togo', 0.0), ('tunisia', 0.0), ('turkey', 0.0), ('turkmenistan', 0.0), ('tuvalu', 0.0), ('ukraine', 0.0), ('uruguay', 0.0), ('vatican city (holy see)', 0.0), ('venezuela', 0.0), ('vietnam', 0.0), ('yemen', 0.0), ('zambia', 0.0)]
```

# Thank you :
>### If you find any bugs or have any suggestion for us, don't hesitate to mail us at tasawarshuddho@gmail.com!
>### Have a nice day! ;)
