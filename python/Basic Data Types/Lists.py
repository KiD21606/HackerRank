if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        task = input().split()
        cmd = task[0]
        params = task[1:]
        if cmd == 'print':
            print(l)
        else:
            eval('l.'+cmd+'('+','.join(params)+')')  
    
    
    '''
    # worthest method: list all of the commands.
    l = []
    for _ in range(int(input())):
        task = input().split()
        movement = task[0]
        if movement == 'print':
            print(l)
        elif movement == 'sort':
            l.sort()
        elif movement == 'pop':
            l.pop()
        elif movement == 'reverse':
            l.reverse()
        else:
            param = list(map(int,task[1:]))
            if movement == 'insert':
                l.insert(param[0],param[1])
            elif movement == 'remove':
                l.remove(param[0])
            elif movement == 'append':
                l.append(param[0])
            else:
                print('unknown movement:',movement)
    '''
