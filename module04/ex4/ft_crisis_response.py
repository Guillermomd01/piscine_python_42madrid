print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
try:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    with open("lost_archive.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
print("STATUS: Crisis handled, system stable\n")

try:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    with open("classified_vault.txt", "w") as file:
        file.write("Helooo")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
print("STATUS: Crisis handled, security maintained\n")

try:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt", "r") as file:
        content = file.read()
        print(f"SUCCESS: Archive recovered - ``{content}''")
except (FileNotFoundError, PermissionError):
    print("Ocurred a problem with this file. Sorry...")
print("STATUS: Normal operations resumed\n")
print("All crisis scenarios handled successfully. Archives secure.")
