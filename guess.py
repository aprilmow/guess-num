import random

r = random.randint(1, 100)

count = 0
while True:
	count += 1 #count = count + 1
	guess = int(input('guess a number:'))
	if guess == r:
		print('correct!')
		print('this is your', count, 'times gussing')
		break
	elif guess > r:
		print('too big')
	else:
		print('too small')
	print('this is your', count, 'times gussing')
