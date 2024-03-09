import math

# от точки1 к точке2 поворот против часовой стрелки    
def ccw(start_pnt: list, pnt1:list, pnt2: list):
    x1, y1 = pnt1[0] - start_pnt[0], pnt1[1] - start_pnt[1]
    x2, y2 = pnt2[0] - start_pnt[0], pnt2[1] - start_pnt[1]
    if x1 * y2 - x2 * y1 > 0:
        return True
    else:
        return False

# нахождение угла между начальной точкой и точкой из множества
def angle(start_pnt: list, pnt: list):
    x, y = pnt[0] - start_pnt[0], pnt[1] - start_pnt[1]
    if x == y == 0: return -2
    return math.atan2(y, x)  

# длинна отрезка
def distance(start_pnt: list, end_pnt: list):
    x, y = end_pnt[0] - start_pnt[0], end_pnt[1] - start_pnt[1]
    return x**2 + y**2 

def graham_scan(input_pnts: list):
    ans = [min(input_pnts, key=lambda pnt: (pnt[0], pnt[1]))]
    
    pnts = sorted(input_pnts, key=lambda pnt: (angle(ans[0], pnt), distance(ans[0], pnt)))
    
    for i in range(1, len(pnts)):
        while (len(ans) > 1 and not ccw(ans[-2], ans[-1], pnts[i])):
            ans.pop(-1)
        ans.append(pnts[i])
        
    return ans