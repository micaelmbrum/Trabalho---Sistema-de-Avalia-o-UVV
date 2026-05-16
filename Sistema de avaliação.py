import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
#validador de notas para nao aceitar notas fora do maximo permitido 
def validar_nota(mensagem, min_val, max_val):
    while True:
        try:
            nota = float(input(mensagem))
            if nota < min_val or nota > max_val:
                print(f"Erro: A nota deve estar entre {min_val} e {max_val}.")
                continue
            return nota
        except ValueError:
            print("Erro: Digite um número válido.")
aprovados = 0
reprovados = 0
total_alunos = 0
# aqui o loop com +1 para finalizar e gerar o relatorio quando terminar de inserir as notas
while True:
    total_alunos += 1
    print(f"\nALUNO {total_alunos}")
    aop1 = validar_nota("Nota [0, 1] na AOP1: ", 0, 1)
    aop2 = validar_nota("Nota [0, 2] na AOP2: ", 0, 2)
    aop3 = validar_nota("Nota [0, 1] na AOP3: ", 0, 1)
    prova_regular = validar_nota("Nota [0, 6] da PROVA REGULAR: ", 0, 6)
    mm = aop1 + aop2 + aop3 + prova_regular
    print(f"Media: {mm:.2f}")
    # aqui e para somar as notas e dizer se foi aprovado, ficou de recuperação ou reprovado
    if mm < 3.0:
        status = "Reprovado"
        reprovados += 1
        print(f"Status: {status}")
    elif mm >= 7.0:
        status = "Aprovado"
        aprovados += 1
        print(f"Status: {status}")
    else:
        prova_recuperacao = validar_nota("Nota [0, 10] da PROVA DE RECUPERACAO: ", 0, 10)
        media_geral = (mm + prova_recuperacao) / 2     
        print(f"Prova de Recuperacao: {prova_recuperacao:.2f}")
        print(f"Media Geral: {media_geral:.2f}") 
        if media_geral >= 5.0:
            status = "Aprovado"
            aprovados += 1
        else:
            status = "Reprovado"
            reprovados += 1
        print(f"Status Final: {status}")
    # coloquei para perguntar se quer continuar ou nao e limpar a tela 
    print()
    continuar = input("Deseja inserir mais um aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break
    limpar_tela()
# relatorio final dos alunos aprovados e reprovados  
print("\n" + "="*50)
print("RELATORIO FINAL")
print("="*50)
print(f"Total de alunos: {total_alunos}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")
print(f"\nPorcentagem de APROVADOS: {(aprovados/total_alunos)*100:.2f}%")
print(f"Porcentagem de REPROVADOS: {(reprovados/total_alunos)*100:.2f}%")
print("="*50)