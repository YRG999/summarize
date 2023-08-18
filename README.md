# README

## Init

For initial setup, create a virtual environment & run it:

```bash
$ python -m venv venv
$ . venv/bin/activate
```

Then install requirements:

```shell
pip install -r requirements.txt
```

Later, just run the second venv line to activate the virtual environment.

## pip list

<details>
  <summary>Expand</summary>

```
Package            Version
------------------ ---------
breadability       0.1.20
certifi            2023.7.22
cffi               1.15.1
chardet            5.2.0
charset-normalizer 3.2.0
click              8.1.6
cryptography       41.0.3
docopt             0.6.2
idna               3.4
joblib             1.3.2
lxml               4.9.3
nltk               3.8.1
numpy              1.25.2
pdfminer           20191125
pdfminer.six       20221105
pip                23.2.1
pycountry          22.3.5
pycparser          2.21
pycryptodome       3.18.0
PyPDF2             3.0.1
regex              2023.8.8
requests           2.31.0
setuptools         58.1.0
sumy               0.11.0
tqdm               4.66.1
urllib3            2.0.4
```
</details>

## claude.ai

**Create a python program that summarizes PDF files.**

Here is a Python program that summarizes PDF files.

* This program uses the PyPDF2 library to extract text from a PDF file. It then uses the Sumy library to parse the text and generate a summary. 
* The LexRankSummarizer from Sumy implements a graph-based summarization algorithm called LexRank. This algorithm determines the importance of sentences based on how similar they are to other sentences in the document. It then extracts the most representative sentences to create the summary.
* The summarize_pdf function takes in a PDF file path, parses the text, summarizes it using LexRank, and returns the summary as a string. To use it, simply pass a PDF file path to the function.
* This summarizer extracts 10 sentences from the PDF to create the summary. You can tweak this number to make the summary longer or shorter.

---

## Resources

* https://pypi.org/project/PyPDF2/
* https://pypi.org/project/sumy/
* https://pypi.org/project/pdfminer/
* https://pypi.org/project/pdfminer.six/