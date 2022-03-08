import sys
import helpers
import messages
memory = float(0)

operations = ["+", "-", "*", "/"]

while True:
    print(messages.msg[0])
    x, operation, y = input("").split()
    x = memory if x == "M" else x
    y = memory if y == "M" else y
    if helpers.isfloat(x) and helpers.isfloat(y):
        if operation in operations:
            result = 0.0
            helpers.check(float(x), float(y), operation)
            if operation == "+":
                result = float(x) + float(y)
                print(result)
            elif operation == "-":
                result = float(x) - float(y)
                print(result)
            elif operation == "*":
                result = float(x) * float(y)
                print(result)
            elif operation == "/" and float(y) != 0:
                result = float(x) / float(y)
                print(result)
            else:
                print(messages.msg[1])
                continue
            while True:
                print(messages.msg[2])
                store = input()
                if store == "y":
                    if helpers.is_one_digit(result):
                        msg_index = 10
                        while True:
                            msg_response = input(messages.msg[msg_index])
                            if msg_response == "y":
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                    continue
                                else:
                                    memory = result
                                    break
                            elif msg_response == "n":
                                break
                            else:
                                continue
                        break
                    else:
                        memory = result
                        break
                elif store == "n":
                    break
                else:
                    continue
            while True:
                print(messages.msg[3])
                more_calc = input()
                if more_calc == "y":
                    break
                elif more_calc == "n":
                    sys.exit(0)
                else:
                    continue

        else:
            print(messages.msg[4])
    else:
        print(messages.msg[5])
