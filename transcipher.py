import string
import numpy
#to read input from a file
f=open("plainfile", "r")
if f.mode == 'r':
    contents = f.read()
plaintext = contents.upper()

plainlength = len(plaintext)
alphabet = list(string.ascii_uppercase)


keyentry = "NA1C3H8TB2OME5WRPD4F6G7I9J0KLQSUVXYZ"
print("\nEntry key is")
print(keyentry)

def matrixValues(text, keyentry):
    z=0
    encryptlist1 = [['0' for i in range(6)] for j in range(6)]
    while z!=len(keyentry):
        for i in range(6):
            for j in range(6):
                encryptlist1[i][j] = keyentry[z]
                z+=1
        return encryptlist1

encryptlist1 = matrixValues(plaintext, keyentry)
print("\n")
print("The encryption list is : ")
print(encryptlist1)
print("\n")
dict1 = {0:"A", 1:"D", 2:"F", 3:"G", 4:"V", 5:"X"}

key = input("Enter the encryption key : ")
print("\n")

#to map the key entry with the plain text and store the result as a string
def encrypt1(plaintext, encryptlist1, dict1, keyentry):
    result = ""
    replace = ""
    row = column = i = j = otherchars = 0
    for x in plaintext:
        if x in keyentry:
            for i in range(6):
                for j in range(6):
                    if encryptlist1[i][j] == x:
                        row = i
                        column = j
                        break
            replace = dict1[row] + dict1[column]
            result += replace
        else:
            otherchars +=1
            continue
    return result

ciphertext1 = encrypt1(plaintext, encryptlist1, dict1, keyentry)
print("The cipher text is : ")
print(ciphertext1)

keysize = len(key)

def encrypt2(ciphertext1, keysize, key):
	nrows = ncol = x = key1 = 0
	result=""
	for a in ciphertext1:
		if len(ciphertext1)%keysize==0 :
			break
		else:
			ciphertext1 += 'J' #Padding
    
	nrows = int(len(ciphertext1))//keysize
	ncol = keysize

	encryptlist2 = [['0' for i in range(ncol)] for j in range(nrows)]
	while x!=len(ciphertext1):
		for i in range(nrows):
			for j in range(ncol):
				encryptlist2[i][j]=ciphertext1[x]
				x+=1

	print("\n List to transpose in array format : ")
	finallist=numpy.array(encryptlist2)
	print(finallist)
	listkey = []
	for a in key:
		key1 = int(a)-1
		listkey.append(key1)
	print("\n")
	listkey = numpy.array(listkey)
	finallist = finallist[:,listkey]
	print("The sorted/transposed array is : ")
	print(finallist)
	finallist = finallist.tolist()
	for i in range(nrows):
		for j in range(ncol):
			result += finallist[i][j]
	return(result)

finalenctext = encrypt2(ciphertext1, keysize, key)
print("\n\nFinal encrypted result :\n")
print(finalenctext)
