#José Guilherme @Development
#Jogo da Velha 1.0




def adcNaMatriz(Px, Py, simbolo): #Adiciona o simbolo na posição digitada, caso ñ esteja ocupada
    if(Py == "A"):
        z [Px] = simbolo
    if(Py == "B"):
        y [Px] = simbolo
    if(Py == "C"):
        x [Px] = simbolo

def Verificador(px, py, simbolo, jogadas): #Se a posição selecionada estiver vazia, sera adc na Matriz
    if (py == "A" and z[px] == ""):
        print("A")
        jogadas+=1
        adcNaMatriz(px, py, simbolo)
        return True

    elif (py == "B" and y[px] == ""):
        print("B")
        jogadas+=1
        adcNaMatriz(px, py, simbolo)
        return True

    elif (py == "C" and x[px] == ""):
        print("C")
        jogadas+=1
        adcNaMatriz(px, py, simbolo)
        return True

    else: #Se estiver ocupada será enviado um alerta!
        print("Posição já ocupada!")
        return False

def view():
  print ("    0 |  1 | 2   ")
  print ("C   %s | %s | %s " % (x[0],x[1],x[2]))
  print ("   ---+---+---   ")
  print ("B   %s | %s | %s " % (y[0],y[1],y[2]))
  print ("   ---+---+---   ")
  print ("A   %s | %s | %s " % (z[0],z[1],z[2]))

def win(simbolo, winPlayer):
    if(x[0]==simbolo and x[1]==simbolo and x[2]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(y[0]==simbolo and y[1]==simbolo and y[2]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(z[0]==simbolo and z[1]==simbolo and z[2]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(x[0]==simbolo and y[0]==simbolo and z[0]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(x[1]==simbolo and y[1]==simbolo and z[1]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(x[2]==simbolo and y[2]==simbolo and z[2]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(x[0]==simbolo and y[1]==simbolo and z[2]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(x[2]==simbolo and y[1]==simbolo and z[0]==simbolo):
        print("Parabéns",winPlayer,"! Você venceu!!!")
        gravar(winPlayer)
        return False

    elif(jogadas==9):
        print("Deu Velha!!")
        return False

def gravar(player):
    ranking.append(player+"\n")
    arquivo = open('ranking.txt', 'w')
    arquivo.writelines(ranking)
    arquivo.close()

#INÍCIO DO PROGRAMA

while(True): #Raiz do jogo

    arquivo = open('ranking.txt', 'r')
    ranking = arquivo.readlines()

    print("JOGO DA VELHA\n\n")

    x = ["","",""]
    y = ["","",""]
    z= ["","",""]
    jogadas = 0

    nPlayer1 = input("[PLAYER 1] Digite seu nome: ")

    while(True): #Escolher o simbolo
        simbolo1 = input(nPlayer1+", escolha o simbolo: X ou O: ")
        simbolo2 =""
        simbolo1 = simbolo1.upper()

        if(simbolo1=="X" or simbolo1=="O"): #Se o player 1 escolher 'X', automaticamente sera atribuido 'Y' ao player 2
            if(simbolo1 == "X"):
                simbolo2 = "O"
                break
            else:
                simbolo1 = "O"
                simbolo2 = "X"
                break

    nPlayer2 = input("[PLAYER 2] Digite seu nome: ")

    print()
    print(nPlayer1,"=",simbolo1)
    print(nPlayer2,"=",simbolo2)
    print()


    while(True): #Processo do jogo

        while(True):

            while(True):
                try:
                    player1x=int(input("["+nPlayer1+"]"+"Digite a posição 'x' (0, 1 OU 2): "))
                    if(player1x<3):
                        break
                except:
                    print("Favor digitar um número (0, 1 OU 2)")



            while(True):
                player1y=input("["+nPlayer1+"]"+"Digite a posição 'y' (A, B OU C): ")
                player1y = player1y.upper()
                if(player1y=='A' or player1y=='B' or player1y=='C'):
                    break

            if(Verificador(player1x, player1y, simbolo1, jogadas) == True):
                view()
                break

        if(win(simbolo1,nPlayer1)==False):
            break

        while(True):

            while(True):
                try:
                    player2x=int(input("["+nPlayer2+"]"+"Digite a posição 'x' (0, 1 OU 2): "))
                    if(player2x<3):
                        break
                except:
                    print("Favor digitar um número (0, 1 OU 2)")

            while(True):
                player2y=input("["+nPlayer2+"]"+"Digite a posição 'y' (A, B OU C): ")
                player2y = player2y.upper()
                if(player2y=='A' or player2y=='B' or player2y=='C'):
                    break

            if(Verificador(player2x, player2y, simbolo2, jogadas) == True):
                view()
                break

        if(win(simbolo2,nPlayer2)==False):
            break




    decisao=input("Deseja jogar novamente: ")
    decisao= decisao.upper()

    if(decisao=="S"):
        continue

    if(decisao=="N"):
        exit()



view()

#ATUALIZAR PLACAR
#ARQUIVO TXT