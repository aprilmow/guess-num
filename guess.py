import random

r = random.randint(1, 100)
while True:
	guess = int(input('guess a number:'))
	if guess == r:
		print('correct!')
		break
	elif guess > r:
		print('too big')
	else:
		print('too small')
