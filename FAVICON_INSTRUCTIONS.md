# Instructions pour générer les favicons

## Option 1 : Utiliser un service en ligne (Recommandé)

1. Allez sur https://realfavicongenerator.net/
2. Uploader le fichier `content/barberousse.png`
3. Configurez les options selon vos préférences
4. Téléchargez le package généré
5. Extrayez les fichiers dans le dossier `static/`

## Option 2 : Utiliser le script Python (nécessite Pillow)

Si vous avez Python et Pillow installés :

```bash
# Installer Pillow
pip3 install Pillow
# ou
python3 -m pip install Pillow

# Générer les favicons
python3 generate_favicons.py
```

## Option 3 : Utiliser ImageMagick

Si vous avez ImageMagick installé :

```bash
cd static
convert ../content/barberousse.png -resize 16x16 favicon-16x16.png
convert ../content/barberousse.png -resize 32x32 favicon-32x32.png
convert ../content/barberousse.png -resize 180x180 apple-touch-icon.png
convert ../content/barberousse.png -resize 192x192 android-chrome-192x192.png
convert ../content/barberousse.png -resize 512x512 android-chrome-512x512.png
convert ../content/barberousse.png -define icon:auto-resize=16,32,48 favicon.ico
```

## Fichiers nécessaires dans static/

Une fois générés, vous devez avoir ces fichiers dans `static/` :
- `favicon.ico` (16x16, 32x32, 48x48)
- `favicon-16x16.png`
- `favicon-32x32.png`
- `apple-touch-icon.png` (180x180)
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`
- `site.webmanifest` (déjà créé)

Le fichier `site.webmanifest` a déjà été créé avec les bonnes informations pour votre site.

