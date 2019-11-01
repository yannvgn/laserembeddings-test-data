# laserembeddings – test data

This repository contains the script used to generate the data required for testing [laserembeddings](https://github.com/yannvgn/laserembeddings), a pip-packaged, production-ready port of Facebook Research's [LASER](https://github.com/facebookresearch/LASER) (Language-Agnostic SEntence Representations) to compute multilingual sentence embeddings.

The data contains a corpus of multilingual sentences with their embeddings computed with [Facebook's LASER](https://github.com/facebookresearch/LASER) original implementation. It is used during the tests of laserembeddings to make sure the embeddings computed with laserembeddings match the ones obtained with Facebook's LASER.

## Usage

First install [LASER](https://github.com/facebookresearch/LASER). Make sure that [MeCab](https://taku910.github.io/mecab/) is also installed and is configured to support UTF-8.

Then export the path to LASER's installation directory (i.e. where you cloned LASER's repository).

```
export LASER=/path/to/laser
```

Install additional dependencies ([iso639](https://github.com/janpipek/iso639-python) and [yapf](https://github.com/google/yapf)):
```
pip install iso639 yapf
```

Then generate that data!

```
python generate-laserembeddings-test-data.py
```

The test data (`laserembeddings-test-data.npz`) is placed into the `test-data` directory. For ease of distribution, a `.tar.gz` archive is also created containing the `.npz` file along with the README and the LICENSE file of the test data.

The test data is generated from a version of the [_Tatoeba corpus_](https://tatoeba.org/eng/downloads) refined by [Facebook Research](https://github.com/facebookresearch), located in LASER's installation directory (`$LASER/data/tatoeba/v1`). Refer below for more information.

## Test data description & license

Check out the [README](test-data/README.md) of the `test-data` directory to know more about the contents of the generated files, their license and the data they are based on.
