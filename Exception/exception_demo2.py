def inputString(a):
    if type(a) != str:
        raise TypeError("Input must be a string")
    if not a:
        raise ValueError("Input must not be blank")

    return True


inputString("addadsda")


try:
    a = ''
    print("Input String or not:", inputString(a))

except ValueError as e:
    print("value error raised", e)
except TypeError as e:
    print("type error raised", e)

