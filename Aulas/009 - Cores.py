print()
'''
    \033[STYLE:TEXT:BACKm
        STYLE           TEXT    |   cor         |   BACK    
    0-  None        ;   30      |   Branco      |   40     m
    1-  Bold        ;   31      |   Vermelho    |   41     m
    4-  Underline   ;   32      |   Verde       |   42     m
    7-  Negative    ;   33      |   Amarelo     |   43     m
                    ;   34      |   Azul        |   44     m
                    ;   35      |   Lilás       |   45     m
                    ;   36      |   Ciano       |   46     m
                    ;   37      |   Cinza       |   47     m

'''
vazio = '\033[m'
tBranco = '\033[30m'
tVermelho = '\033[31m'
tVerde = '\033[32m'
tAmarelo = '\033[33m'
tAzul = '\033[34m'
tLilás = '\033[35m'
tCiano = '\033[36m'
tCinza = '\033[37m'
print(vazio, ' Olá mundo! ', vazio,)
print(tBranco, ' Olá mundo! ',vazio)
print(tVermelho, ' Olá mundo! ',vazio)
print(tVerde, ' Olá mundo! ',vazio)
print(tAmarelo, ' Olá mundo! ',vazio)
print(tAzul, ' Olá mundo! ',vazio)
print(tLilás, ' Olá mundo! ', vazio)
print(tCiano, ' Olá mundo! ', vazio)
print(tCinza, ' Olá mundo! ', vazio)

fBranco = '\033[40m'
fVermelho = '\033[41m'
fVerde = '\033[42m'
fAmarelo = '\033[43m'
fAzul = '\033[44m'
fLilás = '\033[45m'
fCiano = '\033[46m'
fCinza = '\033[47m'
fNovo = '\033[49m'
print()
print(fBranco, ' Olá mundo! ', vazio)
print(fVermelho, ' Olá mundo! ', vazio)
print(fVerde, ' Olá mundo! ', vazio)
print(fAmarelo, ' Olá mundo! ', vazio)
print(fAzul, ' Olá mundo! ', vazio)
print(fLilás, ' Olá mundo! ', vazio)
print(fCiano, ' Olá mundo! ', vazio)
print(fCinza, ' Olá mundo! ', vazio)

sNenhum = '\033[0m'
sNegrito = '\033[2m'
sSublinhado = '\033[4m'
sNegativo = '\033[7m'
sNegrit = '\033[1m'
sItalico = '\033[3m'
sCensor = '\033[8m'
sTachado = '\033[9m'
print()
print(sNenhum, ' Olá mundo! ', vazio)
print(sSublinhado, ' Olá mundo! ', vazio)
print(sNegrito, ' Olá mundo! ', vazio)
print(sNegativo, ' Olá mundo! ', vazio)
print(sNegrit, ' Olá mundo! ', vazio)
print(sItalico, ' Olá mundo! ', vazio)
print(sCensor, ' Olá mundo! ', vazio)
print(sTachado, ' Olá mundo! ', vazio)
