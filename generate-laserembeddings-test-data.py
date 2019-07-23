import os
from collections import defaultdict
from glob import glob
from subprocess import check_call
from tempfile import TemporaryDirectory
import tarfile

import numpy as np
from iso639 import to_iso639_1, NonExistentLanguageError

LASER = os.getenv('LASER')
assert LASER, 'LASER env variable must be defined'


def get_sentences(fname):
    with open(fname, 'r', encoding='utf8') as f:
        return [line.strip() for line in f.readlines()]


def remove_non_single_sentences(sentences):
    return [
        sentence for sentence in sentences
        if sentence.find('.') in (-1, len(sentence) - 1)
    ]


def compute_embeddings(sentences, lang):
    with TemporaryDirectory() as tmpdirname:
        sentences_tmp_file = os.path.join(tmpdirname, 'sentences.txt')
        embeddings_tmp_file = os.path.join(tmpdirname, 'embeddings.raw')

        with open(sentences_tmp_file, 'w', encoding='utf8') as f:
            f.write('\n'.join(sentences))

        check_call([
            os.path.join(LASER, 'tasks', 'embed', 'embed.sh'),
            sentences_tmp_file, lang, embeddings_tmp_file
        ])

        return np.fromfile(embeddings_tmp_file, dtype=np.float32,
                           count=-1).reshape(-1, 1024)


def normalize_language_code(lang):
    try:
        lang_iso639_1 = to_iso639_1(lang)
        return lang_iso639_1 or lang
    except NonExistentLanguageError:
        return lang


output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                          'test-data')

totoeba_data = os.path.join(LASER, 'data', 'tatoeba', 'v1', 'tatoeba.*.*')
totoeba_files = sorted(glob(totoeba_data))

langs = set()
texts = defaultdict(list)
vectors = defaultdict(list)

for i, totoeba_file in enumerate(totoeba_files):
    print(
        f'\033[1;34m[{i+1}/{len(totoeba_files)}] Reading file: {totoeba_file}\033[0;0m'
    )

    lang = normalize_language_code(
        os.path.splitext(totoeba_file)[1][1:])  # lang is the file "extension"
    sentences = get_sentences(totoeba_file)
    sentences = remove_non_single_sentences(
        sentences
    )  # some lines contain more than 1 sentence and LASER processes only 1-sentence inputs

    langs.add(lang)
    texts[lang] += sentences

# only keep 100 sentences per lang
for lang in texts:
    texts[lang] = texts[lang][:100]

for i, lang in enumerate(sorted(langs)):
    print(
        f'\033[1;34m[{i+1}/{len(langs)}] Computing embeddings for lang: {lang}\033[0;0m'
    )

    embeddings = compute_embeddings(texts[lang], lang)
    vectors[lang].append(embeddings)

    print()

np.savez(
    os.path.join(output_dir, 'laserembeddings-test-data.npz'),
    langs=np.asarray(sorted(langs)),
    **{f'{lang}_sentences': np.asarray(texts[lang])
       for lang in sorted(langs)},
    **{
        f'{lang}_embeddings': np.concatenate(vectors[lang])
        for lang in sorted(langs)
    })

print('⏳   \033[1;34mCreating archive...\033[0;0m', end='')

with tarfile.open(os.path.join(output_dir, 'laserembeddings-test-data.tar.gz'),
                  'w:gz') as tar:
    tar.add(os.path.join(output_dir, 'laserembeddings-test-data.npz'),
            'laserembeddings-test-data.npz')
    tar.add(os.path.join(output_dir, 'README.md'), 'README.md')
    tar.add(os.path.join(output_dir, 'LICENSE'), 'LICENSE')

print('\r✅   \033[1;34mCreated archive    \033[0;0m')
