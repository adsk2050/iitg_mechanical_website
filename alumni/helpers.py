def checkInt(str):
    str = str.strip()
    if str[0] in ("-", "+"):
        return str[1:].isdigit()
    return str.isdigit()
