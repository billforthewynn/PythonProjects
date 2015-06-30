# Hello! What is your name?
# Albert
# Well, Albert, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too high.
# Take a guess.
# 2
# Your guess is too low.
# Take a guess.
# 4
# Good job, Albert! You guessed my number in 3 guesses!

from random import randint

answer = randint(0,20)

print 'Hello! What is your name?'

name = raw_input()

print 'Well, %s, I am thinking of a number between 1 and 20.' % name

guess = 1

while guess <= 5:
	# remaining_guesses = 6 - guess
	# print answer
	guess_input = int(raw_input())
	if guess_input > answer:
		print 'Your guess is too high'
	if guess_input < answer: 
		print 'Your guess is too low'
	if guess_input == answer and guess == 1: 
		print 'Good job, %s! You guessed my number in %s guess!' % (name, guess)
		break
	if guess_input == answer:
		print 'Good job, %s! You guessed my number in %s guesses!' % (name, guess)
		break 	
	guess = guess+1

if guess == 6:
	print 'Thanks for playing! The number was %s!' % answer


