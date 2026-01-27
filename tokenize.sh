python NeMo/scripts/tokenizers/process_asr_text_tokenizer.py \
    --manifest "dataset/oslr54/manifest_labels.json" \
    --data_root "tokens" \
    --tokenizer "spe" \
    --spe_type "char" \
    --spe_max_sentencepiece_length 200 \
    --spe_character_coverage 1.0 \
    --log