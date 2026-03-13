alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno para adiciona-lo: ")
    idade = int(input("Digite a idade do aluno: "))
    while True:
         nota = float(input("Digite a nota do aluno: "))
         if nota>=0 and nota<=10:
            break
         else:
          print("nota invalida")
         
    dados = {
     'nome':nome,
    'idade':idade,
  'nota':nota
 }
       
    alunos.append(dados)

    print(f"Nome: {nome} , Idade: {idade} , Nota: {nota}")


def listar_aluno():
   if len(alunos) ==0:
      print("sem alunos listados")
      return

   for aluno in alunos:
         print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}")

def buscar_aluno():
    buscador = input("Digite o nome do aluno para acha-lo no sistema: ")
    for aluno in alunos:
        if aluno['nome'].lower() == buscador.lower():
            print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}")


def remover_aluno():
   buscador = input("Digite o nome do aluno para remove-lo do sistema: ")
   for aluno in alunos:
      if aluno['nome'] == buscador:
        alunos.remove(aluno)
        print("Aluno removido")

def media_notas():
   if len(alunos)==0:
      print("Sem alunos cadastrados")
   soma = 0
   for aluno in alunos:
      soma += aluno['nota']
      media = soma/len(alunos)
      print(f"A média geral das notas dos alunos é: {media}")


   
      
    



while True:
   menu = int(input("\n Escolha uma opção: \n1.Adicionar aluno \n2.Listar aluno\n3.Buscar aluno\n4.Remover aluno\n5.Ver média geral das notas\nOpção: "))
   match menu:
      case 1:
         adicionar_aluno()
      case 2:
         listar_aluno()
      case 3:
         buscar_aluno()
      case 4:
         remover_aluno()
      case 5:
         media_notas()
      case _:
        print ("Programa Encerrado")
        break 