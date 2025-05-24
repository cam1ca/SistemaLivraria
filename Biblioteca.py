
Filiais = [] 
Biblioteca = []

arquivo_atual = None #acessada nas funções 8 e 9 referentes ao arquivo.txt

#Definindo o que é uma filial (p depois adicionar a ação de cadastro)

class Filial:
    def __init__(self, codigoFilial, nomeFilial, enderecoFilial, contatoFilial):
        self.codigoFilial = codigoFilial
        self.nomeFilial = nomeFilial
        self.enderecoFilial = enderecoFilial
        self.contatoFilial = contatoFilial
        self.livros = [] 

    def __str__(self):
        return f'Código: #{self.codigoFilial} Nome: {self.nomeFilial} Endereco: {self.enderecoFilial} Contato: {self.contatoFilial}'

#FUNÇÕES REFERENTE AS FILIAIS
def cadastrarFilial():
    print('Cadastro de uma nova filial')
    codigoFilial = input('Código da Filial: ')
    nomeFilial = input('Nome da filial: ')
    enderecoFilial = input('Endereco da Filial: ')
    contatoFilial = input('Contato da Filial: ')

    nova_filial = Filial(codigoFilial, nomeFilial, enderecoFilial, contatoFilial)
    Filiais.append(nova_filial)
    print('Filial cadastrada com sucesso!')
    print(novaFilial)            

#--------------------------------------------------------------------------
class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return (f' Título: {self.titulo} \n Código: {self.codigo} \n Editora: {self.editora} \n Área: {self.area} \n Ano: {self.ano} \n Valor: R${self.valor} \n Estoque: {self.estoque}\n')
   
Livro1 = Livro('Co-intelligence: Living and Working with AI', 154869,'Independente', 'Inteligencia Artificial', 2024, 90, 7 )
Livro2 = Livro('Supremacy: AI, ChatGPT, and the Race that Will Change the World', 514878,'Bloomberg', 'Inteligencia Artificial', 2024, 75, 18)
Livro3 = Livro('Nexus: A Brief History of Information Networks from the Stone Age to AI', 457895, 'HarperCollins', 'Tecnologia e Ética', 2024, 81, 2)
Livro4 = Livro('The Corporate Life Cycle: Business, Investment, and Management Implications', 458791, 'Wiley', 'Negócios e Tecnologia', 2024, 101, 4)
Livro5 = Livro('Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence', 985476, ' Yale University Press', 'Filosofia da Tecnologia', 2021, 60, 1)

Biblioteca.append(Livro1)
Biblioteca.append(Livro2)
Biblioteca.append(Livro3)
Biblioteca.append(Livro4)
Biblioteca.append(Livro5)


#FUNÇÕES REFERENTES A LIVROS:
def cadastrar_livro():
    print("Cadastro de Novo Livro")
    titulo = input("Título: ")
    codigo = int(input("Código: "))
    editora = input("Editora: ")
    area = input("Área: ")
    ano = int(input("Ano: "))
    valor = float(input("Valor (R$): "))
    estoque = int(input("Estoque: "))

    novo_livro = Livro(titulo, codigo, editora, area, ano, valor, estoque)
    Biblioteca.append(novo_livro)
    print("\nLivro cadastrado com sucesso!\n")
    print(novo_livro)
  
def carregar_estoque_arquivo():
    global arquivo_atual
    ArquivoTxt = input('Digite aqui o nome do arquivo .txt que deseja salvar livros: ')
    arquivo_atual = ArquivoTxt 

    try:
        with open(ArquivoTxt, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) == 7:
                    titulo,codigo,editora,area,ano,valor,estoque = dados
                    codigo = int(codigo)
                    ano = int(ano)
                    valor = float(valor)
                    estoque = int(estoque)

                    novo_livro = Livro(titulo, codigo, editora, area, ano, valor, estoque)
                    Biblioteca.append(novo_livro)

            print("Livros carregados com sucesso a partir do arquivo!")

    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")

def carregarBiblioteca_Arquivo():
    if arquivo_atual is None:
            print('Nenhum arquivo foi carregado ainda. Carregue-o primeiro na opção 8 da interface.')
    else:
        try:
            with open(arquivo_atual, 'w', encoding='utf-8') as arquivo:
                for livro in Biblioteca:
                    linha = f"{livro.titulo},{livro.codigo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.estoque}\n"
                    arquivo.write(linha)

                print(f"Livros salvos com sucesso no arquivo {arquivo_atual}!")

        except Exception as e:
            print(f"Ocorreu um erro ao salvar o arquivo: {e}")


