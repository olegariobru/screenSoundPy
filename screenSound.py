bandas_cadastradas = []

def menuInicial():
        print("Bem Vindo ao Screen Sound!")
        print("Por gentileza, selecione a opção abaixo:")
        print("1- Cadastrar uma banda")
        print("2- Visualizar as bandas cadastradas")
        print("3- Avaliar uma banda cadastrada")
       # print("4- Exibir a média de avaliação de uma banda")
        #print("5- Sair do programa")


def principal():
    while True:
        menuInicial()
        choice = input("Digite a sua escolha de 1 a 5: \n")
        
        if choice == '1':
            cadastrar_banda()
        elif choice == '2':
            visualizar_bandas()
        elif choice == '3':
            avalia_banda()
        


        elif choice == '5':
            print("Obrigado por usar o Screen Sound. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção de 1 a 5: ")

        continuar = input("Deseja voltar ao menu inicial? (sim ou não):")
        if continuar.lower() != 'sim':
            print("Obrigado por usar o Screen Sound. Até mais!")
            break



def cadastrar_banda():
        nome_banda = input("Digite o nome da banda: ")
        bandas_cadastradas.append(nome_banda)
        print(f"A banda {nome_banda} foi cadastrada com sucesso!")  

def visualizar_bandas():
        if not bandas_cadastradas:
            print("Não temos bandas cadastradas ainda")
        else:
            print("Lista de bandas cadastradas: ")
            for banda in bandas_cadastradas:
                print(banda)

def avalia_banda():
    visualizar_bandas()
    nome_avalia_banda2 = input("Qual a banda que você deseja avaliar?")  

    print(f"Avaliando a banda: {nome_avalia_banda2}")
    nota_banda = input(f"Qual será a nota que você definirá para a banda: {nome_avalia_banda2}? (de 0 a 10)")

    print(f"Você atribuiu a nota: {nota_banda} para a banda: {nome_avalia_banda2}.")

principal()
