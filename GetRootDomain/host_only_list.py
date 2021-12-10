from tld import get_fld
 
urls_file = "./sample.txt"
#URLs should be in column A without a heading, in a CSV file named "urls_file.csv"
 
urls = [line.rstrip('\n') for line in open(urls_file)]
 
for url in urls:
    the_list = []
    result = get_fld(url, fail_silently=True)
    print (result)
