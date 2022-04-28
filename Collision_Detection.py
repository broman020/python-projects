# LAB: TUPLES AND STRINGS
# COLLISION DETECTION OF BALLS
# Many games have complex physics engines, and one major function of these engines is to figure out if two objects are colliding. Weirdly-shaped objects are often 
# approximated as balls. In this problem, we will figure out if two balls are colliding.
# We will think in 2D to simplify things, though 3D isn't different conceptually. For calculating a collision, we only care about a ball's position in space and its size. 
# We can store position with its center x-y-coordinates, and we can use its radius for size. So a ball is a tuple of (x, y, r)
# To figure out if two balls are colliding, we need to compute the distance between their centers, then see if this distance is less than the sum of their radii. 
# If so, they are colliding.
# Write a function that takes two balls and computes if they are colliding. Then call the function with two sets of balls. 
# The first set is (0, 0, 1) and (3, 3, 1); these should NOT be colliding. The second set is (5, 5, 2) and (2, 8, 3); these should be colliding.



from math import *

# Defined functions that obtain the x-coordinate, y-coordinate, and radius of each ball.
def get_x(ball):
    return ball[0]

def get_y(ball):
    return ball[1]

def get_r(ball):
    return ball[2]

# Defined a function that calculates the distance between the centers of two balls.
def distance(x1,x2,y1,y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Defined a function that takes the x-coordinate, y-coordinate, and radius of two balls, uses the distance function to calculate the distance between their centers, 
# adds up their radii, and returns a true statement if the distance is smaller than or equal to the sum of the radii
def Collision(ball_1, ball_2):
    d = distance(get_x(ball_1),get_x(ball_2),get_y(ball_1),get_y(ball_2))
    radii_sum = get_r(ball_1) + get_r(ball_2)
    return d <= radii_sum

# If the distance between the centers of the balls is smaller than or equal to the radii, the user will be told the balls collided. 
# Otherwise, they will be told the balls have avoided each other.
a = 0,0,1
b = 3,3,1

if Collision(a,b):
    print("Oops! The balls collided!")
else:
    print("The balls have avoided each other!")


a = 5,5,2
b = 2,8,3

if Collision(a,b):
    print("Oops! The balls collided!")
else:
    print("The balls have avoided each other!")