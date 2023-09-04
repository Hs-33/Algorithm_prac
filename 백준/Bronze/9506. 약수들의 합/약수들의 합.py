yak = []
while True:
    num = int(input())
    if num == -1:
        break
    else:
        for i in range(1,num+1):
            if num%i == 0:
                yak.append(i)

        if num == sum(yak[:-1]):
            print('{} = {}'.format(num," + ".join([str(i) for i in yak[:-1]])))
        else:
            print(num,'is NOT perfect.')
    yak = []