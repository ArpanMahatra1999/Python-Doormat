NM = input()
nm = NM.split(" ")
N = int(nm[0])
M = int(nm[1])
for i in range(N):
    for j in range(M):
        if i == int(N / 2):
            if j == int(M / 2) - 3:
                print('W', end='')
            elif j == int(M / 2) - 2:
                print('E', end='')
            elif j == int(M / 2) - 1:
                print('L', end='')
            elif j == int(M / 2):
                print('C', end='')
            elif j == int(M / 2) + 1:
                print('O', end='')
            elif j == int(M / 2) + 2:
                print('M', end='')
            elif j == int(M / 2) + 3:
                print('E', end='')
            else:
                print('-', end='')
        elif i > int(N / 2):
            if j == int(M / 2):
                print('|', end='')
            elif j > int(M / 2) and (j - int(M / 2)) % 3 == 0 and (j - int(M / 2)) / 3 + (i - int(N / 2)) <= int(N / 2):
                print('|', end='')
            elif j > int(M / 2) and (
                    (j + 1 - int(M / 2)) % 3 == 0 and (j + 1 - int(M / 2)) / 3 + (i - int(N / 2)) <= int(N / 2) or (
                    j - 1 - int(M / 2)) % 3 == 0 and (j - 1 - int(M / 2)) / 3 + (i - int(N / 2)) <= int(N / 2)):
                print('.', end='')
            elif j < int(M / 2) and (int(M / 2) - j) % 3 == 0 and (int(M / 2) - j) / 3 + (i - int(N / 2)) <= int(N / 2):
                print('|', end='')
            elif j < int(M / 2) and (
                    (int(M / 2) - (j + 1)) % 3 == 0 and (int(M / 2) - (j + 1)) / 3 + (i - int(N / 2)) <= int(N / 2) or (
                    int(M / 2) - (j - 1)) % 3 == 0 and (int(M / 2) - (j - 1)) / 3 + (i - int(N / 2)) <= int(N / 2)):
                print('.', end='')
            else:
                print('-', end='')
        elif i < int(N / 2):
            if j == int(M / 2):
                print('|', end='')
            elif j > int(M / 2) and (j - int(M / 2)) % 3 == 0 and (j - int(M / 2)) / 3 + (int(N / 2) - i) <= int(N / 2):
                print('|', end='')
            elif j > int(M / 2) and (
                    (j + 1 - int(M / 2)) % 3 == 0 and (j + 1 - int(M / 2)) / 3 + (int(N / 2) - i) <= int(N / 2) or (
                    j - 1 - int(M / 2)) % 3 == 0 and (j - 1 - int(M / 2)) / 3 + (int(N / 2) - i) <= int(N / 2)):
                print('.', end='')
            elif j < int(M / 2) and (int(M / 2) - j) % 3 == 0 and (int(M / 2) - j) / 3 + (int(N / 2) - i) <= int(N / 2):
                print('|', end='')
            elif j < int(M / 2) and (
                    (int(M / 2) - (j + 1)) % 3 == 0 and (int(M / 2) - (j + 1)) / 3 + (int(N / 2) - i) <= int(N / 2) or (
                    int(M / 2) - (j - 1)) % 3 == 0 and (int(M / 2) - (j - 1)) / 3 + (int(N / 2) - i) <= int(N / 2)):
                print('.', end='')
            else:
                print('-', end='')
        else:
            pass
    print('')
