if __name__ == '__main__':
    students = []
    n = int(input())
    name = input()
    score = float(input())
    # mins = [lowest, 2nd lowest]
    mins = [score, score]
    #names = [list of name with lowest score, list of name with 2nd lowest score]
    names = [[name],[name]]
    i=1
    # find two different scores
    while i<n:
        name = input()
        score = float(input())
        if score!=mins[0]:
            if score>mins[0]:
                mins[1] = score
                names[1] = [name]
            else:
                mins[0] = score
                names[0], names[1] = [name], names[0]
            i+=1
            break
        names[0].append(name)
        i+=1
    # update mins
    while i<n:
        name = input()
        score = float(input())
        if score <= mins[1]:
            if score == mins[1]:
                names[1].append(name)
            elif score > mins[0]:
                mins[1] = score
                names[1] = [name]
            elif score == mins[0]:
                names[0].append(name)
            else:
                mins[0], mins[1] = score, mins[0]
                names[0], names[1] = [name], names[0]
        i+=1
    ans = sorted(names[1])
    print('\n'.join(ans))
