from sre_constants import FAILURE


NUM_AUX = 3
NUM_VAR = 13
AUX_VARS = ('a1', 'a2', 'a3')


# Implementation of backtrack algorithm
def backtrack(csp, assignment):
    if len(assignment) == len(csp.variables):
        return assignment
    selected_var = select_unassigned_variable(csp, assignment)
    # print("selected variable", selected_var)

    for value in csp.domains[selected_var]:
        # print("selected val: ", value)
        if is_consistent(csp, assignment, selected_var, value):
            assignment[selected_var] = value
            # removing used value from the domains
            # for var in csp.domains:
                # if selected_var not in aux_vars: # remove only when the selected variable is not aux
                    # if value in csp.domains[var] and var not in aux_vars: # do not remove from the value from aux domain
                        # csp.domains[var].remove(value)
            print(assignment)
            # print(len(assignment))
            # print(csp.domains)
            result = backtrack(csp, assignment)
            if result:
               return result
            assignment.pop(selected_var)
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
        if var not in assignment:
            legal_val_num = get_legal_value_num(csp, assignment, var)
            print(f'Variable {var} has {legal_val_num} legal values left')
            min_remaining_num = min(legal_val_num, min_remaining_num)

    # if the variable has the min remaining values, select it
    for var in csp.domains:
        if get_legal_value_num(csp, assignment, var) == min_remaining_num and var not in assignment:
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
    

def is_consistent(csp, assignment, this_variable, this_value):  # Not started
    # If there is 1 unassigned var in constraint --> consistent
    # If all vars in constraint are assigned:
    #   If constraint true  --> consistent
    #   If constraint false --> inconsistent

    # Check if the value has been used by other vars
    if this_variable not in AUX_VARS and this_value in assignment.values():
        return False

    # for cons in csp.constraints:   # loop thru constraints
    #     sub_values = []            # the assigned values
    #     if this_variable in cons:  # if the selected variable is involved
    #         if check_all_var_is_assigned(cons, assignment, this_variable):
    #             fetch_sub_values(sub_values, cons, assignment, this_value, this_variable)
    #             print("========================")
    #             print("Assignment: ", assignment)
    #             print(f"Checking {this_variable} = {this_value}:")
    #             print("CHECKING")
    #             print(f'{sub_values[0]} + {sub_values[1]} + {sub_values[2]} = {sub_values[3]} + {sub_values[4]} * 10')
    #             if sub_values[0] + sub_values[1] + sub_values[2] != sub_values[3] + sub_values[4] * 10:
    #                 print("FALSE")
    #                 return False
    #             print("TRUE")
    return True


def check_all_var_is_assigned(cons, assignment, this_variable):
    for var in cons:  # try substitude each var with their assigned values
        if var not in assignment and var is not this_variable:
            return False
    return True


def fetch_sub_values(sub_values, cons, assignment, this_value, this_variable):
    for var in cons:  # try substitude each var with their assigned values
        if var == '0':
            sub_values.append(0)
        elif var == this_variable:
            sub_values.append(this_value)
        else:
            sub_values.append(assignment[var])


def get_legal_value_num(csp, assignment, this_var):
    if this_var in AUX_VARS:
        return len(csp.domains[this_var])
    legal_val_num = 0
    for val in csp.domains[this_var]:
        been_used = False
        for var in assignment:
            if var not in AUX_VARS and val == assignment[var]:
                been_used = True
        if not been_used:
            legal_val_num += 1
    return legal_val_num