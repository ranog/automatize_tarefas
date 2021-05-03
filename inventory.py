#!/usr/bin/env python

""" Inventário de um jogo de fantasia

Você está criando um videogame de fantasia. A estrutura de dados para
modelar o inventário do jogador será um dicionário em que as chaves são
valores de string que descrevem o item do inventário e o valor será um
inteiro detalhando quantos itens desse tipo o jogador tem. Por exemplo,
o valor de dicionário

    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

quer dizer que o jogador tem 1 corda (rope), 6 tochas (torches), 42
moedas de ouro (gold coins) e assim por diante.

Crie uma função chamada displayInventory() que possa receber qualquer
"inventário" possível e exiba essas informações da seguinte maneira:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

Dica: você pode utilizar um loop for para percorrer todas as chaves de um
dicionário.

# inventory.py
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


    def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
            print(str(v) + ' ' + k)
            item_total += v
        print("Total number of items: " + str(item_total))


    displayInventory(stuff)

Função de "lista para dicionário" para o inventário de jogo de fantasia

Suponha que os despojos de um dragão vencido seja representado como uma
lista de strings como esta:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Crie uma função chamada addToInventory(inventory, addedItems), em que o
parâmetro inventory seja um dicionário representando o inventário do
jogador (como no projeto anterior) e o parâmetro addedItems seja uma
lista como dragonLoot. A função addToInventory() deve retornar um
dicionário que represente o inventário atualizado. Observe que a lista
addedItems pode conter vários itens iguais. Seu código poderá ser
semelhante a:

def addToInventory(inventory, addedItems):
    # seu código deve ser inserido aqui

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

O programa anterior (com sua função displayInventory() do projeto
anterior) apresentará a saída a seguir:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48 """


def addToInventory(inventory, addedItems):
    """ Atualiza o inventário. """
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

    return inventory


def displayInventory(inventory):
    """ Exiba essas informações de um inventário. """
    print("Inventory:")

    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
