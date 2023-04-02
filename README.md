# ShootColor

ShootColor est une bibliothèque 
Python pour ajouter des effets de 
couleur à votre code. Elle vous 
permet de facilement ajouter des 
couleurs, des effets animés et des 
effets de fondu à vos applications.

# Installation

Pour installer ShootColor, 
vous pouvez utiliser la commande suivante :

`pip install ShootColor`

# Utilisation

Une fois installé, vous pouvez 
utiliser ShootColor en important 
la classe Colors du module shootcolor. 
Voici un exemple de code qui utilise
la classe Colors pour ajouter une couleur 
de texte rouge clignotante :

```python
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.blink(colors.red(text))
print(colored_text)
```

# Licence

ShootColor est distribué sous la licence MIT. 
Consultez le fichier `LICENSE` pour plus d'informations.
