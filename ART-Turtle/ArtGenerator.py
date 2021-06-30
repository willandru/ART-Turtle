import turtle
from random import randint

def get_input_angle():
	""" Obtain input from user and convert to an int"""
	message= 'please provide an angle:'
	value_as_string= input(message)
	while not value_as_string.isnumeric():
		print('The input must be an integer!')
		value_as_string = input(message)
	return int(value_as_string)

def generate_random_colour():
	""" Generates an R, G, B values randomly in range 0 to 255"""
	r= randint(0, 255)
	g= randint(0, 255)
	b= randint(0, 255)
	return r, g, b

print('Set up screen')
turtle.title('Colorful pattern')
turtle.setup(640,600)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(100)


angle=get_input_angle()

print(' Start the drawing')
for i in range(0, 500):
	turtle.color(generate_random_colour())
	turtle.forward(-i)
	turtle.right(angle)

print('Done')
turtle.done()