idade_usuario = int(input('digite a idade do usuario e tecle:\n'))
#usa int() para defiinir que é numero inteiro
#bota \n   para definir numero
#input recebe string
#string: cadeia de caracteres ( tipos de dados)  (tudo com "" (aspas duplas) é string)
#numericos:int e float 
#alfanumericos = "16" " !=16 (tipo logico so pode ter dois valores, sendo true ou false)
# = significa algo em disposição a algo
#exemplo
"titio geo é o batman" ou 'titio geo é o batman'
                                #se ele quiser votar
    if idade_usuario >= 16 and idade_usuario < 18 or idade_usuario >= 60:
        #se ele for de menor usa else
    elif idade_usuario >=18:
        print("o voto deste usuario é obrigatorio.")
        print("fim do elif")
    else:
        print("o voto deste usuário foi facultativo")
        print("fim do else")
#else nunca vai ter condicional (ela se tornara falsa)
#so pode ter else se tiver if antes
#identar = é dar espaço com o (Tab)
#so pode executar codigo se for true
        print("este usuario não esta apto para votar")
        print("fim do if")
        print('\n',"-*-"*10) #para fzr a linha que ele fez
#não pode realizar calculos com duas ""(strings)
#se fizer "16" * 16 = 161616161616161616
    


#-------------------------------------------------------------------------------------------------------

dia_da_semana = int(input('digite um numero de 1 a 7 e tecle enter:\n'))
if dia_da_semana == 1:
    print:("hj é domingo")
    print:("fim do if")
elif dia_da_semana == 2:
    print("hoje é segunda")
elif dia_da_semana == 3:
    print("hj é terça")
elif dia_da_semana == 4:
    print("hj é quarta")
elif dia_da_semana == 5:
    print("hoje é quinta")
elif dia_da_semana == 6:
    print("hoje é sexta")
elif dia_da_semana == 7:
    print("hoje é sabado")
else: 
    print("o numero digitado não tem um dia na semana correspondente")

#---------------------------------------------------------------------------------------------------------

match
    case 1:
        print("hoje é domingo")    
   


#-------------------------------------------------------------------------------------------------------------
#DIA 30/04/2025
#rever while 

import datetime
pergunta = "S"
while pergunta != "N":
    ano_de_nascimento = int(input('ano de nasc do usuario'))
    data = datetime.date.today()
    idade = data.year - ano_de_nascimento
    print(f'o usuario tem {idade}anos.')
    pergunta = input('deseja fazer uma nova verificação? s ou n').upper()
    print("fim do programa")
    
    #while da função de repetção
    
# estrutura FOR    
    
    int n - 0;
    system.out.println("laço while no java")
    while(n < 10) { 
    system.out.println};
    n+
    
    int n - 0;
    system.out.println("laço while no java")
    for(int i = 0 ; i <= 10; i++){ 
    system.out.println};
    n+;
    #-------------------------------------------------------------------------------------------------------------------
    #dia 07/05/2025
    # pesquisar sobre array,stack e heap,variaveis mutaveis e immutaveis e tipagem.
    # responder as perguntas abaixo:

    #1- oq são arrays?quais os tipos de array em python?
    #2-qual a relação existente entre array,stack e heap?
    #3- oq são stack e heap?
    #4- oq são variaveis mutaveis e imutaveis?,estes conceitos se confundem com o conceito de constância?
    #5- como a relação entre arrays,stack e heap difere entre linguagens de tipagem estática e tipagem dinamica?

    #(fazer demostração grafica em todos)

    #bingo para responder a pergunta equivalente ( ele fez um sistema de gambling)

    #---------------------------------------------------------------------------------------------------------------------
    #dia 14/05/2025
    #(primeiro_slider)objetivos:compreender variaveis de multiplos valores,uso de listas como arrays, manipulr listas.
    
    nome = "joao,pedro,maria"
    print(nome[4:9])
    nome 2 =    v               
    
    #-------------------------------------------------------------------------------------------------------------------------
    nome = "joao,pedro,maria"
    nome_1 = "joao" idade_1 = 18
    nome_2 = "pedro" idade_2 = 18
    nome_3 = "maria" idade_3 = 17
    nome_1000 = "antinia" idade_1000 = 20
    #----------------------------------------------------------------------------------------------------------------------------
    nome = [0] == "joao"
    
    #-----------------------------------------------------------------------------
    array de nomes, idades...
    idade = [18,19,20]
    alturas = 185, 160, 190, 172
    
    endereços = (dial, 3800000)
    qua = (não)17,"30000000 )
    - matriz e coordenada para saber local de água ( exemplo: jogos)
#------------------------------------------------------------------------------------

stack_____________Heap
    b=nomes         joão ["ambris"]
#-----------------------------------------------------------------------------------
    for n in (1,10)
    print(n) 1
    #lembrar que posição é sempre nessa ordem ( 0 1 2 3), lembra do 0
    #tem muitos metodos de fazer, mas vai ver  
    #------------------------------------------------------------------------------------
Python_List
    # as listas são delimitadas por cochetes [] (viu que é cochete é arrey), 
    # os elementos são separados por virgula
    #o elemento podem ser de tipos diferentes 

frutas = ['pera','uva','maçã','salada mista']
escolha = frutas[3] #<- para acessarmos um elemento da lista,precisamos o nome da lista e o indicie ou posição do elemento.
print(escolha)

#dica:para descobrir o comprimento de uma lista podemos utilizar a função len(); 
#se quisermos pegar o ultimo elemento de uma lista podemos passar o nome da lista e o valor -1 dento dos--
alfabeto_portugues = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',]
print(f"A ultima letra do aflabeto é: {alfabeto_portugues[-1]}")
#-------------------------------------------------------------------------------------------
nomes = ["lucas","fabio","thiago","samira","leandra","joao","ismar"]
print(len(nomes))
print(nome(4))

for nome in nomes:
print(f"{nomes.index(nome)} - {nome}")

print('percorrendo com while')
c=0 c:1
while c < len(nomes):
print(f"{nomes.index(nome)} - {nomes[c]}")
c+=1
#-------------------------------------------------------------------------------------------
nomes = ["lucas","fabio","thiago","samira","leandra","joao","ismar"]

nomes.insert(,'daniel')
nomes.pop(0)
print(nomes)
#-------------------------------------------------------------------------------------------
#cadastro de alunos

escolha = ''
alunos = []
while escolha !="n":
    aluno = input('digite o nome do aluno e tecle enter:')
    alunos.append(aluno)
    escolha = input("deseja cadastrar novo aluno? S ou N").lower()
#agora quero exibir os alunos
for al in alunos:
print(f"{al} é um(a) aluno(a) dedicado(a).")
#---------------------------------------------------------------------------------------------
nome = "milton"
print(nome[3])
# dai ele vai contar até 0 1 2 3, e no 3 ele mostra o T do nome
#ele passo umas atividades praticas  sobre a aula no slide
#----------------------------------------------------------------------------------------------
# !spoiler! proxima aula vai ser sobre ( Matriz )