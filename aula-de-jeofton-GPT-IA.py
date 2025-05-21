🐍 Python - Resumo de Anotações com Exemplos e Dicas
📥 Entrada de Dados e Tipos
python
Copiar
Editar
idade_usuario = int(input('Digite a idade do usuário:\n'))
input() → recebe dados como string (str)

int() → converte para número inteiro

\n → quebra de linha

Tipos de dados:

Numéricos: int, float

Texto: str

Lógicos: bool (True ou False)

🔀 Condicionais
Votação (exemplo corrigido)
python
Copiar
Editar
if idade_usuario >= 18 and idade_usuario < 60:
    print("Voto obrigatório")
elif idade_usuario >= 16 or idade_usuario >= 60:
    print("Voto facultativo")
else:
    print("Não vota")
Dicas:
==: igual

!=: diferente

and, or, not: operadores lógicos

else não recebe condição

if deve vir primeiro

Tab para identação correta

📅 Dia da Semana com if
python
Copiar
Editar
dia_da_semana = int(input('Digite um número de 1 a 7:\n'))
if dia_da_semana == 1:
    print("Hoje é domingo")
elif dia_da_semana == 2:
    print("Hoje é segunda")
elif dia_da_semana == 3:
    print("Hoje é terça")
elif dia_da_semana == 4:
    print("Hoje é quarta")
elif dia_da_semana == 5:
    print("Hoje é quinta")
elif dia_da_semana == 6:
    print("Hoje é sexta")
elif dia_da_semana == 7:
    print("Hoje é sábado")
else:
    print("Número inválido")
🆕 Dia da Semana com match-case (Python 3.10+)
python
Copiar
Editar
dia = int(input("Digite o número do dia (1 a 7): "))
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido.")
🕑 Laço de Repetição while com datetime
python
Copiar
Editar
import datetime

pergunta = "S"
while pergunta != "N":
    ano = int(input('Ano de nascimento: '))
    idade = datetime.date.today().year - ano
    print(f"O usuário tem {idade} anos.")
    pergunta = input("Deseja continuar? S ou N: ").upper()
print("Fim do programa")
🔁 Repetição com for
python
Copiar
Editar
for i in range(1, 11):
    print(i)
range(início, fim) (o fim não é incluído)

💻 Código Java (Comparativo)
java
Copiar
Editar
// While em Java
int n = 0;
while(n < 10) {
    System.out.println(n);
    n++;
}

// For em Java
for(int i = 0; i <= 10; i++) {
    System.out.println(i);
}
📚 Listas (Arrays em Python)
python
Copiar
Editar
frutas = ['pera', 'uva', 'maçã', 'salada mista']
print(frutas[2])  # maçã
Acessar último elemento: lista[-1]

Comprimento da lista: len(lista)

Exemplo:
python
Copiar
Editar
alfabeto = ['a','b','c','d','e']
print(f"A última letra é: {alfabeto[-1]}")
🧪 Operações com Listas
python
Copiar
Editar
nomes = ["lucas", "fabio", "thiago"]
nomes.append("daniel")     # adiciona no fim
nomes.insert(1, "joana")   # insere na posição 1
nomes.pop(0)               # remove o primeiro
print(nomes)
📝 Cadastro de Alunos
python
Copiar
Editar
alunos = []
escolha = ''

while escolha != 'n':
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)
    escolha = input("Deseja cadastrar outro aluno? (s/n): ").lower()

for aluno in alunos:
    print(f"{aluno} é um(a) aluno(a) dedicado(a).")
🔠 Strings e Fatiamento
python
Copiar
Editar
nome = "milton"
print(nome[3])      # mostra 'l'
print(nome[1:4])    # mostra 'ilt'
🧩 Conceitos Teóricos
📦 O que são arrays?
Coleção ordenada de dados

Em Python, usamos listas

Ex: numeros = [1, 2, 3, 4]

📚 Stack vs Heap
Conceito	Stack (Pilha)	Heap (Montão)
Uso	Variáveis locais	Objetos grandes
Acesso	Mais rápido	Mais lento (via ponteiros)
Ordem	LIFO	Acesso aleatório

🔃 Variáveis Mutáveis x Imutáveis
Mutáveis: listas, dicionários

Imutáveis: inteiros, strings, tuplas

python
Copiar
Editar
lista = [1, 2, 3]  # mutável
texto = "abc"      # imutável
🔡 Tipagem:
Dinâmica: Python – tipo definido em tempo de execução

Estática: Java, C – tipo definido na declaração

🧠 Exercícios propostos (para estudar):
O que são arrays? Quais tipos em Python?

Qual a relação entre arrays, stack e heap?

O que são stack e heap?

O que são variáveis mutáveis e imutáveis?

Como a tipagem afeta o uso de stack e heap?

📌 Dicas Extras
Strings com números: "16" * 3 = 161616 (concatenação)

Não dá para fazer "16" + 16 (erro!)

Sempre identar (Tab) blocos de if, for, while

Use print() para testar partes do código

🧭 Resumo Visual
text
Copiar
Editar
🔤 Tipos: int, float, str
📥 input() → str
🔀 if / elif / else
🔁 while / for
📋 listas: append, pop, insert
🔠 strings: índices, fatiamento
🧩 teoria: arrays, stack, heap
🛠 mutável x imutável
