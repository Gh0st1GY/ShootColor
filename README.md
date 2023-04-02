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

`pip install ShootColors==1.0.0`

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

# Documentation

### Importer la classe Colors

Pour utiliser le module ShootColor dans votre code Python, 
vous devez importer la classe Colors depuis le module shootcolor. 
Voici comment procéder :

```
from shootcolor import Colors
```

### Utiliser les couleurs

Une fois que vous avez importé la classe Colors, 
vous pouvez utiliser les différentes couleurs disponibles dans le module. 
Voici un exemple de code qui utilise la couleur rouge pour afficher un texte :

```
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.red(text)
print(colored_text)
```

Vous pouvez également utiliser des combinaisons de couleurs en utilisant 
les méthodes `bg_color` et `fg_color`. 
Par exemple, pour afficher du texte en rouge sur un fond bleu :

```
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.fg_color(colors.red(text)) + colors.bg_color(colors.blue(" "))
print(colored_text)
```

### Ajouter des effets de texte

Le module ShootColor vous permet également d'ajouter des effets de texte à vos couleurs. 
Par exemple, pour ajouter un effet de clignotement à votre texte rouge :

```
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.blink(colors.red(text))
print(colored_text)
```

Vous pouvez également utiliser les méthodes underline, reverse, et dim pour ajouter différents types d'effets à votre texte.

Ajouter des effets de fondu
Le module ShootColor vous permet également d'ajouter des effets de fondu à vos couleurs. Par exemple, pour ajouter un effet de fondu entrant à votre texte rouge :

```
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.fade_in(colors.red(text))
print(colored_text)
```

Vous pouvez également utiliser les méthodes `fade_out`, `fade`, et `rainbow` pour ajouter différents types d'effets de fondu à votre texte.

### Ajouter des effets animés

Le module ShootColor vous permet également d'ajouter des effets animés à votre texte. Par exemple, pour faire défiler votre texte en rouge de gauche à droite :

```
from shootcolor import Colors

colors = Colors()
text = "Hello, world!"
colored_text = colors.scroll_right(colors.red(text))
print(colored_text)
```

Vous pouvez également utiliser les méthodes `scroll_left`, `scroll_up`, et `scroll_down` pour ajouter différents types d'effets animés à votre texte.

# Développeurs

 - Gh0st1GY 

# Voir sur PyPi(https://pypi.org/project/ShootColors/1.0.0/)
