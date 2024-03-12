import subprocess
import time
import service.helper as hlpr
import service.graph as grph

import algorithms.graham_scan as gs
import algorithms.chans_alg as ch

def find_tangent_linear(pnt: list, hull: list):
    if len(hull) == 1:
        return hull[0]
    
    curr = 0 
    
    while not (ch.pnt_greater(pnt, hull[curr], hull[(curr + 1) % len(hull)]) and ch.pnt_greater(pnt, hull[curr], hull[curr - 1])):
        curr += 1
        
    return hull[curr]

# -----------------------------------------------------

# pnts = hlpr.generate_points_circle(1_000, 1_000_000)
# hull = gs.graham_scan(pnts)
# grph.draw(pnts, hull)

# start_pnt = [0, 0]
# tngnt_pnt = find_tangent_linear(start_pnt, hull)
# tngnt_pnt = ch.find_tangent(start_pnt, hull)
# grph.draw_tangent(hull, hull, start_pnt, tngnt_pnt)

# -----------------------------------------------------

# кол-во шагов
loops = 10
# кол-во итераций для каждого шага
iters = 20
# стартовое число точек
number = 3
# величина шага
step = 5000

time1 = []
time2 = []

# точка из которой будет найдена касатльеная
start_pnt = [0, 0]

for _ in range(loops):
    print(f'{number / (loops * step) * 100:.2f} %')
    
    delta1 = 0
    delta2 = 0
    
    for _ in range(iters):
        input_data = hlpr.generate_points_circle(number, 1_000_000)
        
        start = time.time()
        find_tangent_linear(start_pnt, input_data)
        end = time.time()
        
        delta1 += end - start
        
        start = time.time()
        ch.find_tangent(start_pnt, input_data)
        end = time.time()
        
        delta2 += end - start
    
    time1.append([number, delta1 / iters])
    time2.append([number, delta2 / iters])
    
    number += step

hlpr.write_test('chans_test/linear_test.txt', time1)
hlpr.write_test('chans_test/binary_test.txt', time2)

print('100.00 %')

subprocess.run(['python', 'service/build_graph_chans.py'])