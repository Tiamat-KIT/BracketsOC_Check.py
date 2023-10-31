# Pythonプログラム
import re
import sys
def O_or_C(check_string):
    open_pattern =  r'[{[(]\n$'
    close_patterm = r"[\}\)\]]\n$"
    if(re.findall(open_pattern,str_line)):
        return True
    elif(re.findall(close_patterm,str_line)):
        return False
        
def Check(char,In_dict,Out_dict):
    if(char == "{"):
        In_dict["wave"] += 1
        Out_dict["block"] += 1
    elif(char == "}"):
        In_dict["wave"] -= 1
        Out_dict["block"] -= 1
    elif(char == "("):
        In_dict["circle"] += 1
        Out_dict["block"] += 1
    elif(char == ")"):
        In_dict["circle"] -= 1
        Out_dict["block"] -= 1
    elif(char == "["):
        In_dict["square"] += 1
        Out_dict["block"] += 1
    elif(char == "]"):
        In_dict["square"] -= 1
        Out_dict["block"] -= 1

def res_print(In_dict,Out_dict):
    err_st = "個対応してないよ！"
    if(Out_dict["block"] != 0):
        if(In_dict["wave"] != 0):
            print(f"波かっこが{In_dict["wave"]}{err_st}")
        elif(In_dict["square"] != 0):
            print(f"角かっこが{In_dict["wave"]}{err_st}")
        elif(In_dict["circle"] != 0):
            print(f"丸かっこが{In_dict["wave"]}{err_st}")

if len(sys.argv)==2:
    with open(sys.argv[1], 'r') as InFile:
        with open("./output.txt","w") as OutFile:
            result = InFile.readlines()
            op = {"row": 1,"block": 0}
            open = {"wave": 0,"square": 0,"circle": 0}
            next_indent = False
            char_count = 0
            store_stack = []
            if(len(result) == 1):
                for char in list(result.pop(0)):
                    Check(char,open,op)
                    store_stack.append(char)
                out_str = "".join(store_stack)
                OutFile.write(f"{str(op["row"])}({op["block"]}):{out_str}\n")
                res_print(open,op)
            else:
                for str_line in range(len(result)):
                    str_line = result.pop(0)
                    store_stack = []
                    next_indent = O_or_C(str_line)
                    line = list(str_line)
                    for i in range(len(line)):
                        char = line.pop(0)
                        if(char == "\n" or len(line) == 0):
                            out_str = "".join(store_stack)
                            Check(char,open,op)
                            if(next_indent):
                                op["block"] -= 1
                                OutFile.write(f"{str(op["row"])}({op["block"]}):{out_str}\n")
                                if(len(result) == 0):
                                    res_print(open,op)
                                else:
                                    op["block"] += 1
                                    op["row"] += 1
                                    next_indent = False
                            else:
                                OutFile.write(f"{str(op["row"])}({op["block"]}):{out_str}\n")
                                if(len(result) == 0):
                                    res_print(open,op)
                                else:
                                    op["row"] += 1
                        else:
                            Check(char,open,op)
                            store_stack.append(char)