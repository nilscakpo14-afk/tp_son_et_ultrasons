# TP — Sons et ultrasons

## Objectifs

Etude des ondes sonores et ultrasonores: détermination de la vitesse du son

## 1. Vitesse d'un front d'onde sonore

La vitesse $$v_g$$ de propagation du front d'onde est déterminée à partir de mesures différentielles de distance et de temps :

$$
v_g = \frac{\Delta l}{\Delta t}
$$

Plusieurs couples \((\Delta l,\Delta t)\) sont utilisés afin d'obtenir une estimation expérimentale de la vitesse.

La valeur obtenue est comparée à une valeur théorique de la vitesse du son :

$$
v_{\mathrm{th}} = 340.29\ \mathrm{m\,s^{-1}}
$$

## 2. Vitesse de phase d'une onde ultrasonore

### Onde progressive

L'émetteur ultrasonore fonctionne à une fréquence voisine de :

$$
\nu \approx 40\ \mathrm{kHz}
$$

La longueur d'onde est déterminée expérimentalement en repérant plusieurs positions pour lesquelles les signaux sont en phase :

$$
\lambda = \frac{X_2-X_1}{N}
$$

La vitesse de phase est ensuite calculée avec :

$$
v_p = \lambda \nu
$$

Les incertitudes sur les positions et sur la fréquence sont prises en compte dans l'estimation de l'incertitude sur la vitesse.

## 3. Superposition d'ondes progressives

Deux émetteurs ultrasonores sont placés face à face.

Lorsque les deux ondes contra-propageantes possèdent la même fréquence, leur superposition produit une **onde stationnaire**.

La distance entre deux maxima successifs correspond à :

$$
\frac{\lambda}{2}
$$

La mesure de plusieurs maxima permet donc de déterminer expérimentalement la longueur d'onde :

$$
\lambda = 2\frac{X_2-X_1}{N}
$$

puis la vitesse de propagation :

$$
v_p = \lambda \nu
$$

## 4. Phénomène de battement

Lorsque deux ondes de fréquences proches $$\nu_1$$ et $$\nu_2\$$ sont superposées, on observe un phénomène de battement.

La fréquence théorique du battement est :

$$
\nu_{\mathrm{bat}} = |\nu_1-\nu_2|
$$

Cette valeur est comparée à la fréquence de battement mesurée expérimentalement à l'oscilloscope.

## 5. Effet Doppler

La dernière partie du TP étudie la variation de la fréquence reçue lorsqu'il existe un mouvement relatif entre l'émetteur et le récepteur.

Pour de faibles vitesses, la fréquence reçue peut être décrite par une relation affine :

$$
f = a f_R + b
$$

où :

- $$f_R$$ est la fréquence de rotation de la source ;
- $$f$$ est la fréquence ultrasonore reçue ;
- $$a$$ est le coefficient directeur de la régression ;
- $$b$$ est l'ordonnée à l'origine.

Le coefficient directeur est déterminé à partir des données expérimentales :

$$
a =
\frac{\mathrm{Cov}(f_R,f)}
{\mathrm{Var}(f_R)}
$$

et :

$$
b = \bar f-a\bar f_R
$$

La vitesse de propagation des ultrasons est finalement obtenue grâce à :

$$
v_p =
\frac{2\pi r f_0}{a}
$$

avec :

$$
f_0 \simeq b
$$

et $$r$$ le rayon de rotation de la source.

L'incertitude sur le coefficient directeur est également calculée à partir des résidus de la régression afin d'estimer l'incertitude sur $$v_p$$.

## Fichiers

- `tp_son_et_ultrasons_code.py` : traitement des données expérimentales et calcul des différentes grandeurs physiques.
- `functions.py` : fonctions utilisées pour le calcul des incertitudes et des écarts relatifs.

## Auteur

**Nils CAKPO**  
Licence 3 Physique