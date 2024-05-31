# slicing accessing parts of a string

str = "hello world"
print(str[1:4])
print(str[0:6])       # space will also get considered
print(str[0:11])

print(str[6:len(str)])
       #or
print(str[6:])      # [6:len(str)]      #python automatically takes all the remaining complete words
print(str[:5])      # [0:5]             #python automatically starts it with the number 0


# negative slicing

str1 = 'apple'
print (str1[-3:-1])
print (str1[-5:-1])
print (str1[-5:])