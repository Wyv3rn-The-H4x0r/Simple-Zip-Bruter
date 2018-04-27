import zipfile
import itertools
import string
from threading import Thread

print(""" 
 **************
 * Zip-Bruter *
 *    Tak     *
 *  V 1.0.0   *
 **************
	""")

list = raw_input("Input Full Dictionary filename *pw_list.txt* :\n")
file = raw_input("Bruting Target *test.zip* :\n")

def dictionary():
    print("Open Password-List..\n ")
    passwords = open(list)
    print("[+] Start Bruting.... ")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        print(pwd)
        t = Thread(target=crack, args=(zipFile, pwd))
        t.start()

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('\n[+] Success: Password is ' + pwd)
        t.stop()
    except:
        pass

zipFile = zipfile.ZipFile(file)
dictionary()