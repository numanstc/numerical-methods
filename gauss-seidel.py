# 3*x1-0.1*x2-0.2*x3 = 7.85
# 0.1*x1+7*x2-0.3*x3 = -19.3
# 0.3*x1-0.2*x2+10*x3 = 71.4

# x1 = (7.85 +0.1*x2 + 0.2*x3)/3
# x2 = (-19.3 - 0.1*x1 + 0.3*x3)/7
# x3 = (71.4 - 0.3*x1 + 0.2*x2)/10
x2, x3 = 0, 0
for i in range(10):
    x1 = (7.85 +0.1*x2 + 0.2*x3)/3
    x2 = (-19.3 - 0.1*x1 + 0.3*x3)/7
    x3 = (71.4 - 0.3*x1 + 0.2*x2)/10
print(x1,x2,x3)
