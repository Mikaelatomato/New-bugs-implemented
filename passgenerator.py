def passgen():
    import random
    import string
    securitylevelask = str
    securitylevel_dict = {"weak": 1, "strong": 2}
    while securitylevelask != "weak" and securitylevelask != "strong":
        securitylevelask = input("type the securitylevel for your password: weak / strong: ")
    pass_chars = int(input("type the # of characters for your password: "))
    securitylevel = securitylevel_dict.get(securitylevelask)
    if securitylevel == 1:
        weakpassword = ''.join(random.choices(string.ascii_lowercase + string.digits, k=pass_chars))
        return print("your password is: ", weakpassword)
    else:
        strongpassword = ''.join(random.choices(string.ascii_letters + string.digits, k=pass_chars))
        return print("your password is: ", strongpassword)
passgen()
