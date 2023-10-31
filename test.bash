#echo 
#python ./main.py ./text0.txt
#!/bin/sh

for i in `seq 0 5`
do
    echo text$i.txtでのテストを開始します
    python ./main.py ./text$i.txt
    sleep 5s
done