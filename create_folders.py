import os

folders = ['models', 'logs']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
print("Folders created ✅")
