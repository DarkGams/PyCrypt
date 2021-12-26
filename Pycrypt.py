import time 
from hashlib import sha256
from pystyle import Anime, Colors, Colorate, Center, Box
from colorama import Fore, Back, Style

banner = """.______   ____    ____  ______ .______     ____    ____ .______   .___________.
|   _  \  \   \  /   / /      ||   _  \    \   \  /   / |   _  \  |           |
|  |_)  |  \   \/   / |  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`
|   ___/    \_    _/  |  |     |      /      \_    _/   |   ___/      |  |     
|  |          |  |    |  `----.|  |\  \----.   |  |     |  |          |  |     
| _|          |__|     \______|| _| `._____|   |__|     | _|          |__|     
                                                                               """
print((Center.XCenter(Box.DoubleCube(banner))))

senetence_1 = (Fore.GREEN + "\nCe crypteur chiffre en XOR , assez efficace mais facile a décrypter si vous avez la clé")

for char in senetence_1:
	time.sleep(0.1)
	print(char, end='', flush=True)

entree = input("\nFichier a crypter : ")
exit = input("Nom du fichier final : ")
key = input("Entrez la clé : ")
keys = sha256(key.encode('utf-8')).digest()

with open(entree,'rb') as a_entree:
	with open(exit,'wb') as a_exit:
		i = 0
		while a_entree.peek():
			b = ord(a_entree.read(1))
			c = i % len(keys)
			d = bytes([c^keys[c]])
			a_exit.write(d)
			i = i + 1 

sentence_2 = (Fore.GREEN + "Le fichier ",exit," a été crée sur votre repertoire actuel")

for char in sentence_2:
	time.sleep(0.1)
	print(char, end='', flush=True)
