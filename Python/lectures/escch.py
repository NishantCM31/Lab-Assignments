str1='Welcome to \'Python\' on my class'
print(str1)
str2="Welcome to \"Python\" on my class"
print(str2)

a='hello world'
b=a.capitalize()
print('Original Stirng: ',a)
print('New String',b)


mystr='Python is a programming language.'
print(mystr.endswith('.'))
print(mystr.endswith('age.'))


mystr1='Hello World'
print(mystr1.endswith('H',0,1))
print(mystr1.endswith('e',0,2))
print(mystr1.endswith('o',0,5))


mstr='Python is a freely available on python.org.website'
print(mstr.endswith(('Python','free','website')))
print(mstr.endswith(('Python','website','free')))
print(mstr.endswith(('Python','free')))
print(mstr.endswith(('Python','is'),0,9))