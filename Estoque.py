import json
from time import sleep


def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo)
    print("Estoque salvo com sucesso.")


def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def exibir_menu():
    print('-=' * 30)
    print('''
        <<<<<<<<<<<<<<<<<<<< - MENU - >>>>>>>>>>>>>>>>>>>>
        [ 1 ] - ADICIONAR PRODUTO
        [ 2 ] - REMOVER PRODUTO
        [ 3 ] - ATUALIZAR QUANTIDADE
        [ 4 ] - MOSTRAR PRODUTOS
        [ 5 ] - CONSULTAR PREÇO TOTAL DO ESTOQUE
        [ 6 ] - CONSULTAR PRODUTO MAIS CARO E MAIS BARATO
        [ 7 ] - CONSULTAR QUANTIDADE TOTAL DE PRODUTOS
        [ 8 ] - LISTAR PRODUTOS COM ESTOQUE BAIXO
        [ 9 ] - SAIR
        <<<<<<<<<<<<<<<<<<<< -------- >>>>>>>>>>>>>>>>>>>>''')


def adicionar_produto(estoque):
    while True:
        nome = str(input('Nome do produto (ou 999 para sair): ')).strip().upper()
        if nome == '999':
            break
        preco = float(input('Preço do produto: '))
        quantidade = int(input('Quantidade em estoque: '))
        estoque.append([nome, preco, quantidade])
        salvar_estoque(estoque)
        print(f'{quantidade} unidade(s) de {nome} a R$ {preco:.2f} adicionadas ao estoque.')


def remover_produto(estoque):
    nome = str(input('Nome do produto a remover: ')).strip().upper()
    estoque[:] = [item for item in estoque if item[0] != nome]
    salvar_estoque(estoque)
    print(f'Produto {nome} removido do estoque.')


def atualizar_quantidade(estoque):
    nome = str(input('Nome do produto para atualizar: ')).strip().upper()
    for item in estoque:
        if item[0] == nome:
            item[2] = int(input('Nova quantidade: '))
            salvar_estoque(estoque)
            print(f'Estoque de {nome} atualizado para {item[2]} unidade(s)')
            return
    print(f'Produto {nome} não encontrado.')


def mostrar_produtos(estoque):
    print('\nEstoque Atual:')
    for i, (nome, preco, quantidade) in enumerate(estoque):
        print(f'{i + 1}. {nome} - R$ {preco:.2f} - {quantidade} unidade(s)')
    print()


def preco_total_estoque(estoque):
    total = sum(item[1] * item[2] for item in estoque)
    print(f'Preço total do estoque: R$ {total:.2f}')


def produto_mais_caro_barato(estoque):
    if not estoque:
        print('O estoque está vazio.')
        return
    mais_caro = max(estoque, key=lambda x: x[1])
    mais_barato = min(estoque, key=lambda x: x[1])
    print(f'Produto mais caro: {mais_caro} - R$ {mais_caro[1]:.2f}')
    print(f'Produto mais barato: {mais_barato} - R$ {mais_barato[1]:.2f}')


def quantidade_total(estoque):
    total = sum(item[2] for item in estoque)
    print(f'Quantidade total de produtos no estoque é de {total}')


def listar_estoque_baixo(estoque, limite=30):
    print('\nProdutos com estoque baixo: ')
    for nome, preco, quantidade in estoque:
        if quantidade < limite:
            print(f'{nome} - {quantidade} unidade(s)')
    print()


def main():
    estoque = carregar_estoque()  # <<< ALTERAÇÃO >>>
    while True:
        exibir_menu()
        opcao = input('Digite uma opção: ').strip()
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            remover_produto(estoque)
        elif opcao == '3':
            atualizar_quantidade(estoque)
        elif opcao == '4':
            mostrar_produtos(estoque)
        elif opcao == '5':
            preco_total_estoque(estoque)
        elif opcao == '6':
            produto_mais_caro_barato(estoque)
        elif opcao == '7':
            quantidade_total(estoque)
        elif opcao == '8':
            listar_estoque_baixo(estoque)
        elif opcao == '9':
            print('Saindo...')
            sleep(1)
            print('VOLTE SEMPRE!')
            break  # <<< ALTERAÇÃO >>>
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
