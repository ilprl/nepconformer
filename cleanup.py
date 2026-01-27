import os
import json

# Load valid characters
valid_chars = set()
with open("ne.vocab", "r", encoding="utf-8") as f:
    for line in f:
        ch = line.strip()
        if ch: valid_chars.add(ch)
valid_chars.remove('EOS')
valid_chars.remove('BOS')
valid_chars.remove('PAD')
valid_chars.add(' ') # line.strip() remove from original vocab file
# print(valid_chars)

files = [
    'dataset/oslr54/manifest_labels_train_org.json',
    'dataset/oslr54/manifest_labels_test_org.json',
    'dataset/oslr54/manifest_labels_val_org.json',
]
for file in files:
    with open(file, 'r', encoding='utf-8') as fin,\
        open(file.replace('_org',''), 'w', encoding='utf-8') as fout:
        for line in fin:
            obj = json.loads(line)
            isok = True
            for char in obj["text"]:
                if char not in valid_chars:
                    isok = False
            if isok: fout.write(line)
