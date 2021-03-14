import subprocess
import os
from sys import argv


if __name__ == '__main__':
    
    try:
        list_files = subprocess.run("lsblk > lsblk.txt", shell=True, check=True)
    except Exception as e:
        os.remove('lsblk.txt')
        exit(0)
    
    try:
        list_files1 = subprocess.run(
                         "df -h --output=source,fstype,size,avail,target -x tmpfs -x devtmpfs > df.txt", 
                         shell=True, check=True)
    except Exception as e:
        os.remove('lsblk.txt')
        os.remove('df.txt')
        exit(0)
    
    try:
        input_filename = argv[1]
        with open(input_filename, 'r') as f:
            dev_path = f.readline().strip()
    except:
        print('Use: python dinfo.py <inputfile name>')
        exit(0)
    
    with open('lsblk.txt', 'r') as f:
        flag1 = False
        f.readline()
        for s in f:
            while not s[0].isalpha():
                s = s[1:]
            s = '/dev/' + s
            if s.rsplit()[0].strip() == dev_path:
                size = s.rsplit()[3].replace('\n','')
                if size[-1].lower() == 'k':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))/1000000) + 'G'
                elif size[-1].lower() == 'm':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))/1000) + 'G'
                elif size[-1].lower() == 't':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000) + 'G'
                elif size[-1].lower() == 'p':
                    size = str(float(size[0:len(size)-1].
                    	                  eplace(',', '.'))*1000000) + 'G'
                elif size[-1].lower() == 'e':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000) + 'G'
                elif size[-1].lower() == 'z':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000000) + 'G'
                elif size[-1].lower() == 'y':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000000000) + 'G'
                s_print = ' '.join((dev_path, s.rsplit()[5].replace('\n',''), size))               
                flag1 = True
                break
    
    with open('df.txt', 'r') as f:
        flag2 = False
        f.readline()
        for s in f:
            if s.rsplit()[0].strip() == dev_path:
                size = s.rsplit()[3].replace('\n','')
                if size[-1].lower() == 'k':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))/1000) + 'M'
                elif size[-1].lower() == 'g':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000) + 'M'
                elif size[-1].lower() == 't':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000) + 'M'
                elif size[-1].lower() == 'p':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000) + 'M'
                elif size[-1].lower() == 'e':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000000) + 'M'
                elif size[-1].lower() == 'z':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000000000) + 'M'
                elif size[-1].lower() == 'y':
                    size = str(float(size[0:len(size)-1].
                    	                  replace(',', '.'))*1000000000000000000) + 'M'
                s_print1 = ' '.join((size, s.rsplit()[1].replace('\n',''), 
                                     s.rsplit()[4].replace('\n','')))                
                flag2 = True
                break
    
    os.remove('lsblk.txt')
    os.remove('df.txt')

    if flag1&(~flag2):
        print(s_print)
    elif flag1&flag2:
        print(s_print, s_print1)
    else:
    	print('The path in the inputfile is not exist.')
