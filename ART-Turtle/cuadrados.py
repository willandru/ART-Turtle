import turtle 

def setup():

	turtle.title('Animación de multiples cuadrados')
	turtle.setup(300, 300, 0, 0)
	turtle.pencolor('red')

def dibujar_cuadrados(size):
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)

setup()

for _ in range(0, 12):
	dibujar_cuadrados(50)
	turtle.right(120)

turtle.exitonclick()