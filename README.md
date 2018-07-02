# Article Full Text
This is a python program to get full text articles from Science Direct (Elsevier) or Springer using Springer Link.  It uses HTTP GET requests to query the Science Direct API or SpringerLink to gather the articles.  Science Direct articles are returned as XML files and Springer articles are returned as PDFs.

## DEPENDENCIES

The Requests package is needed to handle the HTTP interactions.  Requests can be found at http://docs.python-requests.org/en/master/

## USAGE

There are 3 parameters that are needed for this program.  

1. File path to a file containing all of the PMIDs or DOIs that you want to search.  This file should have a single entry per line and should ONLY contain the IDs.

2. Either 'pmid' or 'doi' to tell the program which you want to use.  Springer Link does NOT take PubMed IDs, so ONLY results from Science Direct will be found if you choose to search with PMIDs.  If you search with DOIs, then articles will be found from both Springer and Science Direct.

3.  Your Science Direct API key.  I will not provide one for this program.  Science Direct requires an API key to keep track of users.  To get an API key, you must register for an account at the following link: https://dev.elsevier.com/.

The following is how you would run it on macOS command line:

python main.py /path/to/idFile/ doi $sciDirToken 

'python main.py' runs the program.  '/path/to/idFile/' is the location of the file with the IDs.  'doi' means to run the parts of the program associated with DOIs.  '$sciDirToken' is the API key that Elsevier generates to tie requests to their API to users.
