# NepConformer

## Prepare for training
```bash
python3 -m venv venv
source ./venv/bin/activate
git clone https://github.com/NVIDIA/NeMo.git
```

Copy config file to asr path:
`cp config/nepconformer.yaml NeMo/examples/asr/asr_ctc/config/nepconformer.yaml`

## Logging
Use wandb api for the logging. For this we use wandb.api file with following contents.
```
WANDB_API_KEY=<your key>
```

## Training
Prepare the tokenizer:  `$ ./tokenize.sh`

Before training confirm the configuration of the model to be trained.

Run the training script:  `$ ./train.sh`
