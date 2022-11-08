from timeit import timeit
from random import sample
from cycle_sort import cycle_sort, quick_sort, bubble_sort, wiki_cycle_sort
from typing import Callable, List

NUM_ELEMS = 100000

def time_sort(sorts: List[Callable[[List[int]], int]],  
              num_elems: int, min_val: int, max_val: int):

    random_lst = sample(range(min_val, max_val), num_elems)
    sorting_times = {}
    for sort in sorts:
        sort_nme = sort.__name__
        sorting_times[sort_nme] = timeit(f"{sort_nme}({random_lst})", setup=f"from cycle_sort import {sort_nme}",
                                        number=1, globals=locals())
        print(f"{sort_nme}: Number of elements: {num_elems}, time: {sorting_times[sort_nme]}")
    
    sorting_times["timsort"] = timeit(f"{random_lst}.sort()", number=1, globals=locals())
    print(f"timsort: Number of elements: {num_elems}, time: {sorting_times['timsort']}")

    return sorting_times

def compare_write_sorts(sorts: List[Callable[[List[int]], int]],  
              num_elems: int, min_val: int, max_val: int):

    random_lst = sample(range(min_val, max_val), num_elems)
    print(f"Starting List: {random_lst}")
    sorting_writes = {}
    for sort in sorts:
        random_lst_cpy = random_lst.copy()
        sort_nme = sort.__name__
        sorting_writes[sort_nme] = sort(random_lst_cpy)
        print(f"{sort_nme}: Number of elements: {num_elems}, writes: {sorting_writes[sort_nme]}")

if __name__ == "__main__":
    sorts = [cycle_sort, quick_sort, bubble_sort, wiki_cycle_sort]
    # time_sort(sorts, NUM_ELEMS, -10000, 10000)
    compare_write_sorts(sorts, NUM_ELEMS, -100000, 100000)
