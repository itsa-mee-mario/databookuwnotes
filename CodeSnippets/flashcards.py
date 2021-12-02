Q, A = [] , []
while True:
    Q.append( input("Q:") )
    if Q == '0':
        break
    A.append(input("A:"))


for q, a in zip(Q, A):
    print("Q:\n", q)
    print("A:\n", a)
    print("\n"*3)