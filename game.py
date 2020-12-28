import turtle
import time
import random

# initiliser un dépôt github


delay = 0.1

# -------------------------------------------------------------------
# ---------------------------set up game -------------------------
wn = turtle.Screen()
wn.title("Mon jeu de srpent")
wn.bgcolor("blue")
# redimenssionner l'ecran
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the sreen updates

# -------------------------------------------------------------------
# --------------------------- head turte -------------------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop" #default = "stop"



# -------------------------------------------------------------------
# --------------------------- head food -------------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("aqua")
food.penup()
food.goto(0, 100)


# -------------------------------------------------------------------
# ---------------------------function -------------------------
def go_up():
	head.direction = "up"

def go_down():
	head.direction = "down"

def go_left():
	head.direction = "left"

def go_right():
	head.direction = "right"




def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
	    x = head.xcor()
	    head.setx(x + 20)

# -------------------------------------------------------------------
# --------------------------- Keyboard bindings -------------------------
wn.listen()
wn.onkeypress(go_up, "8")
wn.onkeypress(go_down, "2")
wn.onkeypress(go_left, "4")
wn.onkeypress(go_right, "6")


# -------------------------------------------------------------------
# --------------------------- main game loop -------------------------
while True:
	wn.update()

	if head.distance(food) < 20:
		# More the food to a randon spot
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)


	move()

	time.sleep(delay)



wn.mainloop()