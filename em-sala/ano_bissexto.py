ano = input("Insira um ano: ")
ano = int(ano)

if ano % 400 == 0:
    print("ANO BISSEXTO")
elif ano % 100 == 0:
    print("ANO COMUM")
elif ano % 4 == 0:
    print("ANO BISSEXTO")
else:
    print("ANO COMUM")
