import re
import sys  

def main():
    f = open('1.txt')
    data = f.read() 
    l=[]
    l.append(data)
    # print(l)
    data1 = l[0].split('\n\n')
    # print(data1)
    port = sys.argv[1]
    for i in data1:
        data2 = i.split(' ')
        if port == data2[0]:
            # print(i)
            # pattern = r'\w*\saddress\s+is\s+\w*\d*.?\d*.?\d*.?\d*/\d*'
            pattern = r'\w*\s*address\s+is\s+\w*\d*.?\d*\w*.?\d*\w.?\d*/?\d*'
            regex = re.compile(pattern)
            l = regex.findall(i)
            print(l)
    f.close()

if __name__=='__main__':
    main()
    

