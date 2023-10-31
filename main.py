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

def res_print(In_dict,Out_dict,err_st):
     if(not Out_dict["block"] == 0):
        if(not In_dict["wave"] == 0):
            print(f"波かっこが{In_dict["wave"]}{err_st}")
        elif(not In_dict["square"] == 0):
            print(f"角かっこが{In_dict["wave"]}{err_st}")
        elif(not In_dict["circle"] == 0):
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
            
            for str_line in range(len(result)):
                str_line = result.pop(0)
                store_stack = []
                next_indent = O_or_C(str_line)
                print(f"一行：{str_line}")
                line = list(str_line)
                for i in range(len(line)):
                    char = line.pop(0)
                    print(char)
                    if(char == "\n" or len(line) == 0):
                        out_str = "".join(store_stack)
                        err_st = "個閉じ忘れあるよ！"
                        if(next_indent):
                            op["block"] -= 1
                            OutFile.write(f"{str(op["row"])}({op["block"]}):{out_str}\n")
                            if(len(result) == 0):
                                print("走査終了")
                                res_print(open,op,err_st)
                            else:
                                op["block"] += 1
                                op["row"] += 1
                                next_indent = False
                        else:
                            OutFile.write(f"{str(op["row"])}({op["block"]}):{out_str}\n")
                            if(len(result) == 0):
                                print("走査終了")
                                res_print(open,op,err_st)
                            else:
                                op["row"] += 1
                    else:
                        Check(char,open,op)
                        store_stack.append(char)