inventory_alice = {
    "sword": {
        "category": "weapon",
        "rarity": "rare",
        "quantity": 1,
        "value": 500
    },
    "potion": {
        "category": "consumable",
        "rarity": "common",
        "quantity": 5,
        "value": 50
    },
    "shield": {
        "category": "armor",
        "rarity": "uncommon",
        "quantity": 1,
        "value": 200
    }
}
print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")
for item, data in inventory_alice.items():
    value = data['quantity'] * data['value']
    print(
        f"{item} ({data['category']}, {data['rarity']}): {data['quantity']}x"
        f" @ {data['value']} gold each = {value} gold")
total_value = 0
total_items = 0
for data in inventory_alice.values():
    total_value += data['value'] * data['quantity']
    total_items += data["quantity"]

print(f"\nInventory value: {total_value} gold")
print(f"Item count: {total_items} items")
categories = {}

for data in inventory_alice.values():
    category = data.get("category")
    quantity = data.get("quantity")

    if category in categories:
        categories[category] += quantity
    else:
        categories[category] = quantity

print("Categories:", end=" ")

i = 0
for cat, qty in categories.items():
    if i > 0:
        print(", ", end="")
    print(f"{cat}({qty})", end="")
    i += 1

print()
print("=== Transaction: Alice gives Bob 2 potions ===")
inventory_alice['potion'].update({'quantity': 3})
inventory_bob = {
    "potion": {
        "category": "consumable",
        "rarity": "common",
        "quantity": 2,
        "value": 50
    }
}
print("Transaction successful!\n")
print("=== Updated Inventories ===")
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
# me falta el magic ring
