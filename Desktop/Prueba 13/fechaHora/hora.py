import helps

lista = helps.listaFechaHora()

for i in lista:
    if(i.count(':') == 2):
        lista = i.split(':')
        break

if int(lista[0]) >= 19 and int(lista[0]) <=24:
    print('ya son las {} ves a descansar, mucho trabajo!'.format(lista[0]+':'+lista[1]))
else:
    print('Pilas, te quedan {} horas para seguir trabajando'.format(19-int(lista[0])))

