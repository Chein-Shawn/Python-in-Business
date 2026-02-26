def CournotEq(a, b, c1, c2, n):
    # iteration 0: entering the market
    q1 = list()
    q1.append((a + c1) / 2)
    q2 = list()
    q2.append(max((a + b * q1[0] + c2) / 2, 0))

    # in each iteration, respond once
    for i in range(n):
        q1Next = max((a + b * q2[i] + c1) / 2, 0)
        q1.append(q1Next)
        q2Next = max((a + b * q1Next + c2) / 2, 0)
        q2.append(q2Next)
    return q1, q2

a, b, c1, c2, n = input().strip().split(",")
a, b, c1, c2 = float(a), float(b), float(c1), float(c2)
n = int(n)
q1, q2 = CournotEq(a, b, c1, c2, n)

print("%0.2f %0.2f" %(q1[n], q2[n]))
