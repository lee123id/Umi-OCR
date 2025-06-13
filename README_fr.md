<p align="left">
    <span>
        <b>中文</b>
    </span>
    <span> • </span>
    <a href="README_en.md">
        English
    </a>
    <span> • </span>
    <a href="README_ja.md">
        日本語
    </a>
    <span> • </span>
    <span>
        <b>Français</b>
    </span>
</p>

<p align="center">
  <a href="https://github.com/hiroi-sora/Umi-OCR">
    <img width="200" height="128" src="https://tupian.li/images/2022/10/27/icon---256.png" alt="Umi-OCR">
  </a>
</p>

<h1 align="center">Umi-OCR </h1>

<p align="center">
  <a href="https://github.com/hiroi-sora/Umi-OCR/releases/latest">
    <img src="https://img.shields.io/github/v/release/hiroi-sora/Umi-OCR?style=flat-square" alt="Umi-OCR">
  </a>
  <a href="https://github.com/hiroi-sora/Umi-OCR/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/hiroi-sora/Umi-OCR?style=flat-square" alt="LICENSE">
  </a>
  <a href="#téléchargement-releases">
    <img src="https://img.shields.io/github/downloads/hiroi-sora/Umi-OCR/total?style=flat-square" alt="forks">
  </a>
  <a href="https://star-history.com/#hiroi-sora/Umi-OCR">
    <img src="https://img.shields.io/github/stars/hiroi-sora/Umi-OCR?style=flat-square" alt="stars">
  </a>
  <a href="https://github.com/hiroi-sora/Umi-OCR/forks">
    <img src="https://img.shields.io/github/forks/hiroi-sora/Umi-OCR?style=flat-square" alt="forks">
  </a>
  <a href="https://hosted.weblate.org/engage/umi-ocr/">
    <img src="https://hosted.weblate.org/widget/umi-ocr/svg-badge.svg" alt="翻译状态">
  </a>
</p>

<div align="center">
  <h3>
    <a href="#Catalogue">
      Instructions d'utilisation
    </a>
    <span> • </span>
    <a href="#téléchargement-releases">
      Adresse de téléchargement
    </a>
    <span> • </span>
    <a href="CHANGE_LOG.md">
      Mettre à jour le journal
    </a>
    <span> • </span>
    <a href="https://github.com/hiroi-sora/Umi-OCR/issues">
      Soumettre un bug
    </a>
  </h3>
</div>
<br>

<div align="center">
  <strong>Logiciel OCR hors ligne gratuit, open source et en vrac</strong><br>
  <sub>Applicable à Windows7 x64 、Linux x64
</div><br>

- * * gratuit * *: tout le Code de ce projet est open source et entièrement gratuit.
- * * pratique * *: décompresser prêt à l'emploi, fonctionnement hors ligne, aucun réseau requis.
- * * haute efficacité * *: Apportez votre propre moteur OCR hors ligne haute efficacité avec une bibliothèque de reconnaissance de plusieurs langues intégrée.
- * * flexible * *: prend en charge les méthodes d'appel externes telles que la ligne de commande, l'interface http, etc.
- * * fonction * *: capture d'écran OCR / OCR par lot / reconnaissance PDF / Code QR / reconnaissance de formule

<p align="center"><img src="https://tupian.li/images/2023/11/19/65599097ab5f4.png" alt="1-标题-1.png" style="width: 80%;"></p>

