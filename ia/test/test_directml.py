
## ce fichier il va vous permettre de savoir si vous avez bien installé les librairies nécessaires pour utiliser DirectML avec PyTorch notament avec votre GPU (AMD)


import torch # type: ignore
import torch_directml # type: ignore

# Sélectionner le GPU DirectML
device = torch_directml.device()
print("Device DirectML :", device)

# Créer un tenseur sur le GPU
x = torch.randn(3, 3).to(device)
y = torch.randn(3, 3).to(device)

# Effectuer une addition sur le GPU
result = x + y

print("Tenseur X :", x)
print("Tenseur Y :", y)
print("Résultat X + Y :", result)
print("Le calcul a bien été fait sur :", device)



# import numpy as np
# import matplotlib.pyplot as plt

# # Définition de la grille de 256 points
# d1, d2 = np.meshgrid(np.arange(256), np.arange(256))

# # Définition de la fonction de Dirac
# def delta(r):
#     return np.where(np.abs(r) < 1e-6, 1, 0)

# # Définition de l'image 2D
# image = np.random.rand(256, 256)

# print(image)
# plt.imshow(image, cmap='gray')
# plt.show()

# # Calcul de la projection avant
# sinogramme = np.sum(image * delta(np.sqrt((d1 - 128)**2 + (d2 - 128)**2)), axis=(0, 1))

# print(sinogramme)

