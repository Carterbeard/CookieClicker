from turtle import Screen
import turtle
from typing_extensions import Self
from time import sleep
import tkinter

screen = Screen()
screen.setup(1001,1001)
screen.title("Cookie Clicker")
screen.bgcolor("medium slate blue")

screen.register_shape("Cookie.gif")
screen.register_shape("Cookie1.gif")
screen.register_shape("AutoclickerUpgrade.gif")

cookie = turtle.Turtle()
cookie.shape("Cookie.gif")
cookie.speed(0)

cookie1 = turtle.Turtle()
cookie1.shape("Cookie1.gif")
cookie1.speed(0)

AutoclickUpg = turtle.Turtle()
AutoclickUpg.shape("AutoclickerUpgrade.gif")
AutoclickUpg.speed(0)
AutoclickUpg.penup()
AutoclickUpg.goto(300,100)



cookiesps = 0
clicks = 0


counter = turtle.Turtle()
counter.hideturtle()
counter.color("mint cream")
counter.penup()
counter.goto(0,250)
counter.write(f"Cookies: {clicks}",align="center",font=("Times",32,"normal"))

def timesclicked(X,Y):
    global clicks
    clicks += 1
    cookie1.hideturtle()
    cookie1.showturtle()
    counter.clear()
    counter.write(f"Cookies: {clicks}",align="center",font=("Times",32,"normal"))
    
counterps = turtle.Turtle()
counterps.hideturtle()
counterps.color("light blue")
counterps.penup()
counterps.goto(0,200)
counterps.write(f"Cookies Per Second: {cookiesps}",align="center",font=("Century Gothic",24,"normal"))

def autoupg(x,y):
    global clicks
    global cookiesps
    if clicks <20:
        print("You do not have enough cookies")
    else:    
        cookiesps+=1
        clicks = clicks-20
        counterps.clear()
        counterps.write(f"Cookies Per Second: {cookiesps}",align="center",font=("Century Gothic",24,"normal"))
        counter.clear()
        counter.write(f"Cookies: {clicks}",align="center",font=("Times",32,"normal"))


while cookiesps>0:
    sleep(1)
    clicks+=1
   



cookie1.onclick(timesclicked)
AutoclickUpg.onclick(autoupg)






screen.mainloop()
