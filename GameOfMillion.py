import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint
import time
#Banco de Perguntas e váriaveis
global Perguntas #0 para começar contagem do 1
Perguntas = [0,'A função real de variável real, definida por f (x) = (3 – 2a).x + 2, é crescente quando:','Calcule o valor de 5x² + 15x = 0 para que f(x) = 0','Cinco galinhas botam 10 ovos por dia. Quantos ovos botam 12 galinhas?','Qual montante teremos em 4 meses se aplicarmos um capital inicial de R$5.000,00 a um juros simples de 5% ao mês?','Como se monta a estrutura do for em C?','Como se monta a estrutura do for em Python?','Uma váriavel do tipo char em C aceita que entradas?','Como printar alguma frase em python?','Qual a equivalência lógica de p -> q?','Qual a equivalência lógica de p <-> q?','Qual a tabela verdade de p -> q?','Qual a tabela verdade de p ^ q?','Quanto vale 6(decimal) na base 2?','Quanto vale 1010(base 2) na base 10?','Qual o valor da soma na base 2 de 110+111?','Qual o valor da subtração na base 2 de 1000-111?',"Qual o f'(x) de f(x) = x² + 10x³?","Qual o f'(x) de f(x) = 2x² - e^x?","Qual o f'(x) de f(x) = senx?","Qual o f'(x) de f(x) = cosx?",'O que vai ser exibido? for(i = 0;i<10;i++){ if(i%2==0){continue;} printf("%d", i);}?','O que os progamadores mais esquecem ao utilizar a linguagem C?','O que são ponteiros na linguagem C?','O que é e para que serve a estrutura switch/case?','O que é o mapa de Karnaugh?','Para que serve o Multiplexador?','Para que serve o Demultiplexador?','O que é um Flip-flop?','Se Fortaleza fica no Ceará, então Ceará é maior que fortaleza. É equivalente a:','Fortaleza é melhor que o Ceara se e somente se o Papai Noel existir. É equivalente a:','Ou Ceará é o melhor ou Fortaleza é o melhor. É equivalente a:','Fortaleza é a capital e Ceará é um estado ou Não fazem parte do Brasil É equivalente a:','Ache uma equação da reta tangente à curva y = x³ - 4 no ponto (2,4)','Qual a derivada de ordem 121 de f(x) = cosx?',"Qual o f'(x) de f(x) = senx * cosx?",'Qual o dy/dx de y = cotg e^tgx?','Esse código da linguagem C possui algum erro? printf("Melhor jogo ein!")','Qual é o método mais rápido de ordenação?','Esse código da linguagem Python possui algum erro? print("Melhor jogo ein, nota ", x, "!")','O que esse comando faz: (10 % 2)?','Quais estados são proibidos no Flip-flop Tipo D e uma de suas utilidades?','Quais estados são proibidos no Flip-flop tipo T e uma de suas utilidades?','Com quantos mux de 8 canais obtemos um mux de 64 canais?','Com quantos demux de 2 canais obtemos um demux de 8 canais?','Usando as Regras de Inferência: (p -> q)^ ~q =>','Usando as Regras de Inferência: (p \/ q)^ ~p =>','Usando as Regras de Inferência: (p -> q)^ p =>','Usando as Regras de Inferência: (p -> q)^(q -> s) =>','Qual a derivada de y+xy+y² = 4?','Quais valores de x geram pontos críticos de f(x) = x³-3x²+3?','Qual valor de x gera assíndota vertical de f(x) = 2/x-4?','Dy(cotgy*cossecy) = ?','Qual item é obrigatório em Python e não em C?',"Qual item é obrigatório em C e não em Python?","Qual nota esse jogo merece?","Qual dessas pessoas não precisa jogar o Show do Milhão?",        'Qual a data de anivérsario do professor Joacillo?', "Qual a forma simplificada de S = A* B *C + A * ~C + A * ~B? (~ = Barrado)", "Qual a forma simplificada de S = (A * B * ~C)* (~A + ~B + ~C)?", "Qual a forma simplificada de S = ~A * B + A * ~B + A * B?",'Todos os marinheiros são republicanos. Assim sendo,','A negação de “hoje é segunda-feira e amanhã não choverá” é','Qual a negação da proposição “Algum funcionário da agência P do Banco do Brasil tem menos de 20 anos”?','A proposição funcional “Para todo e qualquer valor de n, tem-se 6n < n² + 8  ” será verdadeira, se n for um número real']
global Itens #0,1,2,3,4 para que criar uma função que a pergunta 1 equivala aos itens 5-9 e ai por diante. Por que a ultima pergunta não teria itens caso os Itens começassem do 1
Itens = [0,1,2,3,"A = a > 0","B = a < 3/2","C = a > 3/2","D = a < 3","A = f(x) = 0, x = -3 e x = -6","B = f(x) = 0, x = 0 e x = –6","C = f(x) = 0, x = -3 e x = –9","D = f(x) = 0, x = 0 e x = –3","A = 12 ovos","B = 18 ovos","C = 24 ovos","D = 30 ovos","A = 5250","B = 5500","C = 5750","D = 6000","A = for([condição]; [váriavel]; [incremento]){}","B = for([variável]; [condição]; [incremento]){}","C = for([variável]; [incremento]; [condição]){}","D = for([incremento]; [condição]; [váriavel]){}","A = for item in range(x):","B = for item range(x):","C = for item in range","D = for item in range(x)","A = Letras","B = Números","C = Números e letras","D = Números, letras e imagens","A = printf('Vou acertar!')","B = printf('Vou acertar!');","C = print('Vou acertar!')","D = prints('Vou acertar!');","A = p ^ q ","B = ~p ^ q","C = p \/ q","D = ~p \/ q","A = (p->q)^(q->p)","B = (~p->q)^(q->p)","C = (p->~q)^(q->p)","D = (p->q)^(q->~p)","A = VVFF","B = VFVV","C = VVFV","D = VVVF","A = VFFF","B = VFFV","C = FVVF","D = FFFV","A = 101","B = 110","C = 111","D = 011","A = 9","B = 11","C = 12","D = 10","A = 1010","B = 1101","C = 1100","D = 1001","A = 0010","B = 0001","C = 0100","D = 0000","A = f'(x) = 2x + 30x³","B = f'(x) = 2x² + 30x³","C = f'(x) = 2x + 30x²","D = f'(x) = 2x² + 30x²","A = f'(x) = 4x - e^x","B = f'(x) = 4x² - 1","C = f'(x) = 4x - 1","D = f'(x) = 4x² - e^x","A = -2cosx","B = 2cosx","C = -cosx","D = cosx","A =  2senx","B = -senx","C = -2senx","D = senx","A = Valores pares de 0 a 10","B = Valores ímpares de 0 a 10","C = Os valores 1,3,5,6,7 e 9","D = Os valores 0, 1, 3, 5, 7 e 9","A = Usar os :","B = Usar o ;","C = Usar a dupla aspas","D = Usar printf","A = Ponteiros são variáveis sem utilidade na programação.","B = Ponteiros são variáveis que destroem outras variáveis.","C = Ponteiros são variáveis que apagam o endereço de memória de outras variáveis.","D = Ponteiros são variáveis que armazenam o endereço de memória de outras variáveis.","A = É uma estrutura de condição que define o código a ser executado com base em uma comparação de valores.","B = É uma estrutura de repetição que define o código a ser executado com base em uma repetição de valores.","C = É uma estrutura de condição que define o código a ser executado com base em uma repetição de valores.","D = É uma estrutura de repetição que define o código a ser executado com base em uma comparação de valores.","A = Metódo gráfico para somar binários","B = Metódo gráfico para simplificar a saída S a partir da tabela verdade","C = Metódo gráfico para simplificar a saída S a partir da soma de binários","D = Metódo gráfico para somar binários a partir da tabela verdade","A = Para enviarmos as informações contidas em vários canais a vários outros canais","B = Para simplificar a saída S a partir da tabela verdade","C = Para enviarmos as informações contidas em um canal à vários canais","D = Para enviarmos as informações contidas em vários canais à um só canal","A = Para enviarmos as informações contidas em vários canais à um só canal","B = Para enviarmos as informações contidas em um canal à vários canais","C = Para simplificar a saída S a partir da tabela verdade","D = Para enviarmos as informações contidas em vários canais a vários outros canais","A = Circuito combinacional em que as saídas dependem das entradas e dos estados anteriores das saídas","B = Circuito combinacional em que as saídas dependem das saídas e dos estados anteriores das entradas","C = Para enviarmos as informações contidas em vários canais à um só canal","D = Para enviarmos as informações contidas em vários canais à um só canal","A = P -> q","B = P <-> q","C = (~p ^ q)\/(p ^ ~q)","D = (p ^ q)\/r","A = P -> q","B = P <-> q","C = (~p ^ q)\/(p ^ ~q)","D = (p ^ q)\/r","A = P -> q","B = P <-> q","C = (~p ^ q)\/(p ^ ~q)","D = (p ^ q)\/r","A = P -> q","B = P <-> q","C = (~p ^ q)\/(p ^ ~q)","D = (p ^ q)\/r","A = y = 13x - 19","B = y = 12x - 20","C = y = 14x - 23","D = y = 10x - 30","A = -cosx","B = senx","C = cosx","D = -senx","A = cos²x + sen²x","B = - cos²x - sen²x","C = cos²x - sen²x","D = 2cos²x + 2sen²x","A =secx * e^tgx *(-cossec²e^tgx)","B = sec²x * e^tgx *(-cossec²e^tgx)","C = sec²x * e^tgx *(-cossece^tgx)","D = sec²x * e^tgx *(-cossec²e^sec²x)","A = Dupla aspas","B = Esqueceu o ;","C = Colocou um f após o print","D = Não há erro","A = Selection Sort","B = Quick Sort","C = Insertion Sort","D = Fast Sort","A = Faltou o ;","B = faltou o f após o print, printf","C = Não há erro","D = Dupla aspas","A = Porcentagem","B = Divisão","C = Resto da divisão","D = Multiplicação","A = J = 0 e K = 0, contador síncrono","B = J = 0 e K = 1, registrador de deslocamento","C = J = 1 e K = 0, contador síncrono","D = J = 1 e K = 1, registrador de deslocamento","A = J = 0 e K = 0, contador síncrono","B = J = 0 e K = 1, contador assíncrono","C = J = 1 e K = 0, registrador de deslocamento","D = J = 1 e K = 1, registrador de deslocamento","A = 8","B = 9","C = 10","D = 7","A = 5","B = 6","C = 7","D = 8","A = q, Modus Tollens","B = ~q, Modus Ponnens","C = p, Modus Ponnens","D = ~p, Modus Tollens","A = q, Silogismo Dijuntivo","B = ~q, Silogismo Hipotetico","C = p, Silogismo Hipotetico","D = ~p,Silogismo Dijuntivo","A = p, Modus Tollens","B = ~p, Modus Ponnens","C = q, Modus Ponnens","D = ~q, Modus Tollens","A = p -> s, Silogismo Dijuntivo","B = ~p -> s, Silogismo Hipotetico","C = p -> s, Silogismo Hipotetico","D = ~p -> s, Silogismo Dijuntivo","A = 1 + (1 * y + x *1) + 2y","B = y' + (1 * y + x * y') + 2y * y'","C = 1 + (1 * y + x *1) + 2y²","D = y' + (1 * y + x * y') + 2y²","A = x = 1 ou x = 0","B = x = 0 ou x = 2","C = x = -2 ou x = 2","D = x = -1 ou x = 0","A = x = 1","B = x = 2","C = x = 3","D = x = 4","A = cosse³y - cotg²y * (-cossecy)","B = cosse³y - cotg²y * (cossecy)","C = -cosse³y + cotg²y * (-cossecy)","D = -cosse³y + cotg²y * (cossecy)","A = A endentação","B = As duplas aspas","C = O ponto e virgula","D = O def main()","A = A endentação","B = O for","C = O ponto e vírgula","D = O if","A = 9","B = 10","C = 8","D = 7","A = Jamile e Matheus","B = Caio e Luan","C = Magno e Lucas","D = Marcos Vinicius e Lara","A = 01/03","B = 02/03","C = 03/03","D = 04/03","A = S = A", "B = S = A * B * ~C","C = S = A + B","D = S = ~A","A = S = A","B = S = A * B * C","C = S = A + ~B","D = S = A * B * ~C","A = S = A","B = S = A + ~B","C = S = A + B","D = S = ~A","A = O conjunto dos marinheiros contém o conjunto dos republicanos;","B = O conjunto dos republicanos contém o conjunto dos marinheiros;","C = Todos os republicanos são marinheiros;","D = Algum marinheiro não é republicano","A = hoje não é segunda-feira e amanhã não choverá","B = hoje não é segunda-feira ou amanhã choverá","C = hoje não é segunda-feira então amanhã choverá","D = hoje não é segunda-feira nem amanhã choverá","A = Todo funcionário da agência P do Banco do Brasil tem menos de 20 anos.","B = Não existe funcionário da agência P do Banco do Brasil com 20 anos.","C = Algum funcionário da agência P do Banco do Brasil tem mais de 20 anos.","D = Nenhum funcionário da agência P do Banco do Brasil tem menos de 20 anos.","A = menor que 8.","B = menor que 4.","C = menor que 2.","D = maior que 2." ]
global Respostas #Respostas Só os itens em Maisculo
Respostas = [0,"B","D","C","D","B","A","C","C","D","A","B","A","B","D","B","B","C","A","D","B","B","B","D","A","B","D","B","A","A","B","C","D","B","D","C","B","B","B","C","C","D", "B", "B", "C", "D", "A", "C","C","B","B","D","C","A","C","B","A","A","A","D","C","B","B","B","C"]
global Win, Stop, Lose #Lista para fazer com que os valores dos premios suba de acordo com o jogo real
Win, Stop, Lose = ["1000 Reais", "2000 Reais", "3000 Reais", "4000 Reais", "5000 Reais", "10000 Reais", "20000 Reais", "30000 Reais", "40000 Reais", "50000 Reais", "100000 Reais", "200000 Reais", "300000 Reais", "400000 Reais", "500000 Reais", "1000000 Reais"], ["0 Reais", "1000 Reais", "2000 Reais", "3000 Reais", "4000 Reais", "5000 Reais", "10000 Reais", "20000 Reais", "30000 Reais", "40000 Reais", "50000 Reais", "100000 Reais", "200000 Reais", "300000 Reais", "400000 Reais", "500000 Reais"], ["0 Reais", "500 Reais", "1000 Reais", "1500 Reais", "2000 Reais", "2500 Reais", "5000 Reais", "10000 Reais", "15000 Reais", "20000 Reais", "25000 Reais", "50000 Reais", "100000 Reais", "150000 Reais", "200000 Reais", "0 Reais"]
global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards, k, random #Parametro das váriaveis
x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards = 1, 4, 0, 1, 1, 1, 1, 1, 1, 1
#Funções dos Botões
def P1(): #Pular 1
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards, k, random, Win, Stop, Lose, Perguntas, Itens, Respostas, Teste, Jogo
    TF = messagebox.askyesno("Pular", "Você tem certeza que deseja pular?")
    if(TF == True and Pu1 == 1):
        k = random #Dando valor do random pro K, para o while
        Pu1 -= 1 #Diminuindo a quantidade de Pulares disponivel
        while(k == random): #Para que não se repita a pergunta
            random = randint(x,y)
        Jogo.destroy()
        #Janela Principal do Tkinter Para executar a ação do P1
        Jogo = Tk()
        Jogo.title("Jogo do Milhão")
        Jogo['background'] = "#002240"
        #Perguntas
        Answer = tkinter.StringVar()
        Answer = Perguntas[random]
        #Perguntas Label
        Pergunta = Label(text = Answer, relief = RIDGE, background = "#DD0000", font = ("Viner Hand ITC", 12, "bold"), foreground = "white")
        Pergunta.grid(row = 0, column = 0, columnspan = 30, ipadx = 10, ipady = 20, sticky = W)
        #Variavel da comparação da resposta
        Teste = tkinter.StringVar()
        #Alternativa A
        ItemA = tkinter.StringVar()
        ItemA = Itens[random*4]
        #Alternativa A Buttom
        A = tkinter.Radiobutton(Jogo, text = ItemA, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"),foreground = "white", variable = Teste, value = "A", command = Resposta)
        A.grid(row = 1, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa B
        ItemB = tkinter.StringVar()
        ItemB = Itens[random*4+1]
        #Alternativa B Buttom
        B = tkinter.Radiobutton(Jogo, text = ItemB, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "B", command = Resposta)
        B.grid(row = 2, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa C
        ItemC = tkinter.StringVar()
        ItemC = Itens[random*4+2]
        #Alternativa C Buttom
        C = tkinter.Radiobutton(Jogo, text = ItemC, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "C", command = Resposta)
        C.grid(row = 3, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa D
        ItemD = tkinter.StringVar()
        ItemD = Itens[random*4+3]
        #Alternativa D Buttom
        D = tkinter.Radiobutton(Jogo, text = ItemD, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "D", command = Resposta)
        D.grid(row = 4, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Linha vazia Label
        Vazio = Label(text = " ", background = "#002240", font = ("High tower text", 15, "bold"), foreground = "white")
        Vazio.grid(row = 5, column = 0, columnspan = 30, ipadx = 3, ipady = 3, sticky = W)
        #Ajudas Label
        Ajudas = Label(text = "Ajudas", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Ajudas.grid(row = 6, column = 0, columnspan = 3, ipadx = 3, ipady = 3, sticky = W)
        #Pular1 Buttom
        if(Pu1 == 1):
            Pular = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P1)
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Pular2 Buttom
        if(Pu2 == 1):
            Pular1 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P2)
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        else:
            Pular1 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        #Pullar3 Buttom
        if(Pu3 == 1):
            Pular2 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P3)
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular2 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Cartas Buttom
        if(Cards == 1):
            Cartas = tkinter.Button(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda1)
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Cartas = Label(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Professor Buttom
        if(Teacher == 1):
            Professor = tkinter.Button(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda2)
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        else:
            Professor = Label(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        #Engenheiros Buttom
        if(Alunos == 1):
            Engenheiros = tkinter.Button(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda3)
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Engenheiros = Label(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Premios Buttom
        Premios = Label(text = "Prêmios", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Premios.grid(row = 6, column = 4,  ipadx = 3, ipady = 3, sticky = W)
        #Perder Label
        Perder = Label(text = "Perder", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder.grid(row = 7, column = 4, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Perder Valor
        ValorP = tkinter.StringVar()
        ValorP = Lose[z]
        Perder1 = Label(text = ValorP, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder1.grid(row = 7, column = 5, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Parar Buttom
        Parar = tkinter.Button(Jogo, text = "Parar", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Desistir)
        Parar.grid(row = 8, column = 4, ipadx = 7, ipady = 5, sticky = W)
        #Parar Valor
        ValorD = tkinter.StringVar()
        ValorD = Stop[z]
        Parar1 = Label(Jogo, text = ValorD, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Parar1.grid(row = 8, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Acertar Label
        Acertar = Label(text = "Acertar",background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar.grid(row = 9, column = 4, ipadx = 5, ipady = 10, pady = 1, sticky = W)
        #Valor
        ValorA = tkinter.StringVar()
        ValorA = Win[z]
        Acertar1 = Label(text = ValorA, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar1.grid(row = 9, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Logo do jogo Imagem
        Logo = PhotoImage(file = "C:/Users/Marcos/Documents/trabalho programação/Jogo do Milhão/Show.png")
        Marca = Label(image = Logo,background = "#002240")
        Marca.Logo = Logo
        Marca.grid(row = 5, rowspan = 10, column = 12, columnspan = 50, sticky = SE)
        Jogo.mainloop()
def P2():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards, k, random, Win, Stop, Lose, Perguntas, Itens, Respostas, Teste, Jogo
    TF = messagebox.askyesno("Pular", "Você tem certeza que deseja pular?")
    if(TF == True and Pu2 == 1):
        k = random #Dando valor do random pro K, para o while
        Pu2 -= 1 #Diminuindo a quantidade de Pulares disponivel
        while(k == random): #Para que não se repita a pergunta
            random = randint(x,y)
        Jogo.destroy()
        #Janela Principal do Tkinter.
        Jogo = Tk()
        Jogo.title("Jogo do Milhão")
        Jogo['background'] = "#002240"
        #Perguntas
        Answer = tkinter.StringVar()
        Answer = Perguntas[random]
        #Perguntas Label
        Pergunta = Label(text = Answer, relief = RIDGE, background = "#DD0000", font = ("Viner Hand ITC", 12, "bold"), foreground = "white")
        Pergunta.grid(row = 0, column = 0, columnspan = 30, ipadx = 10, ipady = 20, sticky = W)
        #Variavel da comparação da resposta
        Teste = tkinter.StringVar()
        #Alternativa A
        ItemA = tkinter.StringVar()
        ItemA = Itens[random*4]
        #Alternativa A Buttom
        A = tkinter.Radiobutton(Jogo, text = ItemA, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"),foreground = "white", variable = Teste, value = "A", command = Resposta)
        A.grid(row = 1, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa B
        ItemB = tkinter.StringVar()
        ItemB = Itens[random*4+1]
        #Alternativa B Buttom
        B = tkinter.Radiobutton(Jogo, text = ItemB, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "B", command = Resposta)
        B.grid(row = 2, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa C
        ItemC = tkinter.StringVar()
        ItemC = Itens[random*4+2]
        #Alternativa C Buttom
        C = tkinter.Radiobutton(Jogo, text = ItemC, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "C", command = Resposta)
        C.grid(row = 3, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa D
        ItemD = tkinter.StringVar()
        ItemD = Itens[random*4+3]
        #Alternativa D Buttom
        D = tkinter.Radiobutton(Jogo, text = ItemD, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "D", command = Resposta)
        D.grid(row = 4, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Linha vazia Label
        Vazio = Label(text = " ", background = "#002240", font = ("High tower text", 15, "bold"), foreground = "white")
        Vazio.grid(row = 5, column = 0, columnspan = 30, ipadx = 3, ipady = 3, sticky = W)
        #Ajudas Label
        Ajudas = Label(text = "Ajudas", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Ajudas.grid(row = 6, column = 0, columnspan = 3, ipadx = 3, ipady = 3, sticky = W)
        #Pular1 Buttom
        if(Pu1 == 1):
            Pular = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P1)
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Pular2 Buttom
        if(Pu2 == 1):
            Pular1 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P2)
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        else:
            Pular1 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        #Pullar3 Buttom
        if(Pu3 == 1):
            Pular2 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P3)
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular2 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Cartas Buttom
        if(Cards == 1):
            Cartas = tkinter.Button(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda1)
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Cartas = Label(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Professor Buttom
        if(Teacher == 1):
            Professor = tkinter.Button(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda2)
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        else:
            Professor = Label(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        #Engenheiros Buttom
        if(Alunos == 1):
            Engenheiros = tkinter.Button(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda3)
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Engenheiros = Label(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Premios Buttom
        Premios = Label(text = "Prêmios", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Premios.grid(row = 6, column = 4,  ipadx = 3, ipady = 3, sticky = W)
        #Perder Label
        Perder = Label(text = "Perder", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder.grid(row = 7, column = 4, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Perder Valor
        ValorP = tkinter.StringVar()
        ValorP = Lose[z]
        Perder1 = Label(text = ValorP, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder1.grid(row = 7, column = 5, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Parar Buttom
        Parar = tkinter.Button(Jogo, text = "Parar", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Desistir)
        Parar.grid(row = 8, column = 4, ipadx = 7, ipady = 5, sticky = W)
        #Parar Valor
        ValorD = tkinter.StringVar()
        ValorD = Stop[z]
        Parar1 = Label(Jogo, text = ValorD, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Parar1.grid(row = 8, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Acertar Label
        Acertar = Label(text = "Acertar",background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar.grid(row = 9, column = 4, ipadx = 5, ipady = 10, pady = 1, sticky = W)
        #Valor
        ValorA = tkinter.StringVar()
        ValorA = Win[z]
        Acertar1 = Label(text = ValorA, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar1.grid(row = 9, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Logo do jogo Imagem
        Logo = PhotoImage(file = "C:/Users/Marcos/Documents/trabalho programação/Jogo do Milhão/Show.png")
        Marca = Label(image = Logo,background = "#002240")
        Marca.Logo = Logo
        Marca.grid(row = 5, rowspan = 10, column = 12, columnspan = 50, sticky = SE)
        Jogo.mainloop()
def P3():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards, k, random, Win, Stop, Lose, Perguntas, Itens, Respostas, Teste, Jogo
    TF = messagebox.askyesno("Pular", "Você tem certeza que deseja pular?")
    if(TF == True and Pu3 == 1):
        k = random #Dando valor do random pro K, para o while
        Pu3 -= 1 #Diminuindo a quantidade de Pulares disponivel
        while(k == random): #Para que não se repita a pergunta
            random = randint(x,y)
        Jogo.destroy()
        #Janela Principal do Tkinter.
        Jogo = Tk()
        Jogo.title("Jogo do Milhão")
        Jogo['background'] = "#002240"
        #Perguntas
        Answer = tkinter.StringVar()
        Answer = Perguntas[random]
        #Perguntas Label
        Pergunta = Label(text = Answer, relief = RIDGE, background = "#DD0000", font = ("Viner Hand ITC", 12, "bold"), foreground = "white")
        Pergunta.grid(row = 0, column = 0, columnspan = 30, ipadx = 10, ipady = 20, sticky = W)
        #Variavel da comparação da resposta
        Teste = tkinter.StringVar()
        #Alternativa A
        ItemA = tkinter.StringVar()
        ItemA = Itens[random*4]
        #Alternativa A Buttom
        A = tkinter.Radiobutton(Jogo, text = ItemA, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"),foreground = "white", variable = Teste, value = "A", command = Resposta)
        A.grid(row = 1, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa B
        ItemB = tkinter.StringVar()
        ItemB = Itens[random*4+1]
        #Alternativa B Buttom
        B = tkinter.Radiobutton(Jogo, text = ItemB, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "B", command = Resposta)
        B.grid(row = 2, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa C
        ItemC = tkinter.StringVar()
        ItemC = Itens[random*4+2]
        #Alternativa C Buttom
        C = tkinter.Radiobutton(Jogo, text = ItemC, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "C", command = Resposta)
        C.grid(row = 3, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa D
        ItemD = tkinter.StringVar()
        ItemD = Itens[random*4+3]
        #Alternativa D Buttom
        D = tkinter.Radiobutton(Jogo, text = ItemD, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "D", command = Resposta)
        D.grid(row = 4, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Linha vazia Label
        Vazio = Label(text = " ", background = "#002240", font = ("High tower text", 15, "bold"), foreground = "white")
        Vazio.grid(row = 5, column = 0, columnspan = 30, ipadx = 3, ipady = 3, sticky = W)
        #Ajudas Label
        Ajudas = Label(text = "Ajudas", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Ajudas.grid(row = 6, column = 0, columnspan = 3, ipadx = 3, ipady = 3, sticky = W)
        #Pular1 Buttom
        if(Pu1 == 1):
            Pular = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P1)
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular.grid(row = 7, column = 0, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Pular2 Buttom
        if(Pu2 == 1):
            Pular1 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P2)
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        else:
            Pular1 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular1.grid(row = 8, column = 0, ipadx = 10, ipady = 10, sticky = W)
        #Pullar3 Buttom
        if(Pu3 == 1):
            Pular2 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P3)
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular2 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular2.grid(row = 9, column = 0, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Cartas Buttom
        if(Cards == 1):
            Cartas = tkinter.Button(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda1)
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Cartas = Label(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Professor Buttom
        if(Teacher == 1):
            Professor = tkinter.Button(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda2)
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        else:
            Professor = Label(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        #Engenheiros Buttom
        if(Alunos == 1):
            Engenheiros = tkinter.Button(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda3)
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Engenheiros = Label(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        #Premios Buttom
        Premios = Label(text = "Prêmios", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Premios.grid(row = 6, column = 4,  ipadx = 3, ipady = 3, sticky = W)
        #Perder Label
        Perder = Label(text = "Perder", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder.grid(row = 7, column = 4, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Perder Valor
        ValorP = tkinter.StringVar()
        ValorP = Lose[z]
        Perder1 = Label(text = ValorP, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder1.grid(row = 7, column = 5, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Parar Buttom
        Parar = tkinter.Button(Jogo, text = "Parar", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Desistir)
        Parar.grid(row = 8, column = 4, ipadx = 7, ipady = 5, sticky = W)
        #Parar Valor
        ValorD = tkinter.StringVar()
        ValorD = Stop[z]
        Parar1 = Label(Jogo, text = ValorD, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Parar1.grid(row = 8, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Acertar Label
        Acertar = Label(text = "Acertar",background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar.grid(row = 9, column = 4, ipadx = 5, ipady = 10, pady = 1, sticky = W)
        #Valor
        ValorA = tkinter.StringVar()
        ValorA = Win[z]
        Acertar1 = Label(text = ValorA, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar1.grid(row = 9, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Logo do jogo Imagem
        Logo = PhotoImage(file = "C:/Users/Marcos/Documents/trabalho programação/Jogo do Milhão/Show.png")
        Marca = Label(image = Logo,background = "#002240")
        Marca.Logo = Logo
        Marca.grid(row = 5, rowspan = 10, column = 12, columnspan = 50, sticky = SE)
        Jogo.mainloop()
    #Cartas
def Ajuda1():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards
    TF = messagebox.askyesno("Cartas", "Você tem certeza que deseja usar as cartas?")
    if(TF == True):
        Sorte = randint (0,3)
        Lucky = str(Sorte)
        Retiradas = "Você eliminou " + Lucky + " Cartas!"
        messagebox.showinfo("Cartas", Retiradas)
        Cards -= 1
        if("A" == Respostas[random]): R = Itens[random*4] #Para não retirar a resposta certa
        if("B" == Respostas[random]): R = Itens[random*4+1]
        if("C" == Respostas[random]): R = Itens[random*4+2]
        if("D" == Respostas[random]): R = Itens[random*4+3]
        if(Sorte == 1):
            if(R == Itens[random*4]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1] + "\n"+ Itens[random*4+2]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+1]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1] + "\n"+ Itens[random*4+2]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+2]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1] + "\n"+ Itens[random*4+2]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+3]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1] + "\n"+ Itens[random*4+3]
                messagebox.showinfo("Cartas", R1)
        if(Sorte == 2):
            if(R == Itens[random*4]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+1]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+1]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+2]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4]+ "\n" + Itens[random*4+2]
                messagebox.showinfo("Cartas", R1)
            if(R == Itens[random*4+3]):
                R1 = "Um dentre esses itens está correto:\n" + Itens[random*4+1]+ "\n" + Itens[random*4+3]
                messagebox.showinfo("Cartas", R1)
        if(Sorte == 3):
            R1 = "Que sorte! Este é o item correto! " + R
            messagebox.showinfo("Cartas", R1)
    #Professor
def Ajuda2():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards
    TF = messagebox.askyesno("Professor", "Você tem certeza que deseja pedir ajuda ao Mauricio??")
    if(TF == True and Teacher == 1):
        messagebox.showinfo("Professor", "Peça ajuda ao Mauricio")
        Teacher -= 1
    #Colegas
def Ajuda3():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards
    TF = messagebox.askyesno("Engenheiros da Computação", "Você tem certeza que pedir ajuda aos colegas?")
    if(TF == True and Alunos == 1):
        messagebox.showinfo("Engenheiros da Computação", "Peça ajuda aos seus colegas!")
        Alunos -= 1
    #Comaprar se acertou ou errou
def Resposta():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards, k, random, Win, Stop, Lose, Perguntas, Itens, Respostas, Teste, Jogo
    TF = messagebox.askyesno("Confirmação", "Você tem certeza?")
    if(TF == True and Teste.get() == Respostas[random] and rod == 16):
        messagebox.showinfo("Milionario", "Você ficou milionario que nem seus colegas Jamille e Matheus! Parabéns!!!")
        Jogo.destro()
    if(TF == True and Teste.get() == Respostas[random] and rod <16):
        messagebox.showinfo("Resposta", "Você acertou! Vamos para a próxima pergunta!")
        z += 1
        x += 4
        y += 4
        rod += 1
        Jogo.destroy()
        #Janela Principal do Tkinter.
        Jogo = Tk()
        Jogo.title("Jogo do Milhão")
        Jogo['background'] = "#002240"
        random = randint(x,y) #Random das Perguntas e dos itens, inicialmente 0 a 4 e vai aumenndo para 4 a 8....
        #Perguntas
        Answer = tkinter.StringVar()
        Answer = Perguntas[random]
        #Perguntas Label
        Pergunta = Label(text = Answer, relief = RIDGE, background = "#DD0000", font = ("Viner Hand ITC", 12, "bold"), foreground = "white")
        Pergunta.grid(row = 0, column = 0, columnspan = 30, ipadx = 10, ipady = 20, sticky = W)
        #Variavel da comparação da resposta
        Teste = tkinter.StringVar()
        #Alternativa A
        ItemA = tkinter.StringVar()
        ItemA = Itens[random*4]
        #Alternativa A Buttom
        A = tkinter.Radiobutton(Jogo, text = ItemA, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"),foreground = "white", variable = Teste, value = "A", command = Resposta)
        A.grid(row = 1, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa B
        ItemB = tkinter.StringVar()
        ItemB = Itens[random*4+1]
        #Alternativa B Buttom
        B = tkinter.Radiobutton(Jogo, text = ItemB, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "B", command = Resposta)
        B.grid(row = 2, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa C
        ItemC = tkinter.StringVar()
        ItemC = Itens[random*4+2]
        #Alternativa C Buttom
        C = tkinter.Radiobutton(Jogo, text = ItemC, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "C", command = Resposta)
        C.grid(row = 3, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Alternativa D
        ItemD = tkinter.StringVar()
        ItemD = Itens[random*4+3]
        #Alternativa D Buttom
        D = tkinter.Radiobutton(Jogo, text = ItemD, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "D", command = Resposta)
        D.grid(row = 4, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Linha vazia Label
        Vazio = Label(text = " ", background = "#002240", font = ("High tower text", 15, "bold"), foreground = "white")
        Vazio.grid(row = 5, column = 0, columnspan = 30, ipadx = 3, ipady = 3, sticky = W)
        #Ajudas Label
        Ajudas = Label(text = "Ajudas", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Ajudas.grid(row = 6, column = 0, columnspan = 3, ipadx = 3, ipady = 3, sticky = W)
        #Pular1 Buttom
        if(Pu1 == 1):
            Pular = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P1)
            Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular.grid(row = 7, column = 0, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Pular2 Buttom
        if(Pu2 == 1):
            Pular1 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P2)
            Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
        else:
            Pular1 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular1.grid(row = 8, column = 0, ipadx = 10, ipady = 10, sticky = W)
        #Pullar3 Buttom
        if(Pu3 == 1):
            Pular2 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P3)
            Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Pular2 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Pular2.grid(row = 9, column = 0, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Cartas Buttom
        if(Cards == 1):
            Cartas = tkinter.Button(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda1)
            Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Cartas = Label(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Cartas.grid(row = 7, column = 1, ipadx = 10, ipady = 10, pady = 1, sticky = W)
        #Professor Buttom
        if(Teacher == 1):
            Professor = tkinter.Button(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda2)
            Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
        else:
            Professor = Label(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Professor.grid(row = 8, column = 1, ipadx = 10, ipady = 10, sticky = W)
        #Engenheiros Buttom
        if(Alunos == 1):
            Engenheiros = tkinter.Button(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda3)
            Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
        else:
            Engenheiros = Label(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
            Engenheiros.grid(row = 9, column = 1, ipadx = 10, ipady = 10, padx = 1, pady = 1, sticky = W)
        #Premios Buttom
        Premios = Label(text = "Prêmios", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
        Premios.grid(row = 6, column = 4,  ipadx = 3, ipady = 3, sticky = W)
        #Perder Label
        Perder = Label(text = "Perder", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder.grid(row = 7, column = 4, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Perder Valor
        ValorP = tkinter.StringVar()
        ValorP = Lose[z]
        Perder1 = Label(text = ValorP, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Perder1.grid(row = 7, column = 5, ipadx = 12, ipady = 10, pady = 1, sticky = W)
        #Parar Buttom
        Parar = tkinter.Button(Jogo, text = "Parar", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Desistir)
        Parar.grid(row = 8, column = 4, ipadx = 7, ipady = 5, sticky = W)
        #Parar Valor
        ValorD = tkinter.StringVar()
        ValorD = Stop[z]
        Parar1 = Label(Jogo, text = ValorD, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Parar1.grid(row = 8, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Acertar Label
        Acertar = Label(text = "Acertar",background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar.grid(row = 9, column = 4, ipadx = 5, ipady = 10, pady = 1, sticky = W)
        #Valor
        ValorA = tkinter.StringVar()
        ValorA = Win[z]
        Acertar1 = Label(text = ValorA, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
        Acertar1.grid(row = 9, column = 5, ipadx = 7, ipady = 5, sticky = W)
        #Logo do jogo Imagem
        Logo = PhotoImage(file = "C:/Users/Marcos/Documents/trabalho programação/Jogo do Milhão/Show.png")
        Marca = Label(image = Logo,background = "#002240")
        Marca.Logo = Logo
        Marca.grid(row = 5, rowspan = 10, column = 12, columnspan = 50, sticky = SE)
        Jogo.mainloop()
    elif(TF == True and Teste.get() != Respostas[random]):
        Errar = "A respostas certa era a letra "+ Respostas[random] + "! Você perdeu!\n Mas ganhou "+ Lose[z] + "! Saque seu dinheiro no dia 30 de Fevereiro"
        messagebox.showinfo("Resposta", Errar)
        Jogo.destroy()
    #Desistir
def Desistir():
    global x, y, z, rod, Pu1, Pu2, Pu3, Alunos, Teacher, Cards
    TF = messagebox.askyesno("Confirmação", "Você tem certeza?")
    if(TF == True):
        Fraco = "Você Desistiu!\n Mas ganhou " + Stop[z] + "! Saque seu dinheiro no dia 30 de Feveireiro"
        messagebox.showinfo("Desistência", Fraco)
        Jogo.destroy()
#Janela Principal do Tkinter.
Jogo = Tk()
Jogo.title("Jogo do Milhão")
Jogo['background'] = "#002240"
random = randint(x,y) #Random das Perguntas e dos itens, inicialmente 0 a 4 e vai aumenndo para 4 a 8....
#Perguntas
Answer = tkinter.StringVar()
Answer = Perguntas[random]
#Perguntas Label
Pergunta = Label(text = Answer, relief = RIDGE, background = "#DD0000", font = ("Viner Hand ITC", 12, "bold"), foreground = "white")
Pergunta.grid(row = 0, column = 0, columnspan = 30, ipadx = 10, ipady = 20, sticky = W)
#Variavel da comparação da resposta
Teste = tkinter.StringVar()
#Alternativa A
ItemA = tkinter.StringVar()
ItemA = Itens[random*4]
#Alternativa A Buttom
A = tkinter.Radiobutton(Jogo, text = ItemA, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"),foreground = "white", variable = Teste, value = "A", command = Resposta)
A.grid(row = 1, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
#Alternativa B
ItemB = tkinter.StringVar()
ItemB = Itens[random*4+1]
#Alternativa B Buttom
B = tkinter.Radiobutton(Jogo, text = ItemB, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "B", command = Resposta)
B.grid(row = 2, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
#Alternativa C
ItemC = tkinter.StringVar()
ItemC = Itens[random*4+2]
#Alternativa C Buttom
C = tkinter.Radiobutton(Jogo, text = ItemC, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "C", command = Resposta)
C.grid(row = 3, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
#Alternativa D
ItemD = tkinter.StringVar()
ItemD = Itens[random*4+3]
#Alternativa D Buttom
D = tkinter.Radiobutton(Jogo, text = ItemD, background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", variable = Teste, value = "D", command = Resposta)
D.grid(row = 4, column = 0, columnspan = 30, ipadx = 10, ipady = 10, pady = 1, sticky = W)
#Linha vazia Label
Vazio = Label(text = " ", background = "#002240", font = ("High tower text", 15, "bold"), foreground = "white")
Vazio.grid(row = 5, column = 0, columnspan = 30, ipadx = 3, ipady = 3, sticky = W)
#Ajudas Label
Ajudas = Label(text = "Ajudas", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
Ajudas.grid(row = 6, column = 0, columnspan = 3, ipadx = 3, ipady = 3, sticky = W)
#Pular1 Buttom
if(Pu1 == 1):
    Pular = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P1)
    Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
else:
    Pular = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Pular.grid(row = 7, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
#Pular2 Buttom
if(Pu2 == 1):
    Pular1 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P2)
    Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
else:
    Pular1 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Pular1.grid(row = 8, column = 0, ipadx = 5, ipady = 5, sticky = W)
#Pullar3 Buttom
if(Pu3 == 1):
    Pular2 = tkinter.Button(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = P3)
    Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
else:
    Pular2 = Label(Jogo, text = "Pular", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Pular2.grid(row = 9, column = 0, ipadx = 5, ipady = 5, pady = 1, sticky = W)
#Cartas Buttom
if(Cards == 1):
    Cartas = tkinter.Button(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda1)
    Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
else:
    Cartas = Label(Jogo, text = "Cartas", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Cartas.grid(row = 7, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
#Professor Buttom
if(Teacher == 1):
    Professor = tkinter.Button(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda2)
    Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
else:
    Professor = Label(Jogo, text = "Professor", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Professor.grid(row = 8, column = 1, ipadx = 5, ipady = 5, sticky = W)
#Engenheiros Buttom
if(Alunos == 1):
    Engenheiros = tkinter.Button(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Ajuda3)
    Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, pady = 1, sticky = W)
else:
    Engenheiros = Label(Jogo, text = "Engenheiros", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
    Engenheiros.grid(row = 9, column = 1, ipadx = 5, ipady = 5, padx= 1, pady = 1, sticky = W)
#Premios Buttom
Premios = Label(text = "Prêmios", background = "#002240", font = ("Viner Hand ITC", 15, "bold"), foreground = "white")
Premios.grid(row = 6, column = 4,  ipadx = 3, ipady = 3, sticky = W)
#Perder Label
Perder = Label(text = "Perder", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
Perder.grid(row = 7, column = 4, ipadx = 12, ipady = 10, pady = 1, sticky = W)
#Perder Valor
ValorP = tkinter.StringVar()
ValorP = Lose[z]
Perder1 = Label(text = ValorP, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
Perder1.grid(row = 7, column = 5, ipadx = 12, ipady = 10, pady = 1, sticky = W)
#Parar Buttom
Parar = tkinter.Button(Jogo, text = "Parar", background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white", command = Desistir)
Parar.grid(row = 8, column = 4, ipadx = 7, ipady = 5, sticky = W)
#Parar Valor
ValorD = tkinter.StringVar()
ValorD = Stop[z]
Parar1 = Label(Jogo, text = ValorD, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
Parar1.grid(row = 8, column = 5, ipadx = 7, ipady = 5, sticky = W)
#Acertar Label
Acertar = Label(text = "Acertar",background = "#DD0000", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
Acertar.grid(row = 9, column = 4, ipadx = 5, ipady = 10, pady = 1, sticky = W)
#Valor
ValorA = tkinter.StringVar()
ValorA = Win[z]
Acertar1 = Label(text = ValorA, background = "#002240", font = ("Viner Hand ITC", 10, "bold"), foreground = "white")
Acertar1.grid(row = 9, column = 5, ipadx = 7, ipady = 5, sticky = W)
#Logo do jogo Imagem
Marca = Label(image = Logo,background = "#002240")
Marca.Logo = Logo
Marca.grid(row = 5, rowspan = 10, column = 12, columnspan = 50, sticky = SE)
Jogo.mainloop()
