from turtle import *
from random import *

class Sprite(Turtle):
   def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
      Turtle.__init__(self)
      self.penup()
      self.speed(6)
      self.goto(x,y)
      self.shape(shape)
      self.color(color)
      self.step = step
      self.points = 0
   def move_up(self):
       self.goto(self.xcor(), self.ycor() + self.step)
   def move_down(self):
      self.goto(self.xcor(), self.ycor() - self.step)
   def move_right(self):
       self.goto(self.xcor() + self.step, self.ycor())
   def move_left(self):
       self.goto(self.xcor() - self.step, self.ycor())
   
   def is_collide(self,sprite):
      dist = self.distance(sprite.xcor(), sprite.ycor())
      if dist <= 30:
         return True
      if dist > 30:
         return False
   
   #player.is_collide(goal)
   def setmove(self, x_start, y_start, x_end, y_end):
       self.x_start = x_start
       self.y_start = y_start       
       self.x_end = x_end
       self.y_end = y_end
       self.goto(x_start, y_start)
       self.setheading(self.towards(x_end, y_end))
   def makestep(self):
      self.forward(self.step)
      if self.distance(self.x_end, self.y_end) < self.step:
         self.setmove(self.x_end, self.y_end, self.x_start, self.y_start)
s_width = 200
s_hight = 180

player = Sprite(0,-100, color = 'orange')
total_score = 0
enemy1 = Sprite(-200, 0, 15, 'square', 'red')
enemy1.setmove(-200, 0, 200, 0)
enemy2 = Sprite(200, 70, 15, 'square', 'red')
enemy2.setmove(200, 70, -200, 70)
goal = Sprite(0,120,20, 'triangle', 'green')

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_left, 'Left')

while total_score < 3:
   enemy1.makestep()
   enemy2.makestep()
   if player.is_collide(goal):
      player.goto(0,-100)
      total_score += 1
   if player.is_collide(enemy1) or player.is_collide(enemy2):
      goal.hideturtle()
      break 
if total_score == 3:
   enemy1.hideturtle()
   enemy2.hideturtle()
   
