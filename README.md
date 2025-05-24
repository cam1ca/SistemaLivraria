# SistemaLivraria
Trabalho em desenvolvimento da disciplina de programação II
Aqui vou compartilhar os requisitos do trabalho:

Versão 1,
Uma livraria solicitou um software para cadastro de seus produtos (livros).
Durante os processos iniciais de projeto foram levantados os seguintes requisitos para
o software:
Requisito 1: O cadastro dos produtos precisa guardar as seguintes informações:
● Titulo, Código, Editora, Área, Ano, Valor, Quantidade em Estoque.

Requisito 2: Listar todos os livros que foram cadastrados e suas informações. O
seguinte exemplo foi dado:
>>>>> Cod#0301
Titulo/Editora: Compiladores/Pearson
Categoria: Computação
Ano: 2016
Valor: R$ 85,00
Estoque: 125 unidades
Valor total em estoque: R$ 10625,00

Requisito 3: Algumas formas de busca e filtragem de livros conforme suas informações:
● Busca pelo nome do livro.
● Informar quais livros tem preço menor que um valor.
● Apresentar livros de uma categoria específica.
● Buscar livros com valor de estoque maior que o indicado pelo usuário.

Requisito 4: Uma interface de usuário onde seja possível selecionar as ações
disponíveis. O sistema deve permitir que sejam executadas múltiplas ações. O seguinte
exemplo foi dado:
1 – Cadastrar novo livro
2 – Listar livros
3 – Buscar livros por nome
4 – Buscar livros por categoria
5 – Buscar livros por preço
6 – Busca por quantidade em estoque
7 – Valor total no estoque
0 – Encerrar atividades

Versão 2,
Requisito 2.1: O cliente deseja que seja implementada uma funcionalidade para
carregar os livros cadastrados através de um arquivo txt (nova opção 8 - carregar
estoque).
Requisito 2.2: Outra solicitação do cliente é que todas as modificações feitas através do
sistema sejam guardadas novamente no arquivo txt. Tal ação deve ocorrer através de
uma opção no menu (Opção 9 - Atualizar arquivo de estoque). Ao encerrar o sistema
(Opção 0 - Encerrar atividades) o usuário deve ser indagado se quer atualizar o arquivo.

Versão 3,
O dono da livraria informou que cada filial tem seu próprio estoque, sendo
assim gostaria que pudesse verificar de forma separada a situação individual de algum
dos estoques quando fosse necessário.
Requisito 3.1: Criar uma nova funcionalidade para criar filial. A filial deve ter as
seguintes informações:
● Código (valor numérico), Nome da filial, Endereço da filial, Contato da filial, Livros em estoque.

Requisito 3.2: Os arquivos de texto usados para carregar/guardar as informações das
filiais e livros é feito da seguinte forma:
#FL01,Barra Sul,Diário de Noticias 80,3221-6369
3426,compiladores,2012,computação,pearson,R$135.50,50
2631,sistemas digitais,2017,computação,liber,R$99.90,30
9680,senhor dos aneis: a sociedade do anel,2005,fantasia,harper,R$35.00,120

Requisito 3.3: É necessário poder acessar de forma separada o estoque de cada filial,
mostrando todos os livros que a mesma possui em estoque. Essa nova funcionalidade
deve ser chamada de “Listagem de estoque”. Também deve ser informado o valor total
em livros no estoque escolhido.

Requisito 3.4: As buscas já implementadas devem ser feitas individualmente em cada
filial, ou seja, em algum momento da busca é necessário informar o número da filial
onde vai ser feita a busca.
