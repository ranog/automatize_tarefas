#!/usr/bin/env python

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
