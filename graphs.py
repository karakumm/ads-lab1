import matplotlib.pyplot as plt
from test import test1, test2, test3, test4

def create_graph(dict1, dict2, dict3, dict4):
    dict1 = dict1
    x = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    y1 = []
    for el in dict1.items():
        y1.append(el[1][1])
    plt.plot(x, y1, label='selection sort')

    dict2 = dict2
    y2 = []
    for el in dict2.items():
        y2.append(el[1][1])
    plt.plot(x, y2, label='insertion sort')

    dict3 = dict3
    y3 = []
    for el in dict3.items():
        y3.append(el[1][1])
    plt.plot(x, y3, label='merge sort')

    dict4 = dict4
    y4 = []
    for el in dict4.items():
        y4.append(el[1][1])
    plt.plot(x, y4, label='shell sort')

    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Experiment 4 Comparisons')
    plt.legend()
    plt.yscale('log')
    plt.savefig('ccccc-experiment4.png')
    plt.close()
    plt.show()

create_graph(test1(), test2(), test3(), test4())
