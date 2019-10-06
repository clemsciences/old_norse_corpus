# Corpus of Old Norse texts

This package provides Old Norse texts with code to parse them.

## Sources
Although texts are in public domain, we must thank those who digitalised and normalized these texts.

- [Heimskringla.no](https://heimskringla.no/wiki/Main_Page)

## Installation

```bash
$ pip install --user --upgrade norsecorpus
```

## How to use **norsecorpus**

```python
import norsecorpus.reader as ncr
available_texts = ncr.get_available_texts()
filename = "volsunga.xml"
volsunga = ncr.read_tei_words(available_texts["volsunga.xml"])
```

You have now the Völsunga saga.