#Interface do Usuário --------------------------------------------------------
x=1

while (x!=0):
    print()
    print('1. Buscar livro pelo nome')
    print('2. Filtragem por preço')
    print('3. Seleção da categoria de interesse')
    print('4. Quantidade de livros em estoque')
    print('5. Cadastrar novo livro')
    print('6. Listar todos os livros da Biblioteca')
    print('7. Valor total em estoque')
    print('8. Carregar do arquivo .txt')
    print('9. Atualizar arquivo .txt')
    print()
    
    x = int(input('Escolha uma das opções acima ou digite 0 para sair do sistema: '))

    if (x==1):
        nomeLivro = input('Digite o nome do livro: ').strip().lower()
        resultadoBuscaNome = [livro for livro in Biblioteca if livro.titulo.strip().lower() == nomeLivro]
       
        if resultadoBuscaNome:
            print('Item Disponivel.')
            print()
            for livro in resultadoBuscaNome:
                print(f' Título: {livro.titulo} \n Código: {livro.codigo} \n Editora: {livro.editora} \n Área: {livro.area} \n Ano: {livro.ano} \n Valor: R${livro.valor} \n Estoque: {livro.estoque}\n')

        else:
            print()
            print('Item indisponível. Você será redirecionado ao menu de opções.')
            print()

    elif (x==2):
        orcamento = float(input('Digite o valor em que deseja filtrar: '))
        livrosNoOrcamento = [livro for livro in Biblioteca if livro.valor <= orcamento]
       
        if livrosNoOrcamento:
            print('Livros disponíveis dentro do valor delimitado:')
            print()
            for livro in livrosNoOrcamento:
                print(f' Título: {livro.titulo} \n Código: {livro.codigo} \n Editora: {livro.editora} \n Área: {livro.area} \n Ano: {livro.ano} \n Valor: R${livro.valor} \n Estoque: {livro.estoque}\n')
           
        else:
            print('Não há itens disponíveis')

    elif (x==3):
        categoria = input('Digite a categoria de interesse: ').strip().lower()
        livrosNaCategoria = [livro for livro in Biblioteca if livro.area.strip().lower() == categoria]
       
        if livrosNaCategoria:
            for livro in livrosNaCategoria:
                print('Livros disponíveis na categoria desejada: ')
                print()
                print(f' Título: {livro.titulo} \n Código: {livro.codigo} \n Editora: {livro.editora} \n Área: {livro.area} \n Ano: {livro.ano} \n Valor: R${livro.valor} \n Estoque: {livro.estoque}\n')
                print()
        else:
            print('Não há livros disponíveis nesta categoria.')
           
    elif (x==4):
        estoque = int(input('Digite a quantidade em estoque que você deseja verificar disponível: '))
        livrosEmEstoque = [livro for livro in Biblioteca if livro.estoque >= estoque]
       
        if livrosEmEstoque:
            for livro in livrosEmEstoque:
                print('Segue abaixo os livros disponíveis dentro da quantidade em estoque desejada')
                print()
                print(f' Título: {livro.titulo} \n Código: {livro.codigo} \n Editora: {livro.editora} \n Área: {livro.area} \n Ano: {livro.ano} \n Valor: R${livro.valor} \n Estoque: {livro.estoque}\n')
                print()
               
        else:
            print('Não há livros disponíveis com essa quantidade em estoque')
   
    elif (x==5):
        cadastrar_livro()
       
    elif (x==6):
        if Biblioteca:
            print("Lista de todos os livros cadastrados:")
            print()
            for livro in Biblioteca:
                print(livro)
                print()
       
    elif (x == 7):
        if Biblioteca:  
            print("Valor total em estoque para cada livro:")
            print()
            for livro in Biblioteca:
                valor_total = livro.valor * livro.estoque
                print(f'{livro}')
                print(f'Valor total em estoque: R${valor_total:.2f}')
                print()  
   
    elif (x==8):
        carregar_estoque_arquivo()
       
    elif (x == 9):
        carregarBiblioteca_Arquivo()
#--------------------------------------------------------------------------