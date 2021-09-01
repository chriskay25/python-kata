def multiples(num):
    if num < 3: return 0
    # m = [n for n in range(3, num) if n % 3 == 0 or n % 5 == 0]
    m = []
    for i in range(3, num):
        if i % 3 == 0 or i % 5 == 0:
            m.append(i)
    result = sum(m)
    print(result)

multiples(15)