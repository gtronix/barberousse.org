#!/usr/bin/env python3
"""
Script pour générer les favicons à partir du logo barberousse.png
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("❌ PIL/Pillow n'est pas installé.")
    print("Installez-le avec: pip install Pillow")
    sys.exit(1)

# Chemins
logo_path = Path("content/barberousse.png")
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

# Vérifier que le logo existe
if not logo_path.exists():
    print(f"❌ Logo introuvable: {logo_path}")
    sys.exit(1)

print(f"📸 Chargement du logo: {logo_path}")
try:
    logo = Image.open(logo_path)
    # Convertir en RGBA si nécessaire
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')
    
    # Tailles nécessaires pour les favicons
    sizes = {
        'favicon.ico': [(16, 16), (32, 32), (48, 48)],
        'favicon-16x16.png': (16, 16),
        'favicon-32x32.png': (32, 32),
        'apple-touch-icon.png': (180, 180),
        'android-chrome-192x192.png': (192, 192),
        'android-chrome-512x512.png': (512, 512),
    }
    
    print("🔨 Génération des favicons...")
    
    # Générer les fichiers PNG individuels
    for filename, size in sizes.items():
        if filename == 'favicon.ico':
            continue  # On gère l'ICO séparément
        
        if isinstance(size, tuple):
            resized = logo.resize(size, Image.Resampling.LANCZOS)
            output_path = static_dir / filename
            resized.save(output_path, 'PNG')
            print(f"  ✅ {filename} ({size[0]}x{size[1]})")
    
    # Générer le favicon.ico avec plusieurs tailles
    ico_sizes = sizes['favicon.ico']
    ico_images = []
    for size in ico_sizes:
        resized = logo.resize(size, Image.Resampling.LANCZOS)
        ico_images.append(resized)
    
    ico_path = static_dir / 'favicon.ico'
    ico_images[0].save(ico_path, format='ICO', sizes=[(s[0], s[1]) for s in ico_sizes])
    print(f"  ✅ favicon.ico (multi-taille)")
    
    print("\n✅ Tous les favicons ont été générés dans le dossier 'static/'")
    print("\n📝 N'oubliez pas de créer/mettre à jour le fichier static/site.webmanifest")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    sys.exit(1)

