N = int(input().split()[0])

for i in range(N//2):
    print(('.|.'*(2*i+1)).center(3*N,'-'))
print('WELCOME'.center(3*N,'-'))
for i in range(N//2):
    print(('.|.'*(N-2-2*i)).center(3*N,'-'))
