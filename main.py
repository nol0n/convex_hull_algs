import service.helper as hlpr
import service.graph as grph
import subprocess

import algorithms.jarvis_march as jm
import algorithms.graham_scan as gs
import algorithms.quick_hull as qh
import algorithms.chans_alg as ch

import time as time

# pnt = [1, 1]
# input_data = srv.read_file("test.txt")
# hull = ch.chans_hull(input_data)
# tangent = ch.find_tangent(pnt, hull)
# print(hull)
# print(f'{pnt} -> {tangent}')
# grph.draw_tangent(input_data, hull, pnt, tangent)

# 1 - проверка алгоритмов
# 2 - для построения графиков
# 3 - проверка на заданных данных
test = 3

if test == 1 or test == 3:
    output_data_file = "main_files/output.txt"
    test_data = "main_files/input.txt"

    if test == 1:
        input_data = hlpr.generate_points_square(15)
        hlpr.write_test(test_data, input_data)
    if test == 3:
        input_data = hlpr.read_file(test_data)
        
    answer = []

    answer.append(jm.jarvis_march(input_data))
    answer.append(gs.graham_scan(input_data))
    answer.append(qh.quick_hull(input_data))
    answer.append(ch.chans_hull(input_data))

    hlpr.write_file(output_data_file, answer)

    grph.draw(input_data, answer[3])

if test == 2:
    # кол-во шагов
    loops = 25
    # кол-во итераций для каждого шага
    iters = 20
    # стартовое число точек
    number = 3
    # величина шага
    step = 100
    
    time1 = []
    time2 = []
    time3 = []
    time4 = []
    for _ in range(loops):
        print(f'{number / (loops * step) * 100:.2f} %')
        
        delta1 = 0
        delta2 = 0
        delta3 = 0
        delta4 = 0
        
        for _ in range(iters):
            input_data = hlpr.generate_points_square(number)
            
            start = time.time()
            jm.jarvis_march(input_data)
            end = time.time()
            
            delta1 += end - start
            
            start = time.time()
            gs.graham_scan(input_data)
            end = time.time()
            
            delta2 += end - start
            
            start = time.time()
            qh.quick_hull(input_data)
            end = time.time()
            
            delta3 += end - start

            start = time.time()
            ch.chans_hull(input_data)
            end = time.time()
            
            delta4 += end - start
        
        time1.append([number, delta1 / iters])
        time2.append([number, delta2 / iters])
        time3.append([number, delta3 / iters])
        time4.append([number, delta4 / iters])
        
        number += step
    
    hlpr.write_test("service/results/jarvis_test.txt", time1)
    hlpr.write_test("service/results/graham_test.txt", time2)
    hlpr.write_test("service/results/quick_test.txt", time3)
    hlpr.write_test("service/results/chans_test.txt", time4)
    
    print('100.00 %')

    subprocess.run(['python', 'service/build_graph.py'])