![1-标题-2.png](https://tupian.li/images/2023/11/19/6559909fdeeba.png)

## Utiliser le code source

Développeurs assurez - vous de lire [Build Project] (\ Build Project).

## Télécharger les Releases :

- **Lanzou** https://hiroi-sora.lanzoul.com/s/umi-ocr 
- **GitHub** https://github.com/hiroi-sora/Umi-OCR/releases/latest
- **Source Forge** https://sourceforge.net/projects/umi-ocr


<details>
<summary><b>•&nbsp;&nbsp;Scoop Installer</b>（Cliquez pour agrandir）</summary>

[Scoop](https://scoop.sh/) Est un programme d'installation en ligne de commande sous Windows qui facilite la gestion de plusieurs applications. Vous pouvez d'abord installer scoop, puis' Umi - OCR 'en utilisant les instructions suivantes:

- Ajouter un seau 'extras'：
```
scoop bucket add extras
```

- (facultatif 1) installez Umi - OCR (avec votre propre moteur ‘rapid - ocr’, bonne compatibilité)：
```
scoop install extras/umi-ocr
```

-(Option 2) installez Umi - OCR (avec votre propre moteur Paddle - OCR, légèrement plus rapide)：
```
scoop install extras/umi-ocr-paddle
```

-N'installez pas les deux en même temps, les raccourcis peuvent être écrasés. Mais vous pouvez importer [plugin] en plus ( https://github.com/hiroi-sora/Umi-OCR_plugins ), basculez entre les différents moteurs OCR à tout moment.

</details>

## Commencer à utiliser

Le package de publication de logiciels est téléchargé en tant que package de compression.7z ou en tant que package auto - extractible.7z.exe. Le package auto - extractible peut décompresser des fichiers sur un PC sans logiciel de compression installé.

Aucune installation n'est requise pour ce logiciel. Une fois décompressé, appuyez sur 'umi-ocr.exe' pour lancer le programme.

Si vous rencontrez des problèmes, veuillez mentionner [issue] ( https://github.com/hiroi-sora/Umi-OCR/issues ), je vous aiderai autant que possible.

## Langue de l'interface

Interface multilingue prise en charge par Umi - OCR. La première fois que vous ouvrez le logiciel, vous changez automatiquement de langue en suivant les paramètres système de votre ordinateur.

Si vous devez changer de langue manuellement, reportez - vous à l'image suivante, ` paramètres globaux ` → ` langue / language `.

<p align="center"><img src="https://tupian.li/images/2023/11/19/65599c3f9e600.png" alt="1-标题-1.png" style="width: 80%;"></p>

## Tag Page

Umi - OCR V2 se compose d'une série de pages d'étiquettes * * flexibles et utilisables. Vous pouvez ouvrir les pages d'onglets dont vous avez besoin, comme vous le souhaitez.

Le coin supérieur gauche de la barre d'étiquettes peut être commuté * * fenêtre en haut * *. Le coin supérieur droit est capable de * * verrouiller la page d'étiquettes * * Pour éviter de toucher par erreur pour fermer la page d'étiquettes lors d'une utilisation quotidienne.

### Capture d'écran ocr

<p align="center"><img src="https://tupian.li/images/2023/11/19/65599097aba8e.png" alt="2-截图-1.png" style="width: 80%;"></p>

* * screenshot OCR * *: après avoir ouvert cette page, il est possible d'évoquer une capture d'écran avec un raccourci pour reconnaître le texte de l'image.
- barre de prévisualisation de l'image sur le côté gauche pour sélectionner la copie directement avec la souris.
- barre d'enregistrement d'identification à droite, qui permet d'éditer le texte, permettant de sélectionner plusieurs copies d'enregistrements.
- prend également en charge la copie d'images ailleurs, coller dans Umi - OCR pour la reconnaissance.

#### Post - traitement du texte

<p align="center"><img src="https://tupian.li/images/2023/11/19/6559909f3e378.png" alt="2-截图-2.png" style="width: 80%;"></p>

À propos * * post - traitement de texte OCR - schéma d'analyse typographique * *: la typographie et l'ordre des résultats OCR peuvent être triés pour rendre le texte plus lisible et plus utilisable. Schéma prédéfini:

- 'Multi - Colonnes - saut de ligne par segment naturel': convient à la plupart des scénarios, reconnaît automatiquement la disposition Multi - colonnes, saut de ligne par segment naturel.
- ` Multi - Bar - always back Line ': chaque phrase passe à la ligne.
- ` Multi - Bar - pas de saut de ligne ': force toutes les instructions à être fusionnées sur la même ligne.
- ` barre unique - passer à la ligne par segment naturel ` / ` toujours passer à la ligne ` / ` ` pas de passage à la ligne `: similaire à ce qui précède, mais ne fait pas de distinction entre les dispositions à colonnes multiples.
- 'Single Bar - Preserve indentation': convient pour analyser les captures d'écran de code, en conservant l'indentation en tête de ligne et les espaces dans la ligne.

---

### OCR par lots

<p align="center"><img src="https://tupian.li/images/2023/11/19/655990a2511e0.png" alt="3-批量-1.png" style="width: 80%;"></p>

* * OCR par lots * *: Cette page est utilisée pour importer des images locales par lots à des fins de reconnaissance.

- formats supportés: ` JPG, jpe, JPEG, jfif, PNG, webp, BMP, tif, TIFF `.
- format pris en charge pour enregistrer les résultats de reconnaissance: ` txt, jsonl, MD, CSV (Excel) `.
- tout comme screenshot OCR, prend en charge la fonction "post - traitement du texte", Trie la typographie et l'ordre du texte OCR.
- il n'y a pas de limite de quantité, il est possible d'importer des centaines d'images à la fois pour les tâches.
- arrêt / veille automatique après la fin de la tâche de support.
- Si vous souhaitez identifier des images longues ou grandes avec des pixels surdimensionnés, Ajustez: * * paramètres de la page → reconnaissance de texte → limiter la longueur des côtés de l'image → [augmenter la valeur] *.
- possède la fonction spéciale "ignorer la zone".

#### Ignorer la zone

<p align="center"><img src="https://tupian.li/images/2023/11/19/6559911d28be7.png" alt="3-批量-2.png" style="width: 80%;"></p>

À propos de * * post - traitement de texte OCR - ignorer la Zone * *: une fonctionnalité spéciale dans l'OCR par lots pour exclure le texte indésirable dans les images.

- l'éditeur de zone ignorée est accessible dans les paramètres de la colonne de droite de la page de reconnaissance de lot.
- comme dans l'exemple ci - dessus, plusieurs filigranes / logos sont présents en haut et en bas à droite de l'image. Si vous reconnaissez ce type d'image par lots, le filigrane peut interférer avec le résultat de l'identification.
- maintenez le bouton droit enfoncé et dessinez plusieurs cases rectangulaires. Le texte dans ces zones sera ignoré dans la tâche.
- s'il vous plaît essayer de dessiner le cadre rectangulaire un peu plus grand, enveloppant complètement le filigrane à tous les endroits où il peut apparaître.

---

###Identification du document

 <p align="centre"> <image source=" https://github.com/hiroi-sora/Umi-OCR/assets/56373419/fc2266ee-b9b7-4079-8b10-6610e6da6cf5  "alt="" style="largeur: 80%;  "></p>

 ** Identification du document * :
 - Formats pris en charge : `pdf, xps, epub, mobi, fb2, cbz`.
 - OCR des scannés ou extrait du texte original. Peut être exporté en **PDF recherchable à deux couches**.
 - Prise en charge du paramètre ** Zone d'ignorer *, qui peut être utilisé pour exclure le texte du pied d'en-tête.
 - Vous pouvez configurer ** Automatique d'arrêt / d'hibernation ** après la fin de la tâche.

---

### Code 2D

<p align="center"><img src="https://tupian.li/images/2023/11/19/655991268d6b1.png" alt="4-二维码-1.png" style="width: 80%;"></p>

* * Code de balayage * *:

- prendre une capture d'écran / coller / glisser dans l'image locale, lire le Code QR, Code à barres à l'intérieur.
- support d'une figure Multi - Code.
 - Prend en charge 19 protocoles et paramètres tels que ** niveau de correction d'erreur *.

---

###Paramètres globaux

<p align="center"><img src="https://tupian.li/images/2023/11/19/655991252e780.png" alt="5-全局设置-1.png" style="width: 80%;"></p>

* * paramètres globaux * *: les paramètres globaux du logiciel peuvent être ajustés ici. Les fonctions habituelles sont les suivantes:

- ajoutez un raccourci ou définissez l'auto - amorçage de démarrage en un clic.
- changer l'interface * * langue * *. UMI prend en charge les langues comme le chinois traditionnel, l'anglais, le japonais, etc.
- changer d'interface * * Thème * *. UMI a plusieurs thèmes clairs / sombres.
- redimensionner l'interface * * Texte * * et * * police * *.
- changer le plugin OCR.
- * * renderer * *: l'interface logicielle prend en charge le rendu accéléré par carte graphique par défaut. Si l'écran clignote, l'interface utilisateur est désalignée sur votre machine, Ajustez l'interface et l'apparence → le moteur de rendu, essayez de passer à un autre schéma de rendu ou désactivez l'accélération matérielle.

##Appeler l'interface:

- [manuel de ligne de commande] (docs / README - cli.md)
- [manuel de l'interface http] (docs / http / readme.md)

---

## À propos de la structure du projet

### Divers entrepôts：

 - [Entrepôt principal]( https://github.com/hiroi-sora/Umi-OCR  (en anglais) 👈
 - [Bibliothèque de plugins]( https://github.com/hiroi-sora/Umi-OCR_plugins  (en anglais)
 - [Bibliothèque d'exécution Windows]( https://github.com/hiroi-sora/Umi-OCR_runtime_windows  (en anglais)
 - [Bibliothèque d'exécution Linux]( https://github.com/hiroi-sora/Umi-OCR_runtime_linux  (en anglais)

### Structure de l'ingénierie:

Le suffixe ` * ` indique ce que contient cet entrepôt (` entrepôt principal ').

```
Umi-OCR
├─ Umi-OCR.exe
├─ umi-ocr.sh
└─ UmiOCR-data
   ├─ main.py **
   ├─ version.py **
   ├─ qt_res **
   │  └─ Ressources du projet qt, y compris les icônes et le code source qml
   ├─ py_src **
   │  └─ Projet Python source
   ├─ plugins
   │  └─ Plugins
   └─ i18n **
      └─ Traduction de documents
```

Moteurs OCR hors ligne pris en charge:

- [paddleocr - json] ( https://github.com/hiroi-sora/PaddleOCR-json ) et
- [rapidocr - json] ( https://github.com/hiroi-sora/RapidOCR-json ) et

Cadre de l'environnement opérationnel:

- [pystand] ( https://github.com/skywind3000/PyStand ) Version personnalisée

8593; construire un projet

Veuillez sauter à l'entrepôt ci - dessous pour terminer le déploiement de l'environnement de développement / d'exploitation de la plate - forme correspondante.

- [Windows] ( https://github.com/hiroi-sora/Umi-OCR_runtime_windows ) et
- [Linux] ( https://github.com/hiroi-sora/Umi-OCR_runtime_linux ) et

--- 

Traduction localisée du logiciel:

Ce projet utilise la plate - forme weblate pour la collaboration de traduction localisée de l'interface utilisateur. Tout traducteur est le bienvenu pour participer à la traduction, vous pouvez accéder à ce lien [weblate: UMI - OCR] ( https://hosted.weblate.org/engage/umi-ocr/ ), relire en ligne, compléter une langue existante ou en ajouter une nouvelle.

Merci aux traducteurs suivants qui ont contribué au travail de traduction localisé d'Umi - OCR:

| Traducteur                                                                               | 贡献语言                  |
| ------------------------------------------------------------------------------------ | ------------------------- |
| [bob](https://hosted.weblate.org/user/q021)                                          | English, 繁體中文, 日本語 |
| [Qingzheng Gao](https://github.com/QZGao)                                            | English, 繁體中文         |
| [Weng, Chia-Ling](https://hosted.weblate.org/user/ChiaLingWeng)                      | English, 繁體中文         |
| [linzow](https://hosted.weblate.org/user/linzow)                                     | English, 繁體中文         |
| [Marcos i](https://hosted.weblate.org/user/ultramarkorj9)                            | English, Português        |
| [Eric Guo](https://hosted.weblate.org/user/qwedc001)                                 | English                   |
| [steven0081](https://hosted.weblate.org/user/steven0081)                             | English                   |
| [Brandon Cagle](https://hosted.weblate.org/user/random4t4x14)                        | English                   |
| [plum7x](https://hosted.weblate.org/user/plum7x)                                     | 繁體中文                  |
| [hugoalh](https://hosted.weblate.org/user/hugoalh)                                   | 繁體中文                  |
| [Anarkiisto](https://hosted.weblate.org/user/Anarkiisto)                             | 繁體中文                  |
| [ドコモ光](https://hosted.weblate.org/user/umren190402)                              | 日本語                    |
| [杨鹏](https://hosted.weblate.org/user/ypf)                                          | Português                 |
| [Вячеслав Анатольевич Малышев](https://hosted.weblate.org/user/1969)                 | Русский                   |
| [Muhammadyusuf Kurbonov](https://hosted.weblate.org/user/muhammadyusuf.kurbonov2002) | Русский                   |
| [தமிழ்நேரம்](https://hosted.weblate.org/user/TamilNeram/)                                | தமிழ்                       |

En cas d'erreur d'information ou de manque de personnel, veuillez consulter [cette discussion] ( https://github.com/hiroi-sora/Umi-OCR/discussions/449 ) en réponse.

---

## Sponsorisé

Umi - OCR projet principalement par auteur [hiroi - Sora] ( https://github.com/hiroi-sora ), passer du temps libre dans le développement et la maintenance. Si vous aimez ce logiciel, le parrainage est le bienvenu.

- les utilisateurs domestiques peuvent produire de l'électricité par [amour] ( https://afdian.com/a/hiroi-sora ), auteurs sponsorisés.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hiroi-sora/Umi-OCR&type=Date)](https://star-history.com/#hiroi-sora/Umi-OCR&Date)

## [Mettre à jour le journal](CHANGE_LOG.md)