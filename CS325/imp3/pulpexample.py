from pulp import *

def pulp_test():

    #define variables: 0 <= x <= 3 and 0 <= y <= 1
    x = LpVariable('x', 0, 3)
    y = LpVariable('y', 0, 1)

    #define a new LP Problem
    prob = LpProblem('My Problem', LpMaximize)

    #add a constraint
    #the <= tells pulp this is a contraint not an objective
    prob += x + y <= 2

    #define the objective
    prob += -4*x + y

    #call to solve
    status = prob.solve()

    #print the results
    print LpStatus[status]
    print value(x)
    print value(y)

def main():

    pulp_test()

if __name__ == '__main__':
    main()
