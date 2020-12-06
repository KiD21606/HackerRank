'''
1. username@websitename.extension
2. The username can only contain "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".
3. The website name can only have letters and digits.
4. The maximum length of the extension is 3. 
'''
def fun(s):
    # return True if s is a valid email, else return False
    u = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_")
    w = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") 
    username, _, s = s.partition('@')
    if (set(username) - u != set()) or (len(username)==0):
        return False
    websitename, _, extension = s.partition('.')
    if (set(websitename) - w != set()) or (len(websitename)==0):
        return False
    if not (3>=len(extension)>0):
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
