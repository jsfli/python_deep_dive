for i in range(5):
    print(i)

for x in [(1,2),(3,4),(5,6)]:
    print(x)

for i, j in [(1,2),(3,4),(5,6)]:
    print(j)

for i in range(10):
    if i==3:
        continue
    print(i)

for i in range(10):
    if i==3:
        break
    print(i)

for i in range(8,20):
    print(i)
    if i%7 == 0:
        print('multiple of 7 found')
        break
else:
    print("no multiples of 7 in the range")

for i in range(5):
    print('-------------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print ('divided by 0')
        continue
    finally:
        print('always run')

    print(i)
