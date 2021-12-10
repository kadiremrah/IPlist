# sample.txt must have every url  at eachline, every line must have at least http:// at the beginning (so if not add manually)
# after changing "sample.txt" as your "filename" on linux terminal command :  python3 host_only_list.py > output.txt
# if tld not installed use terminal commad : pip install https://github.com/barseghyanartur/tld/archive/stable.tar.gz
# run command on terminal to update tld database : update-tld-names
from tld import get_fld
 
urls_file = "./sample.txt"
#URLs should be in column A without a heading, in a CSV file named "urls_file.csv"
 
urls = [line.rstrip('\n') for line in open(urls_file)]
 
for url in urls:
    the_list = []
    result = get_fld(url, fail_silently=True)
    print (result)
