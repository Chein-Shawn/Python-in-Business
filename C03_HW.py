def CournotEq(a, c1, c2, n):
    # iteration 0: entering the market
    q1 = list()
    q1.append((a - c1) / 2)
    q2 = list()
    q2.append(max((a - q1[0] - c2) / 2, 0))

    # in each iteration, respond once
    for i in range(n):
        q1Next = max((a - q2[i] - c1) / 2, 0)
        q1.append(q1Next)
        q2Next = max((a - q1Next - c2) / 2, 0)
        q2.append(q2Next)
    return q1, q2

a = 10.0
c1 = 1.0
c2 = 3.0
n = 10
q1, q2 = CournotEq(a, c1, c2, n)
