import pulp
import csv
import numpy as n
import matplotlib.pyplot as plt

#Define variables
s = pulp.LpVariable("s", 0, None)
x0 = pulp.LpVariable("x0", 0, None)
x1 = pulp.LpVariable("x1", 0, None)
x2 = pulp.LpVariable("x2", 0, None)
x3 = pulp.LpVariable("x3", 0, None)
x4 = pulp.LpVariable("x4", 0, None)
x5 = pulp.LpVariable("x5", 0, None)

#Define problem
prob = pulp.LpProblem("bestFit", pulp.LpMinimize)

#Define instance
t = []

with open('Corvallis.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
	for row in reader:
		t.append((float(row['average']), int(int(row['day']))))

#Add contraints
b1 = 365.25
b2 = 365.25 * 10.7
for i in t:
	d = i[1]
	a = i[0]
	top = 2*n.pi*d  #saving space
	prob += x0+x1*d + \
	x2*n.cos(top/b1) + \
	x3*n.sin(top/b1) + \
	x4*n.cos(top/b2) + \
	x5*n.sin(top/b2) - a-s <= 0
	prob += -(x0+x1*d + \
		x2*n.cos(top/b1) + \
		x3*n.sin(top/b1) + \
		x4*n.cos(top/b2) + \
		x5*n.sin(top/b2) - a) - s <= 0


#Add objective, just minimizing s
prob += s

ans = prob.solve()
print ans
print "Status: ", pulp.LpStatus[prob.status]
print "Values: "
v = [pulp.value(x0),pulp.value(x1),pulp.value(x2),pulp.value(x3),pulp.value(x4),pulp.value(x5)]
for i in range(0,6):
	print "x",i, " = ", v[i]

xplot = n.linspace(0, 22305,22305)
yplot = v[0]+v[1]*xplot+v[2]*n.cos((2*n.pi*xplot)/b1)+v[3]*n.sin((2*n.pi*xplot)/b1)+v[4]*n.cos((2*n.pi*xplot)/b2)+v[5]*n.sin((2*n.pi*xplot)/b2)
xdata = [point[1] for point in t]
ydata = [point[0] for point in t]
plt.figure(1, figsize = (6,4) )
plt.plot(xplot, yplot, 'b-', label='LP Solution')
plt.plot(xdata, ydata, 'r.', label="Points")
plt.xlabel("day")
plt.ylabel("average temperature (C)")
plt.legend(loc='upper right')
plt.axhline(color = 'gray', zorder=-1)
plt.axvline(color = 'gray', zorder=-1)

# save plot to file
plt.savefig("TemperatureFit.pdf")

# display plot on screen
plt.show()