export $(grep -v '^#' wandb.api | xargs)

python NeMo/examples/asr/asr_ctc/speech_to_text_ctc_bpe.py \
    --config-path="config" \
    --config-name="nepconformer" \
    model.train_ds.manifest_filepath="dataset/oslr54/manifest_labels_train.json" \
    model.validation_ds.manifest_filepath="dataset/oslr54/manifest_labels_val.json" \
    model.test_ds.manifest_filepath="dataset/oslr54/manifest_labels_test.json" \
    model.tokenizer.dir="tokens/tokenizer_spe_char_v1024_max_200"