def minion_game(string):
    l = len(string)
    vowels = {'A','E','I','O','U'}
    scores = [0, 0]
    for i in range(l):
        if string[i] in vowels:
            scores[1] += l-i
        else:
            scores[0] += l-i
    if scores[0]>scores[1]:
        print('Stuart', scores[0])
    elif scores[0]==scores[1]:
        print('Draw')
    else:
        print('Kevin', scores[1])

if __name__ == '__main__':
    s = input()
    minion_game(s)
