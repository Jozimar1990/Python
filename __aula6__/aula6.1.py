for a in range(1,9):
    print(f'produto {a}')
    for b in range(1,9):
        print(f' {a} X {b} = {a*b}')

for a in range(1,9):
    #print('produto |{:^5}|'.format(a))
    for b in range(1,9):
        print(f' |{a:^5} X {b:^5}| = {a*b:<5}')