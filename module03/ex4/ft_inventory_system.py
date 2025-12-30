data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3
                },
            "total_value": 1875,
            "item_count": 6
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3
                },
            "total_value": 4125,
            "item_count": 12
        }
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common"
            },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare"
            },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common"
            },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary"
            },
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"}
    }
}
print("=== Player Inventory System ===")

players = data.get("players")
catalog = data.get("catalog")

print("\n=== Alice's Inventory ===")

alice_items = players.get("alice").get("items")

total_value = 0
total_items = 0
categories = {}

for item, qty in alice_items.items():
    item_data = catalog.get(item)
    value = item_data.get("value") * qty
    total_value += value
    total_items += qty

    category = item_data.get("type")
    if category in categories:
        categories[category] += qty
    else:
        categories[category] = qty

    print(
        f"{item} ({category}, {item_data.get('rarity')}): "
        f"{qty}x @ {item_data.get('value')} gold each = {value} gold"
    )

print(f"Inventory value: {total_value} gold")
print(f"Item count: {total_items} items")

print("Categories:", end=" ")
i = 0
for cat, qty in categories.items():
    if i > 0:
        print(", ", end="")
    print(f"{cat}({qty})", end="")
    i += 1
print()

print("\n=== Transaction: Alice gives Bob 2 health_byte ===")

if alice_items.get("health_byte", 0) >= 2:
    alice_items["health_byte"] -= 2

    bob_items = players.get("bob").get("items")
    if "health_byte" in bob_items:
        bob_items["health_byte"] += 2
    else:
        bob_items["health_byte"] = 2

    print("Transaction successful!")
else:
    print("Transaction failed!")

print("\n=== Updated Inventories ===")
print(f"Alice health_byte: {alice_items.get('health_byte')}")
print(f"Bob health_byte: {players.get('bob').get('items').get('health_byte')}")

print("\n=== Inventory Analytics ===")

most_value_player = ""
max_value = 0

most_items_player = ""
max_items = 0

for player, pdata in players.items():
    if pdata.get("total_value") > max_value:
        max_value = pdata.get("total_value")
        most_value_player = player

    if pdata.get("item_count") > max_items:
        max_items = pdata.get("item_count")
        most_items_player = player

print(
    f"Most valuable player: {most_value_player.capitalize()} ({max_value} "
    f"gold)")
print(f"Most items: {most_items_player.capitalize()} ({max_items} items)")

rarity_rank = {
    "common": 1,
    "uncommon": 2,
    "rare": 3,
    "legendary": 4
}

max_rarity = 0
rarest_items = []

for item, info in catalog.items():
    rank = rarity_rank.get(info.get("rarity"))
    if rank > max_rarity:
        max_rarity = rank
        rarest_items = [item]
    elif rank == max_rarity:
        rarest_items.append(item)

print("Rarest items:", ", ".join(rarest_items))
