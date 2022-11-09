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
    >>> simplify([[5, 3, 5, 6, 2], [3], [4], [5], [5], [5]])
    [[5, 6, 2], [3], [4]]
    
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

    # >>> equal_perm([[1, 2, 3]], [[1, 2, 3]])
    # True
    # >>> equal_perm([[2, 1, 3]], [[1, 2, 3]])
    # False
    # >>> equal_perm([[1, 3, 2], [1, 3, 2]], [[1, 2, 3]])
    # True
    # >>> equal_perm([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]],\
    #                [[1, 4, 5], [3], [2], [6]])
    # False

    """
    return get_mapping_expr(expr1) == get_mapping_expr(expr2) # Note: order doesn't matter when comparing dicts

def get_mapping_expr(expr: List[List[int]]) -> Dict[int, int]:
    true_expr = simplify(remove_singletons(expr))
    mapping = {}

    for cycle in true_expr: 
        mapping = get_mapping_cycle(cycle, mapping)
    return mapping

def get_mapping_cycle(cycle: List[int], mapping: Dict[int, int]) -> Dict[int, int]:
    for index, elem in enumerate(cycle):
        if index == len(cycle) - 1:
            mapping[elem] = cycle[FIRST_ELEM]
        else: 
            mapping[elem] = cycle[index + 1]
    return mapping

def end_cycle_num(expr: List[List[int]], num: int) -> int:
    for cycle in range(len(expr) -1, -1, -1):
        if num in expr[cycle]:
            num_index = len(expr[cycle]) - list(reversed(expr[cycle])).index(num) - 1
            if num_index == len(expr[cycle]) - 1: num = expr[cycle][0]
            else:
                if cycle == 0: leftover = []
                else: leftover = expr[:cycle]
                leftover.append(expr[cycle][:num_index + 1])
                num = end_cycle_num(leftover, expr[cycle][num_index + 1])
                break # might need to modify into while loop instead
                # num = expr[cycle][num_index + 1]
    
    return num

def remove_dups(lst: List[int]) -> List[int]:
    all_nums = set()

    # basically, add an element to our new list if:
    # - the element is not in our set and...
    # - adding to the set is successful (since set.add() rets None)
    return [elem for elem in lst if not (elem in all_nums or all_nums.add(elem))]

def remove_singletons(lst: List[List[int]]) -> List[List[int]]:
    return [elem for elem in lst if len(elem) > 1]


def cycle_inverse(expr: List[List[int]]) -> List[List[int]]:
    """
    Return the inverse of <expr>.

    # >>> cycle_inverse([[1, 2, 3]])
    # [[3, 2, 1]]
    # >>> equal_perm(cycle_inverse([[1, 3, 2], [1, 3, 2]]), [[2, 1, 3]])
    # True
    # >>> equal_perm(cycle_inverse([[1, 3, 2], [1, 3, 2]]), [[1, 3, 2]])
    # True
    """
    expr_inverse = []
    true_expr = simplify(expr)
    for cycle in true_expr:
        expr_inverse.append(list(reversed(cycle)))
    return expr_inverse

if __name__ == "__main__":
    # print(get_mapping_expr([[2, 1, 3]]))
    # equal_perm([[2, 1, 3]], [[1, 2, 3]])
    # get_mapping_expr([[2, 1, 3]]) == get_mapping_expr([[1, 2, 3]])
    
    import doctest
    doctest.testmod()

    """
    Hypotheses:
    Suppose that p1 is a cyclic permutation. Furthermore suppose that p2 is p1's inverse. Then, 
    - Every 1st, 4th, 7th,... degree of a p2 is p1's identity permutation
    - Every 2rd, 5th, 8th,... degree of a p2 is the inverse of p
    - Every 3th, 6th, 9th,... degree of p2 is p.
    """
    ## test 1
    # test1 = [[1, 3, 2]] => p
    # test1.extend(cycle_inverse([[1, 3, 2]])) # identity permutation => p2
    # test1.extend(cycle_inverse([[1, 3, 2]])) # inverse of [[1, 3, 2]] => [[1, 2, 3]] => p2 ** 2
    # test1.extend(cycle_inverse([[1, 3, 2]])) # back to [[1, 3, 2]] => p2 ** 3
    # test1.extend(cycle_inverse([[1, 3, 2]])) # identity permutation => p2 ** 4
    # test1.extend(cycle_inverse([[1, 3, 2]])) # inverse of [[1, 3, 2]] => p2 ** 5
    # test1.extend(cycle_inverse([[1, 3, 2]])) # back to [[1, 3, 2]] => p2 ** 6
    # print(simplify(test1))

    ## test 2
    # test2 = [[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]] # Note: simplified ver: [[1, 4, 5], [3], [2], [6]]
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # test2.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # print(simplify(test2))

    """
    Hypotheses:
    Suppose that p1 is a cyclic permutation. Then, 
    - Every 1st, 4th, 7th,... degree of a p is p
    - Every 2rd, 5th, 8th,... degree of a p is the inverse of p
    - Every 3th, 6th, 9th,... degree of p is the identity permutation of p.
    """

    ## test 3
    test3 = [[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]] # Note: simplified ver: [[1, 4, 5], [3], [2], [6]]
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # inverse
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # identity
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # bacl to orig
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # inverse
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # identity
    # test3.extend([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]) # back to orig
    # print(simplify(test3))


    ## test 4
    # test4 = [[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]
    # test4.extend(cycle_inverse([[1, 5, 4], [3], [2, 6], [1, 5, 4], [3], [2, 6]]))
    # print(simplify(test4))