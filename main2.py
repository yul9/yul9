
# () [] {}

# operators +-*/

# if for 

# print






# cyrillic_letters = "пир"
# cyrillic_letters[0] == 'п'

# translit_dict['п'] == 'p' # true
# cyrillic_letters[0] == 'п' # true

# print(translit_dict[cyrillic_letters[0]])


# for i in range(0,len(input_text)):
# 	x = input_text[i]
# 	if x=='с':
# 		print('s', end='')	
# 	elif x=='п':
# 		print('p', end='')	
# 	elif x=='о':
# 		print('o', end='')	
# 	elif x=='и':
# 		print('і', end='')	
# 	elif x=='б':
# 		print('b', end='')
# 	else:
# 		print(x, end='')
# horisontal output
# all letters
# capital letters
# everything else except letters: do nothing


# # store mapping in strings
# x = 50
# symbol = "O"
# thickness = 8

# first_line = '\n' + x*symbol
# last_line = '\n' + x*symbol
# line_with_spaces = '\n'+(symbol*thickness + (" "*(x - thickness*2) + symbol*thickness))
# print(first_line*thickness + (line_with_spaces*(x//2)) + last_line*thickness)
# print(x*symbol)


# a = 'objection'
# print(a[0:6]+('-')+(a[6])+('-')+(a[7:9]))

# e='contrapoints'
# print(e[:3]+'$'+e[3:6]+'$'+e[6:])

# a, b = 0, 1
# while a < 1000:
# 	# print(a, end=',')
# 	a, b = a+b, b
# 	print(a,b)


# a, b = 0, 1
# while a < 1000:
# 	# print(a, end=',')
# 	a, b = b, a+b
# 	print(a,b)

# print ('Космічний бар \"Пробіл\":\nвхід тільки у в\'язаному\n\t светрі')
#print ("""Космічний бар "Пробіл":
#вхід тільки у в'язаному
#	светрі""")
# i = "izoBILLEieeeees"
# print (i[1:-1])

"""Космічний бар "Пробіл":вхід тільки у в'язаному светрі"""
text = "Космічний бар \"Пробіл\":вхід тільки у в'язаному светрі"
x = ['о','і','и','а','е','я']
# t = 'y'
index = 4
#print (i[0]+'y'+i[2:])


for i in range(0,len(text)): #i=1 i=2
	if text[i] == 'о' or text[i] == 'і':
		text = text[:i]+'y'+text[i+1:]
print(text)






# # current_symbol = 
# if current_symbol == x[0] or current_symbol == x[1]:
# 	
