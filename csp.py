NUM_AUX = 3
NUM_VAR = 13


class CSP:
    def __init__(self, input_data):
        self.variables = self.init_variables(input_data)
        self.domains = self.init_domains(input_data)
        self.constraints = self.init_constraints(input_data)

    def init_variables(self, input):
        variables = []
        # domains of auxiliary
        for i in range(0,NUM_VAR):
            if input[i] not in variables:
                    variables.append(input[i])
        # domains of auxiliary
        variables.extend(['a1', 'a2', 'a3'])
        return tuple(variables)
        
    def init_domains(self, input):
        domains = {}
        # domains of auxiliary
        for i in range(0,NUM_VAR):
            if i + 1 != 1 and i + 1 != 5 and i + 1 != 9:
                if input[i] not in domains.keys():
                    domains[input[i]] = [x for x in range(0, 10)]
        domains[input[0]] = [x for x in range(1, 10)]
        domains[input[4]] = [x for x in range(1, 10)]
        domains[input[8]] = [1]
        # domains of auxiliary
        domains['a1'] = [0, 1]
        domains['a2'] = [0, 1]
        domains['a3'] = [0, 1]
        return domains

    def init_constraints(self, input_data):
        # x4 + x8 + 0 = x13 + 10 * a1
        # x3 + x7 + a1 = x12 + 10 * a2
        # x2 + x6 + a2 = x11 + 10 * a3
        # x1 + x5 + a3 = x10 + 10 * x9

        # Notation: x(n) --> input(x-1) and a(m)
        c1 = (input_data[3], input_data[7], 0, input_data[12], 'a1')
        c2 = (input_data[2], input_data[6], 'a1', input_data[11], 'a2')
        c3 = (input_data[1], input_data[5], 'a2', input_data[10], 'a3')
        c4 = (input_data[0], input_data[4], 'a3', input_data[9], input_data[8])
        return (c1, c2, c3, c4)