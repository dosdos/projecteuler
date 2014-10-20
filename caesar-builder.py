

#===============================================================================
# text = 'The Answer to the Ultimate Question of Life The Universe and Everything is forty two'
#===============================================================================


text1 = 'the third number is the answer to the ultimate question of life the universe and everything'

text = 'the result is the sum of three numbers the first number is inside the email you received from scontoflash the second number is riccardos facebook id the third number is the answer to the ultimate question of life the universe and everything and remember to like us on facebook'

print(len(text))

alphabeth = ' xyzabcdefghijklmnopqrstuvw'

secretCode = {}

for a in alphabeth:
	secretCode[a] = alphabeth.index(a)

for s in secretCode:
	print(s,secretCode[s])

code = []

for l in text:
	code.append(secretCode[l])
	# code.append(l)

# print code

code = [bin(c)[2:].zfill(5) for c in code]

numsperline = 12

nlines = int(len(code)/numsperline)
rest = len(code)%numsperline

# print nlines

print('THERE ARE ONLY 10 KIND OF PEOPLE THAT UNDERSTAND BINARY CODE. CAESAR WAS ONE OF THEM. \n')

for i in range(nlines+1):
	begin = 0+i*numsperline
	end = numsperline+i*numsperline
	if end>len(code):
		end = len(code)
	string = ''
	for num in code[begin:end]: 
		string = string+str(num)+' '
	print(string)

# maxim = 0
# for c in code:
# 	if len(c) > maxim:
# 		maxim = len(c)

# print maxim

