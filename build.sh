#!/bin/bash

# Script pour générer le site Hugo pour Cloudflare Pages

echo "🔨 Génération du site Hugo..."
hugo --minify

if [ $? -eq 0 ]; then
    echo "✅ Site généré avec succès dans le dossier 'public/'"
    echo ""
    echo "📦 Prochaines étapes pour déployer sur Cloudflare Pages:"
    echo "   1. Allez sur https://dash.cloudflare.com/"
    echo "   2. Workers & Pages > Create application > Pages > Upload assets"
    echo "   3. Sélectionnez tous les fichiers du dossier 'public/'"
    echo "   4. Cliquez sur 'Save and Deploy'"
    echo ""
    echo "📁 Les fichiers sont prêts dans: $(pwd)/public/"
else
    echo "❌ Erreur lors de la génération"
    exit 1
fi

