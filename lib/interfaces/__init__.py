def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[31m Erro: digite um numero inteiro valido\033[m')
            continue
        else:
            return n



def linha(tam=42):
    return '_'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu (lista):
    cabeçalho('Menu Principal')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua Opção\033[m')
    return opc

