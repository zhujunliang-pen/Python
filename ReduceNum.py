import sys;

def reduceNum(n): 
    #print(type(n))   
    #print('{} ='.format(n), end=' ')
    if(type(n) == "int") or n <= 0:
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    result = []
    while n > 1:
        for f in range(2, n + 1):
            if n % f == 0:
                result.append(f)
                n //= f
                break
            elif f == n // 2:
                result.append(n)
                n = 1
                break
            else:
                continue       
            
    #                break
    return result


if __name__ == "__main__":    
    res = reduceNum(5)
    print('{0} ='.format(5), ' * '.join([str(i) for i in res]))
    res = reduceNum(100)
    print('{} ='.format(100), ' * '.join([str(i) for i in res]))