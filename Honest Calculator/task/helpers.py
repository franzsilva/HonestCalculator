
import messages


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages.msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + messages.msg[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + messages.msg[8]
    if msg != "":
        msg = messages.msg[9] + msg
        print(msg)


def is_one_digit(v):
    if (-10 < float(v) < 10) and float(v).is_integer():
        return True
    else:
        return False
