import re
import sys

# if __name__ == "__main__":
if len(sys.argv)==2:
    with open(sys.argv[1], 'r') as InFile:
        with open("./output.txt","w") as out:
            lines = InFile.readlines()
            output_row_num = 1
            open_wave = 0
            open_square = 0
            open_circle = 0
            count = 0

            for i in range(len(lines)):
                st = lines[i]
                output_row_num += 1

                for j in st:
                    if(re.match(r"\{",j)):
                        open_wave = 1
                        count += 1
                    elif(re.match(r"\)|\]",j) and open_wave == 1):
                        raise ValueError("波括弧が正常に閉じられていない可能性があります")
                    elif(re.match(r"\}",j)):
                        open_wave = 0
                        count -= 1

                    if(re.match(r"\(",j)):
                        open_circle = 1
                        count += 1
                    elif(re.match(r"\]|\}",j) and open_circle == 1):
                        raise ValueError("かっこが正常に閉じられていない可能性があります")
                    elif(re.match(r"\)",j)):
                        open_circle = 0
                        count -= 1
                
                    if(re.match(r"\[",j)):
                        open_square = 1
                        count += 1
                    elif(re.match(r"\}|\)",j) and open_square == 1):
                        raise ValueError("角かっこが正常に閉じられていない可能性があります")
                    elif(re.match(r"\]",j)):
                        open_square = 0
                        count -= 1
                    
                    if count < 0:
                        raise ValueError("括弧が最初に閉じられている可能性があります")
                    
                out.writelines(str(output_row_num) + "(" + str(count) + ") :" + st)