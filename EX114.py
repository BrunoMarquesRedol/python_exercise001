
def tenteconectar(msg):
    from urllib import request, error
    try:
        site = request.urlopen(f'http://{msg}')
    except:
        print(f'\n\033[1;31mO site não está disponível no momento.\033[m')
    else:
        print(f'\n\033[1;34mO site está acessivel!\033[m')

--
from ex114.utilidadescev import dado

url = dado.tenteconectar(str(input('Site para avaliar: ')))