NUM_AUX = 3
NUM_VAR = 13


# Implementation of backtrack algorithm
def backtrack(csp, assignment):
    if len(assignment) == NUM_VAR + NUM_AUX:
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in csp.domains[var]:
        if is_consistent(csp, value):
            assignment[var] = value
            result = backtrack(csp, assignment)
            if result:
                return result
            assignment.pop('var')
    return False


def select_unassigned_variable(csp, assignment):
    # apply MRV then degree heuristic
    selected_var = do_minimum_remaining_value(csp, assignment)
    return selected_var


def do_minimum_remaining_value(csp, assignment):
    selected_vars = []
    min_remaining_num = 10
    for var in csp.variables:
        if var not in assignment.keys() and len(csp.domains[var]) < min_remaining_num:
            min_remaining_num = len(csp.domains[var])
    for var in csp.domains.keys():
        if len(csp.domains[var]) == min_remaining_num:
            selected_vars.append(var)

    return selected_vars


def do_degree_heuristic(csp, variables):
    return
    

def is_consistent(csp, val):
    # if value when added with curr assignment satisfies the constraints
    return
