inventory_alice = {
    "sword": {
        "category": "weapon",
        "strange": "rare",
        "quantity": 1,
        "value": 500
    },
    "potion": {
        "category": "consumable",
        "strange": "common",
        "quantity": 5,
        "value": 50
    },
    "shield": {
        "category": "armor",
        "strange": "uncommon",
        "quantity": 1,
        "value": 200
    }
}
print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")
for item, data in inventory_alice.items():
    value = data['quantity'] * data['value']
    print(
        f"{item} ({data['category']}, {data['strange']}): {data['quantity']}x"
        f" @ {data['value']} gold each = {value} gold")
total_value = 0
total_items = 0
# falta las categories
for data in inventory_alice.values():
    total_value += data['value'] * data['quantity']
    total_items += data["quantity"]

print(f"\nInventory value: {total_value} gold")
print(f"Item count: {total_items} items")
# falta las categories
print("=== Transaction : Alice gives Bob 2 potions ===")
inventory_alice['potion'].update({'quantity': 3})
inventory_bob = {
    "potion": {
        "category": "consumable",
        "strange": "common",
        "quantity": 2,
        "value": 50
    }
}
print("Transaction succesful\n")
print("=== Updated Inventory ===")
print(f"Alice potions: {inventory_alice['potion'].get('quantity')}")
print(f"Bob potions: {inventory_bob['potion'].get('quantity')}\n")
print("=== Inventory Analytics ===")
update_value = 0
update_items = 0
for data in inventory_alice.values():
    update_value += data['value'] * data['quantity']
    update_items += data["quantity"]
print(f"Most valuable player: Alice ({update_value} gold)")
print(f"Most items: Alice ({update_items} items)")
