import logging
import re


logging.basicConfig(filename='pswdvalid.log', level=logging.DEBUG)


def passwdlencheck(passwd):
    logging.info("Evaluating if password having minimum length of 15 digit")
    len1 = False
    if len(passwd) >= 15:
        len1 = True
    return len1


def passwdsplchk(passwd):
    logging.info("Evaluating if password has spl Characters @, $, _")
    spl = True
    if bool(re.search('[@$_]', passwd)) is False:
        spl = False
    return spl


def passwducchk(passwd):
    logging.info("Evaluating if upper case is used")
    upchk = False
    for i in passwd:
        if i.isupper():
            upchk = True
            break
    return upchk


def passwdlcchk(passwd):
    logging.info("Evaluating if Lower case is used")
    lcchk = False
    for i in passwd:
        if i.islower():
            lcchk = True
            break
    return lcchk


def numbrchk(passwd):
    logging.info("Evaluating if Digit is used")
    dcchk = False
    for i in passwd:
        if i.isdigit():
            dcchk = True
            break
    return dcchk


def spacechk(passwd):
    logging.info("Evaluating if space is not used")
    scchk = True
    for i in passwd:
        if i.isspace():
            scchk = False
            break
    return scchk


def passwdchk(passwd):
    logging.info("Evaluating password")
    if passwdlencheck(passwd) and spacechk(passwd) and passwdsplchk(passwd) and passwducchk(passwd) and passwdlcchk(passwd) and numbrchk(passwd) is True:
        print("Your password follows all security standards")
    else:
        logging.error("Your Password has failed to meet complexity standard")
        print('''Your password does not meet Complexity standard - Please follow below guidelines
        1. Password should contain minimum of 15 Digits
        2. Password should have at least 1 upper case.
        3. Password should have at least 1 Lower case.
        4. Password should not contain Spaces.
        5. Password should have at least 1 Number.''')


passwd = input("Please enter the password you need to validate:")

p1 = passwdchk(passwd)
