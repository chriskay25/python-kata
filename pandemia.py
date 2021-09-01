def pandemia(s):
    population = [p for p in s if p != 'X']
    continents = s.split('X')
    infected = 0
    for continent in continents:
        if '1' in continent: 
            infected += len(continent)
    result = 100 * infected/len(population)
    print(result)

pandemia('01000000X000X011X0X') 
#=>      '11111111X000X111X0X'