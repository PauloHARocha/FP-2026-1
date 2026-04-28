# Solicite o nome e a data de nascimento de dois usuarios
# Indique quem é o mais velho

#Usuario 1
u1_nome = input("Usuario 1, insira o nome:")
u1_ano = int(input("Usuario 1, insira o ano de nascimento:"))
u1_mes = int(input("Usuario 1, insira o mes de nascimento:"))
u1_dia = int(input("Usuario 1, insira o dia de nascimento:"))

#Usuario 2
u2_nome = input("Usuario 2, insira o nome:")
u2_ano = int(input("Usuario 2, insira o ano de nascimento:"))
u2_mes = int(input("Usuario 2, insira o mes de nascimento:"))
u2_dia = int(input("Usuario 2, insira o dia de nascimento:"))

if u1_ano < u2_ano:
    print(u1_nome)
elif u1_ano > u2_ano:
    print(u2_nome)
else:
    if u1_mes < u2_mes:
        print(u1_nome)
    elif u1_mes > u2_mes:
        print(u2_nome)
    else:
        if u1_dia < u2_dia:
            print(u1_nome)
        elif u1_dia > u2_dia:
            print(u2_nome)
        else:
            print(u1_nome, u2_nome)