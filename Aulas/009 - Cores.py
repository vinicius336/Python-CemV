print()
'''
    \033[STYLE:TEXT:BACKm
        STYLE           TEXT    |   cor         |   BACK    
    0-  None        ;   30      |   Branco      |   40     m
    1-  Bold        ;   31      |   Vermelho    |   41     m
    4-  Underline   ;   32      |   Verde       |   42     m
    7-  Negative    ;   33      |   Amarelo     |   43     m
                    ;   34      |   Azul        |   44     m
                    ;   34      |   Lilás       |   45     m
                    ;   35      |   Ciano       |   46     m
                    ;   37      |   Cinza       |   47     m

'''
print('\033[m Olá mundo! \033[m')
print('\033[31;43m Olá mundo! \033[m')
print('\033[1;31;43m Olá mundo! \033[m')
print('\033[4;30;45m Olá mundo! \033[m')
print('\033[1;32;45m Olá mundo! \033[m')
