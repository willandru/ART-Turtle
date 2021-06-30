import turtle

IMAGE_SIZE_Y=150
IMAGE_SIZE_X=150
MIN_Y=0
MIN_X=0
MAX_Y=5
MAX_X=5
MAX_ITERATIONS=200
SCREEN_OFFSET_X=200
SCREEN_OFFSET_Y=200

print('Set up screen')
turtle.title('Mendelbrot')
turtle.setup(200,200)
turtle.hideturtle()
turtle.bgcolor('sky blue')
turtle.colormode(255)
turtle.speed(10)

for y in range(IMAGE_SIZE_Y):
	zy= y * (MAX_Y - MIN_Y) / (IMAGE_SIZE_Y - 1) + MIN_Y
	turtle.speed(10)
	for x in range(IMAGE_SIZE_X):
			zx= x* (MAX_X - MIN_X) / (IMAGE_SIZE_Y-1)+ MIN_X
			z = zx + zy * 1j
			c= z
			turtle.speed(10)
			for i in range(MAX_ITERATIONS):
				if abs(z)> 2.0:
					break
				z = z * z + c
			turtle.color((i % 4 * 64, i % 8 * 32, i % 16 *16))
			turtle.setposition(x- SCREEN_OFFSET_X, y - SCREEN_OFFSET_Y)
			turtle.pendown()
			turtle.speed(10)
			turtle.dot(1)
			turtle.penup()
