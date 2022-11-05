from cycle_sort import cycle_sort, bubble_sort, quick_sort
from typing import List
from hypothesis import given
from hypothesis.strategies import integers, lists

def brute_force_sort(lst: List[int]):
    lst_copy = lst.copy()
    lst_copy.sort()
    return lst_copy

def matching_sorted_test(lst1: List[int], lst2: List[int]):
    assert len(lst1) == len(lst2)
    for i in range(len(lst1)): assert lst1[i] == lst2[i]

@given(lists(integers()))
def test1_cycle_sort(lst: List[int]):
    lst_sorted = brute_force_sort(lst)
    cycle_sort(lst)
    matching_sorted_test(lst, lst_sorted)

@given(lists(integers()))
def test2_bubble_sort(lst: List[int]):
    lst_sorted = brute_force_sort(lst)
    bubble_sort(lst)
    matching_sorted_test(lst, lst_sorted)

@given(lists(integers()))
def test3_quick_sort(lst: List[int]):
    lst_sorted = brute_force_sort(lst)
    quick_sort(lst)
    matching_sorted_test(lst, lst_sorted)

if __name__ == "__main__":
    import pytest
    pytest.main(['cycle_sort.py'])
