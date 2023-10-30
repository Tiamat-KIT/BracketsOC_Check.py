import re
import sys

if len(sys.argv)==2:
    with open(sys.argv[1], 'r') as InFile:
        with open("./output.txt","w") as OutFile:
            result = InFile.readlines()
            output = {
                "row": 1,
                "block": 0 
            }

            open = {
                "wave": 0,
                "square": 0,
                "circle": 0
            }
            
            next_indent = False
            char_count = 0
            store_stack = []
            open_pattern =  r'[{[(]\n$'
            close_patterm = r"[\}\)\]]\n$"
            for str_line in range(len(result)):
                str_line = result.pop(0)
                store_stack = []
                if(re.findall(open_pattern,str_line)):
                    next_indent = True
                elif(re.findall(close_patterm,str_line)):
                    next_indent = False
                print(f"一行：{str_line}")
                line = list(str_line)
                for i in range(len(line)):
                    char = line.pop(0)
                    print(char)
                    if(char == "\n" or len(line) == 0):
                        out_str = "".join(store_stack)
                        err_st = "個閉じ忘れあるよ！"
                        if(next_indent):
                            print(f"{output["row"]}行目の走査を完了しました(階層構造{output["block"]})")
                            output["block"] -= 1
                            OutFile.write(f"{str(output["row"])}({output["block"]}):{out_str}\n")
                            if(len(result) == 0):
                                print("走査終了")
                                if(not output["block"] == 0):
                                    if(not open["wave"] == 0):
                                        print(f"波かっこが{open["wave"]}{err_st}")
                                    elif(not open["square"] == 0):
                                        print(f"角かっこが{open["wave"]}{err_st}")
                                    elif(not open["circle"] == 0):
                                        print(f"丸かっこが{open["wave"]}{err_st}")
                            else:
                                output["block"] += 1
                                output["row"] += 1
                                next_indent = False
                        else:
                            print(f"{output["row"]}行目の走査を完了しました")
                            OutFile.write(f"{str(output["row"])}({output["block"]}):{out_str}\n")
                            if(len(result) == 0):
                                print("走査終了")
                                if(not output["block"] == 0):
                                    if(not open["wave"] == 0):
                                        print(f"波かっこが{open["wave"]}個閉じ忘れあるよ！")
                                    elif(not open["square"] == 0):
                                        print(f"角かっこが{open["wave"]}個閉じ忘れあるよ！")
                                    elif(not open["circle"] == 0):
                                        print(f"丸かっこが{open["wave"]}個閉じ忘れあるよ！")
                            else:
                                output["row"] += 1
                    else:
                        if(char == "{"):
                            open["wave"] += 1
                            output["block"] += 1
                        elif(char == "}"):
                            open["wave"] -= 1
                            output["block"] -= 1
                        elif(char == "("):
                            open["circle"] += 1
                            output["block"] += 1
                        elif(char == ")"):
                            open["circle"] -= 1
                            output["block"] -= 1
                        elif(char == "["):
                            open["square"] += 1
                            output["block"] += 1
                        elif(char == "]"):
                            open["square"] -= 1
                            output["block"] -= 1
                        store_stack.append(char)
                        
