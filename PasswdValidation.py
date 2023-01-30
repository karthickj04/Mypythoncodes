import logging


logging.basicConfig(filename='pswdvalid.log', level=logging.DEBUG)


def passwdlencheck(passwd):
    logging.info("Evaluating if password having minimum length of 15 digit")
    if len(passwd) >= 15:
        len1 = True

    else:
        len1 = False

    return len1


def passwdsplchk(passwd):
    logging.info("Evaluating if password has Mandatory spl Characters")
    char = {'@', '$', '_'}
    for c in passwd:
        if c in char:
            spl = True
            break
        else:
            spl = False

    return spl


def passwducchk(passwd):
    logging.info("Evaluating if upper case is used")
    for i in passwd:
        if i.isupper():
            upchk = True
            break
        else:
            upchk = False

    return upchk


def passwdlcchk(passwd):
    logging.info("Evaluating if Lower case is used")
    for i in passwd:
        if i.islower():
            lcchk = True
            break
        else:
            lcchk = False

    return lcchk


def numbrchk(passwd):
    logging.info("Evaluating if Mandatory Digit is used")
    for i in passwd:
        if i.isdigit():
            dcchk = True
            break
        else:
            dcchk = False

    return dcchk


def spacechk(passwd):
    logging.info("Evaluating if space is used")
    for i in passwd:
        if i.isspace():
            scchk = False
            break
        else:
            scchk = True

    return scchk


def passwdchk(passwd):
    logging.info("Evaluating password")
    if passwdlencheck(passwd) and passwdsplchk(passwd) and passwducchk(passwd) and passwdlcchk(passwd) and numbrchk(passwd) and spacechk(passwd) == True:
        print("Your password is strong as per standard")
    else:
        print('''Your password does not meet Complexity standard - Please follow below guidelines
        1. Password should contain minimum of 15 Digits
        2. Password should have at least 1 upper case.
        3. Password should have at least 1 Lower case.
        4. Password should not contain Spaces.
        5. Password should have at least 1 Number.''')


passwd = input("Please enter the password you need to validate:")

p1 = passwdchk(passwd)