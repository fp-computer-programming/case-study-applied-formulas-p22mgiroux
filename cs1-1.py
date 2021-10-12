# Author: MOG 10/12/21

x1 = input("What is the x value of your first point? ")
y1 = input("What is the y value of your first point? ")
x2 = input("What is the x value of your second point? ")
y2 = input("What is the y value of your second point? ")

distance = (((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2)) ** .5

print("The distance between points (" + x1 + ", " + y1 + ") and (" + x2 + ", " + y2 + ") is " + str(distance) + ".")