import matplotlib.pyplot as plt
import numpy as np

def draw(input: list, hull: list):
    x = [point[0] for point in input]
    y = [point[1] for point in input]
    
    if (len(input) < 0):
        plt.grid()
        plt.xticks(np.arange(min(x), max(x)+1, 1.0))
        plt.yticks(np.arange(min(y), max(y)+1, 1.0))
    
    points = plt.scatter(x, y)
    
    x = [point[0] for point in hull]
    y = [point[1] for point in hull]
    x.append(hull[0][0])
    y.append(hull[0][1])
    
    hull_fig = plt.plot(x, y, marker='.', linestyle='-', color='orange')
    
    plt.show()
    
def draw_tangent(input: list, hull: list, pnt: list, tng_pnt: list):
    x = [point[0] for point in input]
    y = [point[1] for point in input]

    if (len(input) < 10):
        plt.grid()
        plt.xticks(np.arange(min(x), max(x)+1, 1.0))
        plt.yticks(np.arange(min(y), max(y)+1, 1.0))

    points = plt.scatter(x, y)

    x = [point[0] for point in hull]
    y = [point[1] for point in hull]
    x.append(hull[0][0])
    y.append(hull[0][1])

    hull_fig = plt.plot(x, y, marker='.', linestyle='-', color='orange')

    line_x = [pnt[0], tng_pnt[0]]
    line_y = [pnt[1], tng_pnt[1]]

    plt.plot(line_x, line_y, linestyle='-', color='red')

    plt.show()