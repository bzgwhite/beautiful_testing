from defs.webdriver_def import mb
from defs.diff_tools import makefile
import sys


url = sys.argv[1]
tar = sys.argv[2]


makefile(url,tar)
mb(url,tar)
mb(url,tar,True)