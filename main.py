import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]_-+=@!.,*/{}"

all = lower+upper+numbers+symbols

length = int(input("[+] Enter the strength of the password (must be more than 8)"))
if length< 8:
    print("[+] Length of password is weak please give length is more then 8")
else:
    password = "".join(random.sample(all, length))
    print(password)

