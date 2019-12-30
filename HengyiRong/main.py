import sys
import os,time
from operation import operation
from datetime import datetime,timedelta



def main(argv):
    operation(argv)# operation agrv(account, password,preiod,money)

#import data 
if __name__ == "__main__":
    main(sys.argv)

    #option 1 = 3, 2 =6, 3 =12, 4 =18, 5 =24, 6 =36, 7 = 48
