arquivo = open('ranking.txt', 'r')
ranking = arquivo.readlines()

nome = input("Digite um nome ")

for line in arquivo:
    if(nome==line):
        print("Já Existe!")
        ranking.append(nome+"\n")

arquivo = open('ranking.txt', 'w')
arquivo.writelines(ranking)
arquivo.close()

arquivo = open('ranking.txt','r')

for line in arquivo:
    print(line)

arquivo.close()