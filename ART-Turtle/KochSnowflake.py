import turtle

ANGLES =[60, -120, 60, 0]
SIZE_OF_SNOWFLAKE= 300


def get_input_depth():
	"""Obtain input from user and convert to an int"""
	message='Please provide the depth (0 or a positive integer):'
	value_as_string= input(message)
	while not value_as_string.isnumeric():
		print('The input must be an integer!')
		value_as_string = input(message)
	return int(value_as_string)

def setup_screen(title, background='white', screen_size_x=640, screen_size_y= 320, tracer_size=800):
	print('Set up Screen')

	turtle.title(title)
	turtle.setup(screen_size_x,screen_size_y)
	turtle.penup()
	turtle.backward(240)
	turtle.tracer(tracer_size)
	turtle.bgcolor(background)


def draw_koch(size, depth):
	if depth>0:
		for angle  in ANGLES:
			draw_koch(size/3, depth-1)
			turtle.left(angle)
	else:
		turtle.forward(size)


depth=get_input_depth()
setup_screen('Koch Snowflake (depth' + str(depth) + ')', background='black', screen_size_x=420, screen_size_y=420)
turtle.color('sky blue')


turtle.penup()
turtle.setposition(-180,0)
turtle.left(30)
turtle.pendown()
turtle.speed(50)



for _ in range(3):
	draw_koch(SIZE_OF_SNOWFLAKE, depth)
	turtle.right(120)

turtle.update()
print('Done')
turtle.done()