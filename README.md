# Danish-English Sentence Pair Dataset Cleaner

This repository contains a Python script that cleans and separates Danish-English sentence pair data obtained from the Tatoeba project (tatoeba.org). The script performs the following tasks:

- Cleans the dataset file by removing unnecessary information and formatting the sentence pairs.
- Separates the Danish and English sentences into two separate files.
- Provides a convenient way to preprocess the data for further analysis or machine learning tasks.

## Features

- Cleans and formats Danish-English sentence pairs from the Tatoeba dataset.
- Separates the Danish and English sentences into separate files.
- Removes unnecessary information and maintains the original sentence pair structure.
- Supports handling large datasets.
- Easy-to-use Python script.

## Usage

1. Download the Danish-English sentence pair dataset from tatoeba.org.
2. Place the dataset file in the same directory as the Python script.
3. Run the script using Python: `python sentence_pair_cleaner.py`.
4. The cleaned dataset will be saved as "Danish-English pairs.txt".
5. The Danish sentences will be saved in "danish.txt".
6. The English sentences will be saved in "english.txt".

Feel free to modify the script to suit your specific needs and adapt it to different languages or datasets.

## Requirements

- Python 3.x
- `re` module (built-in)

## License

This project is licensed under the MIT License.
