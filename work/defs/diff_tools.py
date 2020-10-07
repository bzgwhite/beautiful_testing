import requests
import os
from bs4 import BeautifulSoup as bs



def makefile(url,src_file):
    tar_file = 'result/' + src_file + '.html'
    res = requests.get(url)
    print(tar_file)
    if os.path.exists(tar_file):
        tar_file = tar_file.replace('.','_after.')
        
    with open(tar_file,'w') as f :
        soup = bs(res.text, 'html.parser')
        print(soup, file=f)

