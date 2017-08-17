from scipy import signal
import matplotlib.pyplot as plt
import random
import math

####################
#  Encode Section
####################

datafile = open("data_raw.log",'w')

data_string = "Felicitaciones! Has conseguido decodificar este texto. El codigo es 33mkJ78. Mandarlo por mail a lborgnino@gmail.com"

#Data write

data = []
for i in range(len(data_string)):
    data.append(int(ord(data_string[i])))
#print data

data_coded = []
for i in range(len(data)):
    if (i == 0):
        data_coded.append(data[i])
    else:
        data_coded.append( (data[i-1] + data[i]) )
#print data_coded

data_bin = []

for i in data_coded:
    data_bin.append(format(i,'#010b'))
    
for i in range(len(data_bin)):
    data_bin[i] = data_bin[i].replace("0b","")

#print data_bin
    
parity = []
temp_counter = 0
for i in range(len(data_bin)):
    temp_counter = 0
    for j in range(len(data_bin[0])):
        if data_bin[i][j] == '1':
            temp_counter += 1
    if(temp_counter%2):
        parity.append(0)
    else:
        parity.append(1)
        
#print parity


EXTRA_DATA = 5
data_noised = []

for i in range(len(data_bin)):
    flag_change = 0
    for j in range(EXTRA_DATA):
        data_noised.append(list(data_bin[i]))
        position = random.randint(0,len(data_bin[0])-1)
        if (random.random() > 0.5 and (flag_change != (EXTRA_DATA-2))):
            flag_change += 1
            if (data_noised[i*EXTRA_DATA+j][position] == '1'):
                data_noised[i*EXTRA_DATA+j][position] = "0"
            else:
                data_noised[i*EXTRA_DATA+j][position] = "1"
                
data_noised_string = []
for i in data_noised:
     data_noised_string.append("".join(i))
#print data_noised_string

data_noised_parity = []

for i in range(len(data_noised_string)):
    temp_string = str(parity[int(i/(EXTRA_DATA+0.))]) + data_noised_string[i]
    data_noised_parity.append(temp_string)
    datafile.write("%s\n"%temp_string)

#print data_noised_parity
datafile.close()

####################
#  Decode Section
####################

file_read = open("data_raw.log",'r')

# Read Data Raw

data_encoded_lines = file_read.readlines()
for i in range(len(data_encoded_lines)):
    data_encoded_lines[i] = data_encoded_lines[i].replace('\n','')

data_decoded = []
temp_counter = 0
for i in range(len(data_encoded_lines)/EXTRA_DATA):
    for k in range(EXTRA_DATA):
        temp_counter = 0
        for j in range(len(data_encoded_lines[0])-1):
            if data_encoded_lines[i*EXTRA_DATA+k][j+1] == '1':
                temp_counter += 1
        if ((temp_counter%2) != int(data_encoded_lines[i*EXTRA_DATA+k][0])):
            data_decoded.append(data_encoded_lines[i*EXTRA_DATA+k][1:])
            break

data_decoded_int = []
for i in data_decoded:
    data_decoded_int.append(int(i,2))

data_decoded_final = []
for i in range(len(data_decoded_int)):
    if (i == 0):
        data_decoded_final.append(data_decoded_int[i])
    elif (i == 1):
        data_decoded_final.append(data_decoded_int[i]-data_decoded_int[i-1])
    else:
        data_decoded_final.append(data_decoded_int[i]-data_decoded_final[i-1])
        

#print data_decoded_final
    
temp_counter = 0
for i in range(len(data_decoded_final)):
    if ( data_decoded_final[i] == data[i]):
        temp_counter += 1

# print data
# print temp_counter
# print len(data_decoded_int)
# print len(data)

string_decoded = ""
if temp_counter == len(data_decoded_final):
    print "OK"
    for i in range(len(data_decoded_final)):
        string_decoded += chr(data_decoded_final[i])
    print string_decoded
                
        


