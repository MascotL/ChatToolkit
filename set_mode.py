import chat


def help_i():
    ret1 = "[CMD]\t[PARAM]\t[VAL]\t[DESC]\n"
    ret2 = ".set\tkey\t-\tEnter the APIkey\n"
    ret3 = "\ttemp\t0~1\tSet the creativity index\n"
    ret4 = ".help\t\t\tShow help"
    ret = ret1 + ret2 + ret3 + ret4
    return ret


def set_i(inp):
    set_cmd = inp.split()[0]  # 读取指令
    try :
        set_par = inp.split()[1]  # 读取参数
    except IndexError:
        set_par = None
    try:
        set_val = inp.split()[2]  # 读取值
    except IndexError:
        set_val = None

    if set_cmd == ".set":  # 设置参数
        if set_par is not None:
            if set_par == "key":
                if set_val is not None:
                    chat.set_key(set_val)
                    return ""
                else:
                    return "[.set key] has no value"
            elif set_par == "temp":
                if set_val is not None:
                    chat.temp(set_val)
                else:
                    return "[.set temp] has no value"
            else:
                return '[' + set_par + ']' + "is not a parameter!"
        else:
            return "[.set] has no parameter"
    elif set_cmd == ".help":
        return help_i()
    else:
        return "[" + set_cmd + "]" + "is not a command!"