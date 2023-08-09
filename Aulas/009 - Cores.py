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
print(tBranco, ' Olá mundo! - 30',vazio)
print(tVermelho, ' Olá mundo! - 31',vazio)
print(tVerde, ' Olá mundo! - 32',vazio)
print(tAmarelo, ' Olá mundo! - 33',vazio)
print(tAzul, ' Olá mundo! - 34',vazio)
print(tLilás, ' Olá mundo! - 35', vazio)
print(tCiano, ' Olá mundo! - 36', vazio)
print(tCinza, ' Olá mundo! - 37', vazio)

fBranco = '\033[1;40m'
fVermelho = '\033[1;41m'
fVerde = '\033[1;42m'
fAmarelo = '\033[1;43m'
fAzul = '\033[1;44m'
fLilás = '\033[1;45m'
fCiano = '\033[1;46m'
fCinza = '\033[1;47m'
fNovo = '\033[1;49m'
print()
print(fBranco, ' Olá mundo! - 40', vazio)
print(fVermelho, ' Olá mundo! - 41', vazio)
print(fVerde, ' Olá mundo! - 42', vazio)
print(fAmarelo, ' Olá mundo! - 43', vazio)
print(fAzul, ' Olá mundo! - 44', vazio)
print(fLilás, ' Olá mundo! - 45', vazio)
print(fCiano, ' Olá mundo! - 46', vazio)
print(fCinza, ' Olá mundo! - 47', vazio)

sNenhum = '\033[0m'
sNegrito = '\033[2m'
sSublinhado = '\033[4m'
sNegativo = '\033[7m'
sNegrit = '\033[1m'
sItalico = '\033[3m'
sCensor = '\033[8m'
sTachado = '\033[9m'
print()
print(sNenhum, ' Olá mundo! - 0', vazio)
print(sSublinhado, ' Olá mundo! - 4', vazio)
print(sNegrito, ' Olá mundo! - 2', vazio)
print(sNegativo, ' Olá mundo! -7', vazio)
print(sNegrit, ' Olá mundo! - 1', vazio)
print(sItalico, ' Olá mundo! - 3', vazio)
print(sCensor, ' Olá mundo!', vazio, '- Censor - 8')
print(sTachado, ' Olá mundo! - 9', vazio)
