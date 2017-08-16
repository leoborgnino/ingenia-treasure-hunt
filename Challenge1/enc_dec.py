from scipy import signal
import matplotlib.pyplot as plt
import random
import math

####################
#  Encoded Section
####################

data_raw = open("data_raw.log",'w')
keys_file = open("key.log",'w')

data_string = "Hola! Felicitaciones! Has conseguido decodificar este texto. El codigo es eH77flmn. Mandarlo por mail a lborgnino@gmail.com\ "

key = [2.5,2.5]

# Data write
data = []
for i in range(len(data_string)):
    data.append(int(ord(data_string[i])))


encoded = signal.deconvolve(data,key)

for i in range(len(encoded[0])):
    data_raw.write("%.2f\n"%encoded[0][i])

# Keys write (OTHER_KEYS: number of extra non-functional keys)    
keys = []
OTHER_KEYS = 100

position = random.randint(0,OTHER_KEYS)

for i in range(OTHER_KEYS):
    if (i == position):
        keys_file.write("%.2f %.2f\n"%(key[0],key[1]))
    else:
        keys_file.write("%.2f %.2f\n"%(random.random()*3,random.random()*3))

keys_file.close()
data_raw.close()

####################
#  Decoded Section
####################

data_encoded_rd = open("data_raw.log",'r')
keys_rd = open("key.log",'r')

# Read Data Raw

data_encoded_lines = data_encoded_rd.readlines()
for i in range(len(data_encoded_lines)):
    data_encoded_lines[i] = data_encoded_lines[i].replace('\n','')
#print data_encoded_lines

# Read Keys

keys_set = keys_rd.readlines()
keys_set_x = []
for i in range(len(keys_set)):
    keys_set_x.append(keys_set[i].replace('\n','').split(' '))
#print keys_set_x

    
la = len(data_encoded_lines)
lb = len(keys_set_x[0])


for j in range(OTHER_KEYS): # j keys iterator
    data_decoded = []
    key_temp = keys_set_x[j]
#    print key_temp
    
# Convolution
    for i in range(int(la+lb-1)): # convolution element iteration
        result = 0.
        for k in range(int(la)): # key parametrized iterator
            if(((i-k)>=0.) & ((i-k)<lb)):
                result += float(data_encoded_lines[k]) * float(key_temp[i-k])
            else:
                result += 0.
        data_decoded.append(result)
# End of convolution

# String Constructor                
    string_decoded = ""
    for i in range(len(data_decoded)):
        if (int(data_decoded[i])) > 255 or (int(data_decoded[i])) < 0:
            #print("Error")
            break
        else:
            string_decoded += chr(int(data_decoded[i]))

# Search 'Hola' word in decoded string           
    if 'Hola' in string_decoded:
        print("Key: %.2f %.2f"%(float(key_temp[0]),float(key_temp[1])))
        print(string_decoded)
        plt.plot(data_encoded_lines)
        plt.show()
        plt.plot(data_decoded[0:-1])
        plt.show()


        


