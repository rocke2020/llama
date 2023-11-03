# 
torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir /mnt/nas1/models/llama/pretrained_weights/llama-2-7b \
    --tokenizer_path /mnt/nas1/models/llama/pretrained_weights/tokenizer.model \
    --max_seq_len 512 --max_batch_size 6 \
    > example_text_completion.log 2>&1 &