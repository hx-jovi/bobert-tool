# bobert-tool
Our tool returns the latest research results by crawling arXiv and Google Scholar papers and summarizing abstracts. Bobert helps you stay organized and do faster research.

Installing
This script runs using Python 3. It requires nltk, six, and pyspellchecker. To install it as a Python package, follow the following steps:

Step 1: clone this repo, and go inside that repo:
$ git clone [github.com/hxjovi/bobert-tool]
$ cd bobert-tool
Step 2: install using pip
$ pip3 install .
On Windows, due to encoding errors, the script may cause issues when run on the command line. It is recommended to use pip install win-unicode-console --upgrade prior to launching the script. If you get UnicodeEncodingError, you must  install the above.

In MacOS, you can get the SSL error
[nltk_data] Error loading punkt: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:1045)>
This will be fixed by reinstalling certificates:
$ /Applications/Python\ 3.x/Install\ Certificates.command
 
 
Usage:
This project adds the bobert script for you to run globally on Terminal or command line.
To query for a certain keyword, run:
$ bobert [keyword] [number of results]
For example:
$ bobert Nazi Germany 10
or
$ bobert Law of Cosines 7
