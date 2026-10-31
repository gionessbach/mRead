set -e
cd /home/claude/train
python3 gen.py data/train 160 fonts_train.txt 11
python3 gen.py data/train_std 200 fonts_std.txt 12
python3 gen.py data/eval 8 fonts_train.txt 13
python3 gen.py data/test 60 fonts_test.txt 14
python3 gen.py data/test_std 20 fonts_std.txt 15
for d in train train_std eval; do
  ls data/$d/*.png | xargs -n 200 python3 mkbox.py
  ls data/$d/*.png | xargs -P 2 -I{} sh -c 'b="${1%.png}"; tesseract "$1" "$b" --psm 13 lstm.train >/dev/null 2>&1' _ {}
done
ls data/train/*.lstmf data/train_std/*.lstmf | shuf --random-source=<(yes) > list.train
ls data/eval/*.lstmf > list.eval
wc -l list.train list.eval
echo FERTIG
