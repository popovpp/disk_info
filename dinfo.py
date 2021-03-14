import subprocess
import os
from sys import argv


if __name__ == '__main__':
    
    input_filename = argv[1]
    list_files = subprocess.run("lsblk > lsblk.txt", shell=True)
    list_files1 = subprocess.run("df -h --output=source,fstype,size,avail,target -x tmpfs -x devtmpfs > df.txt", 
                                     shell=True)
    try:
        with open(input_filename, 'r') as f:
            dev_path = f.readline().strip()
    except:
        print('Use: python dimfo.py <input filename>')
        exit(0)
    with open('lsblk.txt', 'r') as f:
        s_title = f.readline()
        for s in f:
            while not s[0].isalpha():
                s = s[1:]
            s = '/dev/' + s
            if s.rsplit()[0].strip() == dev_path:
                size = s.rsplit()[3].replace('\n','')
                if size[-1].lower() == 'k':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))/1000000) + 'G'
                elif size[-1].lower() == 'm':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))/1000) + 'G'
                elif size[-1].lower() == 't':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000) + 'G'
                elif size[-1].lower() == 'p':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000) + 'G'
                elif size[-1].lower() == 'e':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000) + 'G'
                elif size[-1].lower() == 'z':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000000) + 'G'
                elif size[-1].lower() == 'y':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000000000) + 'G'
                s_print = ' '.join((dev_path, s.rsplit()[5].replace('\n',''), size))
#                    print(s_print)
                os.remove('lsblk.txt')
                break
    with open('df.txt', 'r') as f:
        s_title = f.readline()
        for s in f:
            print(s.rsplit()[0].strip())
            if s.rsplit()[0].strip() == dev_path:
                av_size = s.rsplit()[3].replace('\n','')
                if size[-1].lower() == 'k':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))/1000) + 'M'
                elif size[-1].lower() == 'g':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000) + 'M'
                elif size[-1].lower() == 't':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000) + 'M'
                elif size[-1].lower() == 'p':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000) + 'M'
                elif size[-1].lower() == 'e':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000000) + 'M'
                elif size[-1].lower() == 'z':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000000000) + 'M'
                elif size[-1].lower() == 'y':
                    size = str(float(size[0:len(size)-1].replace(',', '.'))*1000000000000000000) + 'M'
                s_print1 = ' '.join((size, s.rsplit()[1].replace('\n',''), 
                                     s.rsplit()[4].replace('\n','')))
                print(s_print, s_print1)
                os.remove('df.txt')
                break

