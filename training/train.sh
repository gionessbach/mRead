cd /home/claude/train
lstmtraining \
  --model_output out/kids \
  --continue_from deu.lstm \
  --traineddata deu_best.traineddata \
  --train_listfile list.train \
  --eval_listfile list.eval \
  --max_iterations 12000 \
  --learning_rate 0.0001 \
  --target_error_rate 0.5 \
  --debug_interval 0
echo TRAIN_FERTIG
