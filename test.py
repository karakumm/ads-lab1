import sorts
from sorts import selection_sort, insertion_sort, merge_sort, shell_sort
import time
import math
import random


def time_counter_calculator(lst, sort):
    start1 = time.time()
    comparisons_num = sort(lst.copy())[1]
    end1 = time.time()
    time1 = end1 - start1
    return time1, comparisons_num

def average(results, range):
    total = 0
    for res in results:
        total += res
    average = total / range
    return average

def test1():
    
    selection_dict = {}
    insertion_dict = {}
    merge_dict = {}
    shell_dict = {}

    selection_results, selection_compare = [], []
    insertion_results, insertion_compare = [], []
    merge_results, merge_compare = [], []
    shell_results, shell_compare = [], []

    for size in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        for experiment in range(5):
            lst = [random.randrange(-10000, 10000) for i in range(size)]

            selection_res = time_counter_calculator(lst, selection_sort)
            selection_results.append(selection_res[0])
            selection_compare.append(selection_res[1])

            insertion_res = time_counter_calculator(lst, insertion_sort)
            insertion_results.append(insertion_res[0])
            insertion_compare.append(insertion_res[1])

            start3 = time.time()
            merge_sort(lst.copy())
            end3 = time.time()
            time3 = end3 - start3
            merge_results.append(time3)
            merge_compare.append(sorts.merge_comparisons)
            sorts.merge_comparisons = 0

            shell_res = time_counter_calculator(lst, shell_sort)
            shell_results.append(shell_res[0])
            shell_compare.append(shell_res[1])


        selection_time_average = average(selection_results, 5)
        selection_compare_average = average(selection_compare, 5)
        selection_dict.update({int(math.log(size, 2)): (selection_time_average, selection_compare_average)})

        insertion_time_average = average(insertion_results, 5)
        insertion_compare_average = average(insertion_compare, 5)
        insertion_dict.update({int(math.log(size, 2)): (insertion_time_average, insertion_compare_average)})

        merge_time_average = average(merge_results, 5)
        merge_compare_average = average(merge_compare, 5)
        merge_dict.update({int(math.log(size, 2)): (merge_time_average, merge_compare_average)})

        shell_time_average = average(shell_results, 5)
        shell_compare_average = average(shell_compare, 5)
        shell_dict.update({int(math.log(size, 2)): (shell_time_average, shell_compare_average)})      

        selection_results, selection_compare = [], []
        insertion_results, insertion_compare = [], []
        merge_results, merge_compare = [], []
        shell_results, shell_compare = [], []

    return selection_dict, insertion_dict, merge_dict, shell_dict


def test2():
    selection_dict = {}
    insertion_dict = {}
    merge_dict = {}
    shell_dict = {}

    for size in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        lst = sorted([random.randrange(-10000, 10000) for i in range(size)])

        selection_res = time_counter_calculator(lst, selection_sort)
        selection_dict.update({int(math.log(size, 2)): selection_res})

        insertion_res = time_counter_calculator(lst, insertion_sort)
        insertion_dict.update({int(math.log(size, 2)): insertion_res})

        start3 = time.time()
        merge_sort(lst.copy())
        end3 = time.time()
        time3 = end3 - start3
        merge_dict.update({int(math.log(size, 2)): (time3, sorts.merge_comparisons)})

        shell_res = time_counter_calculator(lst, shell_sort)
        shell_dict.update({int(math.log(size, 2)): shell_res})

        sorts.merge_comparisons = 0

    return selection_dict, insertion_dict, merge_dict, shell_dict


def test3():

    selection_dict = {}
    insertion_dict = {}
    merge_dict = {}
    shell_dict = {}

    for size in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        lst_random = sorted([random.randrange(-10, 10) for i in range(size)])
        lst = lst_random[::-1]

        selection_res = time_counter_calculator(lst, selection_sort)
        selection_dict.update({int(math.log(size, 2)): selection_res})

        insertion_res = time_counter_calculator(lst, insertion_sort)
        insertion_dict.update({int(math.log(size, 2)): insertion_res})

        start3 = time.time()
        merge_sort(lst.copy())
        end3 = time.time()
        time3 = end3 - start3
        merge_dict.update({int(math.log(size, 2)): (time3, sorts.merge_comparisons)})

        shell_res = time_counter_calculator(lst, shell_sort)
        shell_dict.update({int(math.log(size, 2)): shell_res})

        sorts.merge_comparisons = 0

    return selection_dict, insertion_dict, merge_dict, shell_dict


def test4():

    selection_dict = {}
    insertion_dict = {}
    merge_dict = {}
    shell_dict = {}

    selection_results, selection_compare = [], []
    insertion_results, insertion_compare = [], []
    merge_results, merge_compare = [], []
    shell_results, shell_compare = [], []

    for size in [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]:
        for experiment in range(3):
            lst = [random.choice([1, 2, 3]) for i in range(size)]

            selection_res = time_counter_calculator(lst, selection_sort)
            selection_results.append(selection_res[0])
            selection_compare.append(selection_res[1])

            insertion_res = time_counter_calculator(lst, insertion_sort)
            insertion_results.append(insertion_res[0])
            insertion_compare.append(insertion_res[1])

            start3 = time.time()
            merge_sort(lst.copy())
            end3 = time.time()
            time3 = end3 - start3
            merge_results.append(time3)
            merge_compare.append(sorts.merge_comparisons)
            sorts.merge_comparisons = 0

            shell_res = time_counter_calculator(lst, shell_sort)
            shell_results.append(shell_res[0])
            shell_compare.append(shell_res[1])


        selection_time_average = average(selection_results, 3)
        selection_compare_average = average(selection_compare, 3)
        selection_dict.update({int(math.log(size, 2)): (selection_time_average, selection_compare_average)})

        insertion_time_average = average(insertion_results, 3)
        insertion_compare_average = average(insertion_compare, 3)
        insertion_dict.update({int(math.log(size, 2)): (insertion_time_average, insertion_compare_average)})

        merge_time_average = average(merge_results, 3)
        merge_compare_average = average(merge_compare, 3)
        merge_dict.update({int(math.log(size, 2)): (merge_time_average, merge_compare_average)})

        shell_time_average = average(shell_results, 3)
        shell_compare_average = average(shell_compare, 3)
        shell_dict.update({int(math.log(size, 2)): (shell_time_average, shell_compare_average)})      

        selection_results, selection_compare = [], []
        insertion_results, insertion_compare = [], []
        merge_results, merge_compare = [], []
        shell_results, shell_compare = [], []

    return selection_dict, insertion_dict, merge_dict, shell_dict
