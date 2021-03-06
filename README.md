# compbio_utils
short python scripts for day to day research

## 1. title2PMID.py
This code converts a csv containing article titles to a csv containing PMID of the articles.
Enter input/output filename and path to get results.
example input file: title2PMID_input.csv

usage:
On terminal go to folder containing .py file then run:

 `$ python3 title2PMID.py input_filename.csv output_filename.csv`

requirements (installation order):
1. python3
2. chromedriver
3. selenium for python

For a mac os which already has anaconda (python3) and homebrew (like mine), just run these on your terminal window:
 ```
 $ brew tap homebrew/cask
 $ brew cask install chromedriver
 $ conda install -c conda-forge selenium
```
## 2. pdf2excel.ipynb
Converts a pdf table to csv format. easy for reading in ms excel or pandas. 
yo can do this easily to on google colab. Just install tabula-py using the following command in your colab notebook.


`!pip install -q tabula-py`

## 3. GO_analysis.ipynb

For GO enrichment provided a list of genes. Uses STRINGdb API. Run this in google colab.
requires 'requests' package.

enrichment categories: 'Molecular Function', 'PMID','Component','Process','KEGG','Interpro'


## 4. merge_multiple_csv.ipynb

merges all the csv files in a given folder into a single csv file. can be modified as per requirement.

