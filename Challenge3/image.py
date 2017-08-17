from scipy import misc
import matplotlib.pyplot as plt
import random
import math

def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolvera Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero

data_string = "https://scontent-eze1-1.xx.fbcdn.net/v/t1.0-9/227082_1036403003799_1159_n.jpg?oh=464e2e95452eceb4c0ad468422997639&oe=59EF63CF "

f = misc.imread('tarpuy.png') # uses the Image module (PIL)

plt.imshow(f)
plt.show()

temp_counter = 0
for i in range(len(data_string)):
    while (not(es_primo(temp_counter))):
        temp_counter += 1
    print temp_counter
    f[temp_counter][temp_counter][1] = ord(data_string[i])
    temp_counter += 1
    
plt.imshow(f)
plt.show()

data_decoded = ""
temp_counter = 0
for i in range(len(data_string)):
    while (not(es_primo(temp_counter))):
        temp_counter += 1
    data_decoded += (chr(f[temp_counter][temp_counter][1]))
    temp_counter += 1
    
print data_decoded

print type(f)
print f.shape
print f.dtype
