# laserembeddings test data

The file `laserembeddings-test-data.npz` is a [NumPy archive](https://docs.scipy.org/doc/numpy/reference/generated/numpy.lib.format.html) containing 3 types of NumPy arrays:

- `langs`: the list of available languages in the corpus in [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) or [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) format. The list is alphabetically sorted.
- `{LANGUAGE-CODE}_sentences`: a 1-d NumPy array of Unicode strings containing the sentences for the language designed by `{LANGUAGE-CODE}`.
- `{LANGUAGE-CODE}_embeddings`: a 2-d NumPy array of `float32` numbers containing the embeddings of the sentences in `{LANGUAGE-CODE}_sentences`, computed with [LASER embedding utility script](https://github.com/facebookresearch/LASER/tree/master/tasks/embed). The shape of this array is _N * 1024_, N being the length of `{LANGUAGE-CODE}_sentences` array

For more information about how this file was created, please check out https://github.com/yannvgn/laserembeddings-test-data.

## Using this file

```python
import numpy as np
laserembeddings_test_data = np.load('laserembeddings-test-data.npz')

laserembeddings_test_data.files
# Returns the list of available arrays
# ['langs', 'af_sentences', 'am_sentences', 'ang_sentences', ..., 'zsm_embeddings']

laserembeddings_test_data['langs']
# array(['af', 'am', 'ang', 'ar', 'arq', 'arz', 'ast', 'awa', 'az', 'be',
#        'ber', 'bg', 'bn', 'br', 'bs', 'ca', 'cbk', 'ceb', 'ch', 'cmn',
#        'cs', 'csb', 'cy', 'da', 'de', 'dsb', 'dtp', 'el', 'en', 'eo',
#        'es', 'et', 'eu', 'fi', 'fo', 'fr', 'fy', 'ga', 'gd', 'gl', 'gsw',
#        'he', 'hi', 'hr', 'hsb', 'hu', 'hy', 'ia', 'id', 'ie', 'io', 'is',
#        'it', 'ja', 'jv', 'ka', 'kab', 'kk', 'km', 'ko', 'ku', 'kw', 'kzj',
#        'la', 'lfn', 'lt', 'lvs', 'max', 'mhr', 'mk', 'ml', 'mn', 'mr',
#        'nb', 'nds', 'nl', 'nn', 'nov', 'oc', 'orv', 'pam', 'pes', 'pl',
#        'pms', 'pt', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr', 'sv', 'swg',
#        'swh', 'ta', 'te', 'th', 'tk', 'tl', 'tr', 'tt', 'tzl', 'ug', 'uk',
#        'ur', 'uz', 'vi', 'war', 'wuu', 'xh', 'yi', 'yue', 'zsm'],
#       dtype='<U3')

laserembeddings_test_data['en_sentences']
# array(['Her English is excellent.', "I don't give a damn about my CV.",
#        'The teacher is supervising her students.',
#        ...,
#        'I am fat.'], dtype='<U54')

laserembeddings_test_data['en_embeddings']
# array([[ 1.82296131e-02,  5.49756951e-05,  9.57560958e-04, ...,
#         -7.25955237e-04, -2.47536576e-03,  1.24272797e-02],
#        [-3.13856086e-04, -7.28133591e-06,  2.24805158e-02, ...,
#          1.97728239e-02,  2.70649418e-02,  2.75465213e-02],
#        [ 2.08503986e-03,  1.66819154e-04,  5.31200925e-03, ...,
#          1.06439553e-02,  2.42042039e-02, -6.29558088e-03],
#        ...,
#        [ 8.62005539e-03, -1.67025602e-04, -3.64240841e-04, ...,
#          5.51943667e-03,  2.11967919e-02, -4.78343759e-03],
#        [ 1.49085384e-03, -7.25948266e-05,  1.64968763e-02, ...,
#          2.54525244e-03,  1.93307996e-02,  1.03027290e-02],
#        [ 5.11183869e-04,  5.27936299e-06,  1.21905054e-04, ...,
#          1.68113736e-03,  9.61784739e-03, -2.13472173e-03]], dtype=float32)
```

## License & attribution

The file `laserembeddings-test-data.npz` in this directory is a derivative of [LASER](https://github.com/facebookresearch/LASER)'s [_test set for more than 100 languages_](https://github.com/facebookresearch/LASER/tree/master/data/tatoeba/v1) by [Facebook Research](https://github.com/facebookresearch), itself being a derivative of the [_Tatoeba corpus_](https://tatoeba.org/eng/downloads) by [Tatoeba](https://tatoeba.org), used under [CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/deed.en). The file `laserembeddings-test-data.npz` is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by [yannvgn](https://github.com/yannvgn).


[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
