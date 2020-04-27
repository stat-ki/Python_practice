from turtle import *

n = int(input("Please enter natural number "))
angle = 360/n
for i in range(n):
    forward(100)
    left(angle)
done()