import re
import sys

def main(st):
    InputStringList = list(st)
    """
    Count配列の4つの要素を左から解説
    ・波かっこの開き閉じの個数
    ・丸かっこの開き閉じの個数
    ・四角かっこの開き閉じの個数
    ・改行文字の個数
    """
    Count = [0,0,0,0]
    StringLengthCount = 0
    line_num = 1

    for i in InputStringList:
        if(re.match(r"\{",i)):
            # print("波かっこの展開が認められました")
            Count[0] += 1

        if(re.match(r"\}",i)):
            # print("ちゃんと閉じててえらい！")
            Count[0] += 1

        if(re.match(r"\(",i)):
            # print("かっこの展開が認められました")
            Count[1] += 1

        if(re.match(r"\)",i)):
            # print("ちゃんと閉じててえらい！")
            Count[1] += 1
        
        if(re.match(r"\[",i)):
            # print("角かっこの展開が認められました")
            Count[2] += 1

        if(re.match(r"\]",i)):
            # print("ちゃんと閉じててえらい！")
            Count[2] += 1
        
        if(re.match(r"\n",i)):
            # print("改行コードが検出されました。")
            Count[3] += 1

        StringLengthCount += 1
        # if(StringLengthCount == len(InputText)):
        if(StringLengthCount == len(st)):
            if Count[0] % 2 != 0: raise ValueError("波括弧が正常に閉じられていない可能性があります")
            elif Count[1] % 2 != 0: raise ValueError("かっこが正常に閉じられていない可能性があります") 
            elif Count[2] % 2 != 0: raise ValueError("角かっこが正常に閉じられていない可能性があります")
            else: 
                print("---------------------------------------------\n 与えられた文字の検証を終了します。改行の数は"+ str(Count[3]) +"回でした\n---------------------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv)==2:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            st=[line for line in lines]
            print(st)
            line_num = 1
            for i in st:
                main(i)
                with open("./output.txt","w") as out:
                    out.white(str(line_num) + ":" + st)
                    line_num += 1
                    