inverterstring = "eu sou uma string"

def invertstring(string):
    listastring = list(string)
    for i in range(len(listastring)//2):

        temp = listastring[i]
        listastring[i] = listastring[len(listastring) - i - 1]
        listastring[len(listastring) - i - 1] = temp
    stringinvert = ''.join(listastring)

    return stringinvert
print(invertstring(inverterstring))