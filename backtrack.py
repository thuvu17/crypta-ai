from sre_constants import FAILURE


NUM_AUX = 3
NUM_VAR = 13


# Implementation of backtrack algorithm
def backtrack(csp, assignment):
    if len(assignment) == len(csp.variables):
        return assignment
    selected_var = select_unassigned_variable(csp, assignment)
    print("selected variable", selected_var)

    for value in csp.domains[selected_var]:
        print("selected val: ", value)
        if is_consistent(csp, assignment, selected_var, value):
            assignment[selected_var] = value
            # removing used value from the domains
            for var in csp.domains.keys():
                if selected_var != 'a1' and selected_var != 'a2' and selected_var != 'a3': # remove only when the selected variable is not aux
                    if value in csp.domains[var] and var != 'a1' and var != 'a2' and var != 'a3': # do not remove from the value from aux domain
                        csp.domains[var].remove(value)
            print(assignment)
            print(len(assignment))
            print(csp.domains)
            result = backtrack(csp, assignment)
            if result:
               return result
            assignment.pop('var')
    return FAILURE


def select_unassigned_variable(csp, assignment):
    # apply MRV then degree heuristic
    vars_after_MRV = do_minimum_remaining_value(csp, assignment)

    if len(vars_after_MRV) != 1:  # if there is more than one variables with the same MRV
        selected_var = do_degree_heuristic(csp, assignment, vars_after_MRV)
    else: 
        selected_var = vars_after_MRV[0]

    return selected_var


def do_minimum_remaining_value(csp, assignment):  # good now #######################################
    selected_vars = []
    min_remaining_num = 10  # the max number of remaining values that a variable can have

    for var in csp.variables:
        # if var is not assigned yet and its domain size is smaller than the min
        if var not in assignment.keys() and len(csp.domains[var]) < min_remaining_num:
            min_remaining_num = len(csp.domains[var])

    # if the variable has the min remaining values, select it
    for var in csp.domains.keys():
        if len(csp.domains[var]) == min_remaining_num and var not in assignment.keys():
            selected_vars.append(var)

    return selected_vars


def do_degree_heuristic(csp, assignment, variables): # not sure exactly how it works##############
    # [var1, var2] --> [#constraints1, #constraints2]
    cons_on_vars = []
    for i in range(len(variables)):
        cons_num = 0
        for cons in csp.constraints:  # loop thru the constraints
            if variables[i] in cons:  # if the variable is in the constraint
                # is_unassigned = False
                # for var in constraint:
                #    if var not in assignment.keys():  # if there is unassigned variables
                #        is_unassigned = True          # the constr
                # if is_unassigned:
                cons_num += 1
        cons_on_vars.append(cons_num)
    max_cons_num = max(cons_on_vars)
    max_cons_index = cons_on_vars.index(max_cons_num)
    return variables[max_cons_index]
    

def is_consistent(csp, assignemnt, variable, value):  # Not started
    # If there is 1 unassigned var in constraint --> consistent
    # If all vars in constraint are assigned:
    #   If constraint true  --> consistent
    #   If constraint false --> inconsistent
    
    # Use try-except
    return True
