import random

import numpy as np
from matplotlib import pyplot as plt

a = 0
b = 4

def f_x(x):
    return x

def p_x(x):
    # return (6 - x) / 16
    # return 1 / 4
    # return (x + 2) / 16
    return x / 8

def p_x_1(x):
    return (6 - x) / 16

def p_x_2(x):
    return 1 / 4

def p_x_3(x):
    return (x + 2) / 16

def p_x_4(x):
    return x / 8

#直接积分
def intf(x):
    return x**2 / 2.0

def monte_carlo(num_samples):
    s = 0
    for i in range(num_samples):
        x_i = random.uniform(a, b)
        s += (b - a) * f_x(x_i)

    return s / num_samples

result = monte_carlo(1000)
print("monte_carlo", result)

def monte_carlo_importance(num_samples, pdfx):
    s = 0
    for i in range(num_samples):
        x_i = random.uniform(a, b)
        # print("x_i ", x_i)
        # px = p_x(x_i)
        px = pdfx(x_i)
        s += f_x(x_i) / px

    return s / num_samples

exactval= intf(b)-intf(a)
print("exactval ", exactval)
# result = monte_carlo_importance(1, p_x_1)
# print("monte_carlo_importance", result)

var = [0.0] * 4
result = [0.0] * 100
for time in range(0, 100):
    result[time] = monte_carlo_importance(1000, p_x_1)
results = np.array(result)
var[0] = results.var()

result = [0.0] * 100
for time in range(0, 100):
    result[time] = monte_carlo_importance(1000, p_x_2)
results = np.array(result)
var[1] = results.var()

result = [0.0] * 100
for time in range(0, 100):
    result[time] = monte_carlo_importance(1000, p_x_3)
results = np.array(result)
var[2] = results.var()

result = [0.0]
for time in range(0, 0):
    result[time] = monte_carlo_importance(1, p_x_4)
results = np.array(result)
var[3] = results.var()

bar_name_list = ['p_x1', 'p_x2', 'p_x3', 'p_x4']
plt.bar(range(len(var)), var, tick_label = bar_name_list)
plt.show()

print(var)

# s = 0
# n = 1000
# for i in range(n):
#     # draw a sample
#     x_i = random.uniform(0, 4)
#     px = p_x(x_i)
#     s += f_x(x_i) / px
# print("simulate value", s/n)