

# 1) Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. 
# Write a function which is given the day number, and it returns the day name (a string).

# def day_of_wk(num):
#     days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
#     return(days[num])

# print(day_of_wk(2))
# print(type(day_of_wk(2)))


# 2) You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) 
# leaving on day number 3 (a Wednesday). You return home after 137 sleeps. 
# Write a general version of the program which asks for the starting day number, 
# and the length of your stay, and it will tell you the name of day of the week you 
# will return on.


# CODE BELOW STILL DOESN'T WORK!!!
# def vacay_length(duration):
#     day = (input("What day of the week would you like to leave? "))

#     days = {
#         "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5,
#     "Saturday": 6, "Sunday": 7
#     }

#     if day in days:
#         print("The number of the day you want to leave is: ", days[day])
#         print((days[day] + duration) % 7)
#         v = int((days[day] + duration) % 7)
#         print(f"you left your destination on a {days[v]}.")
#     else:
#         print("That day isn't in the week")
        
# print(vacay_length(21))

# CODE ABOVE STILL DOESN'T WORK !!!


# weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 
# 5: "Friday", 6: "Saturday"}

# x = int(input("what number of day of the week are you leaving? \n"))
# print("that's a {}.".format(weekdays[x]))

# y = int(input("How many nights will you stay at your destination? \n"))

# z = (x + y) % 7

# print("You left your destination on a {}".format(weekdays[z]))












# data = {'a': '1', 'b': '2', 'c':'3'}

# key = input('Enter the key: ')

# if key in data:
#     print('The value is:', data[key])
# else:
#     print('That key is not in the dictionary.')


# 3) Give the logical opposites of these conditions


# a > b  -->  <=
# a >= b  -->  <
# a >= 18  and  day == 3  -->  a < 18 and da != 3
# a >= 18  and  day != 3  -->  a < 18 and day == 3

# 4) What do these expressions evaluate to?

# 3 == 3 --> True
# 3 != 3 --> False
# 3 >= 4 --> True
# not (3 < 4) --> False

# 5) Complete this truth table:

# p  q  r    (not(p and q)) or r
# -------------------------------
# F  F  F    F
# F  F  T    T
# F  T  F    F
# F  T  T    T
# T  F  F    F
# T  F  T    T
# T  T  F    F
# T  T  T    T


# 6) Write a function which is given an exam mark, 
# and it returns a string — the grade for that mark — according to this scheme:

# def grade(mark):
#     g = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]

#     if mark >= 75:
#         return g[0]
#     elif mark >= 70 and mark <75:
#         return g[1]
#     elif mark >= 60 and mark < 70:
#         return g[2]
#     elif mark >= 50 and mark < 60:
#         return g[3]
#     elif mark >= 45 and mark < 50:
#         return g[4] 
#     elif mark >= 40 and mark <45:
#         return g[5]
#     else:
#         return g[6]


# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

# for x in xs:
#     print(x, grade(x))
    
  

# 7) Modify the turtle bar chart program so that the 
# pen is up for the small gaps between each bar.

# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")

# def draw_bar(t, height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(" " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.pu()
#     t.forward(10)
#     t.pd()

    



# tess = turtle.Turtle()
# tess.color("blue", "red")
# tess.pensize(3)

# tess.pu()
# tess.bk(100)
# tess.pd()

# xs = [48, 117, 200, 240, 160, 260, 220]

# for v in xs:
#     draw_bar(tess, v)

# wn.exitonclick()

# 8) Modify the turtle bar chart program so that the bar for any 
# value of 200 or more is filled with red, values between [100 and 200) 
# are filled with yellow, and bars representing values less than 100 
# are filled with green.

# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")

# def draw_bar(t, height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(" " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.pu()
#     t.forward(10)
#     t.pd()

    
# tess = turtle.Turtle()
# tess.color("blue", "red")
# tess.pensize(3)

# tess.pu()
# tess.bk(100)
# tess.pd()

# xs = [48, 117, 200, 240, 160, 260, 220]

# for v in xs:
#     if v >= 200:
#         tess.color("blue", "red")
#     elif v >= 100 and v < 200:
#         tess.color("blue", "yellow")
#     else: tess.color("blue", "green")
#     draw_bar(tess, v)

# wn.exitonclick()


# 9) In the turtle bar chart program, what do you expect to happen if one or 
# more of the data values in the list is negative? Try it out. 
# Change the program so that when it prints the text value for the negative bars, 
# it puts the text below the bottom of the bar.


# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")

# def draw_bar(t, height):

#     t.begin_fill()
#     t.left(90)
#     if height > 0:
#         t.forward(height)
#         t.write(" " + str(height))
#     else:
#         t.forward(height)
#         t.pu()
#         t.forward(-12)
#         t.write(" " + str(height))
#         t.bk(-12)
#         t.pd()
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.pu()
#     t.forward(10)
#     t.pd()

    
# tess = turtle.Turtle()
# tess.color("blue", "red")
# tess.pensize(3)

# tess.pu()
# tess.bk(100)
# tess.pd()

# xs = [48, 117, -155, 200, 240, 160, 260, 220]

# for v in xs:
#     if v >= 200:
#         tess.color("blue", "red")
#     elif v >= 100 and v < 200:
#         tess.color("blue", "yellow")
#     else: tess.color("blue", "green")
#     draw_bar(tess, v)

# wn.exitonclick()

# Finish excercises tomorrow
# Please work


# 10) Write a function find_hypot which, given the length of two sides of a 
# right-angled triangle, returns the length of the hypotenuse. 
# (Hint: x ** 0.5 will return the square root.)

# def find_hypot(a, b):
#     return (a ** 2 + b **2) ** .5

# print(find_hypot(4,5))


# 11) Write a function is_rightangled which, given the length of three sides 
# of a triangle, will determine whether the triangle is right-angled. 
# Assume that the third argument to the function is always the longest side. 
# It will return True if the triangle is right-angled, or False otherwise.

# def is_rightangled(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         return True
#     else:
#         return False
# print(is_rightangled(11, 60, 61))


# 12) Extend the above program so that the sides can be given to the function in any order.

# def is_rightangled(a, b, c):
#     sides_list = [a, b, c]
#     sorted_sides = sorted(sides_list)
#     a = sorted_sides[0]
#     b = sorted_sides[1]
#     c = sorted_sides[2]
#     if a ** 2 + b ** 2 == c ** 2:
#         print(sorted_sides[1])
#         return True
#     else:
#         print(sorted_sides[1])
#         return False
        


# print(is_rightangled(12, 13, 5))


# 13) If you’re intrigued by why floating point arithmetic is sometimes inaccurate, 
# on a piece of paper, divide 10 by 3 and write down the decimal result. 
# You’ll find it does not terminate, so you’ll need an infinitely long sheet of paper. 
# The representation of numbers in computer memory or on your calculator has similar
#  problems: memory is finite, and some digits may have to be discarded. 
# So small inaccuracies creep in. Try this script:
    
# import math

# a = math.sqrt(2.0)
# print(a, a*a)
# print(a*a == 2.0)
