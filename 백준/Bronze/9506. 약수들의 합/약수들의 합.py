while True:
    n = int(input())
    if n == -1:
        break

    num = []
    for i in range (1, n):
        if n % i == 0:
            num.append(i)
    
    if sum(num) == n:
        string = ''
        string = str(n) + " = " + ' + '.join(map(str, num))
        print(string)
    else:
        print(n, "is NOT perfect.")
        