print("=== Achievement Tracker System ===\n")
alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {
    'level_10', 'treasure_hunter', 'boss_slayer',
    'speed_demon', 'perfectionist'}
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}\n")

print("=== Achievement Analytics ===")
unique_achievements = alice.union(bob, charlie)
print(f"All unique achievements: {unique_achievements}")
print(f"Total unique achievements: {len(unique_achievements)}\n")

common_achievements = alice.intersection(bob, charlie)
print(f"Common to all players: {common_achievements}")
alice_unique = alice.difference(bob, charlie)
bob_unique = bob.difference(alice, charlie)
charlie_unique = charlie.difference(alice, bob)
rare_achievements = bob_unique.union(charlie_unique)
print(f"Rare achievements (1 player: {rare_achievements}\n")

print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
