'''
      Problem Set Link : https://www.hackerrank.com/challenges/python-string-formatting/problem 
      
'''

def print_formatted(number):
    num = 0
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1 , number + 1):
        #print(i)
        dec = str(i).rjust(w , ' ')
        octa = oct(i)[2:].rjust(w , ' ')
        hexa = str(hex(int(i))[2:].rjust(w , ' ')).upper()
        binary = bin(int(i))[2:].rjust(w , ' ')
        print (dec , octa , hexa , binary)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
