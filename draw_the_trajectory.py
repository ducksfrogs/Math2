'''
Draw the trajectory of body in projectile motion
'''

from matplotlib import pyplot as plt

import math

def draw_graph(x, y):
    plt.plot(x,y)
    plt.xlabel('x-cordinate')
    plt.ylabel('y-cordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    numbers = []
    while start <  final:
        numbers.append(start)
        start = start + interval
    return numbers
def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    #Time of flight
    t_flight = 2*u*math.sin(theta)/g
    #find time intervals
    intervals = frange(0, t_flight, 0.001)
    #list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity(m/s):'))
        theta = float(input('EEnter the angle of projection (degrees):'))
    except ValueError:
        print('You enterd an invaild input')
    else:
        draw_trajectory(u, theta)
        plt.show()

