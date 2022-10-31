from typing import Dict, List

FIRST_ELEM = 0

def simplify(expr: List[List[int]]) -> List[List[int]]:
    """
    Simplify <expr>, where <expr> is a list of cycles, starting from <expr>'s
    first element.
    
    >>> simplify([])
    []
    >>> simplify([[1, 3, 2], [1, 3, 2]])
    [[1, 2, 3]]
    >>> simplify([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]])
    [[1, 4, 5], [3], [2], [6]]
    
    """
    if expr == []: return []

    simplified_expr = []
    curr_cycle = []
    all_nums = []

    first_cycle = expr[FIRST_ELEM]
    curr_elem = first_cycle[FIRST_ELEM]
    curr_cycle.append(curr_elem)

    for cycle in expr: all_nums.extend(cycle)
    all_nums = remove_dups(all_nums)
    all_nums.remove(curr_elem)

    while curr_elem != None:
        elem_insert = end_cycle_num(expr, curr_elem)
        if elem_insert in curr_cycle:
            if curr_cycle: 
                simplified_expr.append(curr_cycle)
            
            curr_cycle = []
            
            if all_nums: 
                curr_elem = all_nums[FIRST_ELEM]
            else: 
                curr_elem = None
        else:
            curr_cycle.append(elem_insert)
            all_nums.remove(elem_insert)
            curr_elem = elem_insert

    return simplified_expr

def equal_perm(expr1: List[List[int]], expr2: List[List[int]]) -> bool:
    """
    Return True if <expr1>'s elements have the same mapping as <expr2>.
    Return False otherwise.

    >>> equal_perm([[1, 2, 3]], [[1, 2, 3]])
    True
    >>> equal_perm([[2, 1, 3]], [[1, 2, 3]])
    False
    >>> equal_perm([[2, 1, 3]], [[1, 2, 3]])
    False
    >>> equal_perm([[1, 3, 2], [1, 3, 2]], [[1, 2, 3]])
    False
    >>> equal_perm([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]],\
                   [[1, 4, 5], [3], [2], [6]])
    False

    """
    get_mapping(expr1) == get_mapping(expr2) # Note: order doesn't matter when comparing dicts

def get_mapping(expr: List[List[int]]) -> Dict[int, int]:
    true_expr = simplify(remove_singletons(expr))
    mapping = {}

    for cycle in true_expr:
        for index, elem in enumerate(cycle):
            if index == len(cycle) - 1:
                mapping[elem] = cycle[FIRST_ELEM]
            else: 
                mapping[elem] = cycle[index + 1]
    return mapping

def end_cycle_num(expr: List[List[int]], num: int) -> int:
    for cycle in range(len(expr) -1, -1, -1):
        if num in expr[cycle]:
            num_index = expr[cycle].index(num)
            if num_index == len(expr[cycle]) - 1: num = expr[cycle][0]
            else: num = expr[cycle][num_index + 1]
    
    return num

def remove_dups(lst: List[int]) -> List[int]:
    all_nums = set()

    # basically, add an element to our new list if:
    # - the element is not in our set and...
    # - adding to the set is successful (since set.add() rets None)
    return [elem for elem in lst if not (elem in all_nums or all_nums.add(elem))]

def remove_singletons(lst: List[List[int]]) -> List[List[int]]:
    return [elem for elem in lst if len(elem) > 1]

if __name__ == "__main__":
    equal_perm([[2, 1, 3]], [[1, 2, 3]])
    
    # import doctest
    # doctest.testmod()
