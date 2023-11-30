#happy birthday 
from turtle import *
import colorsys

speed(10000)
bgcolor("black")
h=0

#flor
for i in range(15):
	for j in range(10):
		c=colorsys.hsv_to_rgb(h,1,1)
		color(c)
		h+=0.05 #h <1 (if use 0.05 the bucle j <20)
		rt(90) 
		circle(150-j*6,90) 
		lt(90) 
		circle(150-j*6,90) 
		rt(180) 
	circle(40,24)
	
penup()
#nombre
#colors = ["red", "orange", "yellow", "light green", "green", "cyan", "blue", "dark blue", "purple", "pink"] #colors rainbow
colors = ["red", "orange", "yellow", "light green", "cyan", "blue", "purple"] #i like this combination
# colors = ["red", "purple", "blue", "green", "orange", "yellow"] #party feeling
str="HAPPY B-DAY!!!"
for i in range (len(str)):
	goto((-350 + i * 50, 250))
	color(colors[i%len(colors)])
	write(str[i], font=("Courier", 40, "bold"))
	

hideturtle()

done()