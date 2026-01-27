# NepConformer: A Conformer-based Nepali ASR

## About
NepConformer is an End-to-End Automatic Speech Recognition (ASR) system designed for the Nepali language, leveraging the Conformer architecture to address challenges posed by the language's diverse dialects, complex syllable structures, and low-resource nature. Implemented using NVIDIA’s NeMo framework, NepConformer achieves a state-of-the-art Character Error Rate (CER) of 6.01% and a Word Error Rate (WER) of 23.96% on the SLR54 Nepali speech dataset.

## Key Features
- Utilizes Conformer architecture for enhanced ASR performance.
- Implements advanced techniques like spectrogram augmentation and SentencePiece Unigram tokenizer.

## Dataset
The model uses the OSLR54 dataset. you can add your own dataset.
You need `manifest` files.

Folder structure:
```
dataset
  - DS_NAME
      - manifest_train.json
      - manifest_test.json
      - manifest_val.json
      - wav
          - all the sound files should be here.
```

Sample `manifest.json`
```
{"audio_filepath": "dataset/oslr54/wav/e8/e84d149646.wav", "duration": 2.53, "text": "उनी प्रख्यत सोफोत्वरे"}
{"audio_filepath": "dataset/oslr54/wav/07/073a200bf6.wav", "duration": 1.63, "text": "मन्दिर निर्माणको लागि"}
{"audio_filepath": "dataset/oslr54/wav/5b/5bcd9bcc55.wav", "duration": 1.53, "text": "शर्मा बताउनुहुन्छ"}
```
Note: it is not exactly json format :-(


## Model Training

Prepare the environment

```bash
python3 -m venv venv
source ./venv/bin/activate
git clone https://github.com/NVIDIA/NeMo.git
```

Copy config file to asr path:
```bash
cp config/nepconformer.yaml NeMo/examples/asr/asr_ctc/config/nepconformer.yaml
```

### Logging
Use wandb api for the logging. For this we use wandb.api file with following contents.
```
WANDB_API_KEY=<your key>
```

### Tokenization
Prepare the tokenization parameters as in `tokenize.sh`. Once all configuration are placed, run the tokenizer.
```
./tokenize.sh
```
This will produce the tokens folder with some necessary files.
Check `text_corpus/document.txt` and `<tokenizer_name>/tokenizer.vocab` file.


### Training
Before training confirm the configuration of the model to be trained.
Run the training script:  `$ ./train.sh`

The current configuraiton file contain multi-gpu training. Change the
`trainer:` section of the configuration file for more details.

## Contribution

### Citation
If you use this work, please cite:

```bibtex
@inproceedings{poudel2025nepconformer,
  title={NepConformer: A Conformer-Based Nepali Automatic Speech Recognition System},
  author={Poudel, Jenny and Dahal, Ankit and Sharma, Rishikesh Kumar and Tiwari, Rupak and Ghimire, Rupak Raj and Bal, Bal Krishna},
  booktitle={International Conference on Computing and Machine Learning},
  pages={167--178},
  year={2025},
  organization={Springer}
}
```

### Link to the Paper
[Read NepConformer Paper](https://link.springer.com/chapter/10.1007/978-981-95-2872-1_13)


### Acknowledgments
This work was supported by the Information and Language Processing Research Lab (ILPRL) at Kathmandu University.

