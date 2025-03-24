
## ce fichier il va vous permettre de savoir si vous avez bien installé les librairies nécessaires pour utiliser DirectML avec PyTorch notament avec votre GPU (AMD)


import torch # type: ignore
import torch_directml # type: ignore

# Sélectionner le GPU DirectML
device = torch_directml.device()

# Créer un tenseur sur le GPU
x = torch.randn(3, 3).to(device)
y = torch.randn(3, 3).to(device)

# Effectuer une addition sur le GPU
result = x + y

print("Tenseur X :", x)
print("Tenseur Y :", y)
print("Résultat X + Y :", result)
print("Le calcul a bien été fait sur :", device)


