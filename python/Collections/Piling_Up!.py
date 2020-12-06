def judgement(n,nums):
    # l: start from left side, how far can it go?(decreasing)
    l = 0
    while l < n-1:
        if nums[l+1]<=nums[l]:
            l+=1
        else:
            break
    # r: start from right side, how far can it go?(decreasing)
    r = n-1
    while r > 0:
        if nums[r-1]<=nums[r]:
            r-=1
        else:
            break
    # if they meet each other, then the answer is yes, else no.
    if r<=l:
        print('Yes')
    else:
        print('No')

cases = int(input())
for case in range(cases):
    n = int(input())
    nums = list(map(int,input().split()))
    judgement(n,nums)
