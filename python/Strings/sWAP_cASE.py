def swap_case(s):
    ss=''
    for i in s:
        if ord('a')<=ord(i)<=ord('z'):
            ss += chr(ord(i)-32)
        elif ord('A')<=ord(i)<=ord('Z'):
            ss += chr(ord(i)+32)
        else:
            ss += i
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
