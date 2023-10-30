import re
import sys

# if __name__ == "__main__":
if len(sys.argv)==2:
    with open(sys.argv[1], 'r') as InFile:
        result = InFile.read()
        # print(result)
        output_row_num = 0
        open_wave = 0
        open_square = 0
        open_circle = 0
        block_count = 0
        char_count = 0
        store_stack = []
        full_text = list(result)
        with open("./output.txt","w") as out:
            while True:
                char = full_text.pop(0)
                if(char == "{"):
                    open_wave += 1
                    #open_circle -= 1
                    #open_square -= 1
                elif(char == "}"):
                    open_wave -= 1
                    #if(open_circle):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "丸括弧が閉じられてないです")
                    #if(open_square):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "角括弧が閉じられてないです")
                elif(char == "("):
                    open_circle += 1
                    #open_wave -= 1
                    #open_square -= 1
                elif(char == ")"):
                    #if(open_wave):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "波括弧が閉じられてないです")
                    #elif(open_square):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "角括弧が閉じられてないです")
                    open_circle -= 1
                elif(char == "["):
                    open_square += 1
                    #open_circle -= 1
                    #open_wave -= 1
                elif(char == "]"):
                    #if(open_circle):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "丸括弧が閉じられてないです")
                    #elif(open_wave):
                    #    raise ValueError(str((output_row_num + 1)) + "行目" + str((char_count - 1)) + "文字目で発生。" + "波括弧が閉じられてないです")
                    open_square -= 1

                if(char == "\n"):
                    output_row_num += 1
                    char_count = 1
                    out.write(str(output_row_num) + ": " + ''.join(store_stack) + "\n")
                    store_stack = []
                    print("改行文字が入りました")
                else: 
                    store_stack.append(char)
                char_count += 1
                if(len(full_text)==0):
                    out.write(str(output_row_num) + ": " + ''.join(store_stack) + "\n")
                    if(open_circle): raise ValueError("丸括弧閉じてないぞ")
                    elif(open_square): raise ValueError("角括弧閉じてないぞ")
                    elif(open_wave): raise ValueError("波括弧閉じてないぞ")
                    else: print("走査を終了します")
                    break
            

            
