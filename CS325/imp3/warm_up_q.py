import pulp

#Define variables
s = pulp.LpVariable("s", 0, None)
a = pulp.LpVariable("a", 0, None)
b = pulp.LpVariable("b", 0, None)

#Define problem
prob = pulp.LpProblem("bestFit", pulp.LpMinimize)

#Define instance
t = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]

#Add contraints
for i in t:
	prob += a*(i[0]) + b - i[1] - s <= 0
	prob += -(a*(i[0]) + b - i[1]) - s <= 0

#Add objective, just minimizing s
prob += s

ans = prob.solve()
prob
print ans
print "Status: ", pulp.LpStatus[prob.status]
print "Line of best fit: y = ", pulp.value(a),"x + ", pulp.value(b)