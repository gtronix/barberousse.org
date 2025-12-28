# Guide de déploiement sur Cloudflare Pages

## Méthode 1 : Upload direct de fichiers statiques (Recommandé pour débuter)

### Étape 1 : Générer les fichiers statiques

Assurez-vous que votre site Hugo est construit et à jour :

```bash
hugo --minify
```

Les fichiers statiques seront générés dans le dossier `public/`.

### Étape 2 : Uploader sur Cloudflare Pages

1. **Connectez-vous à Cloudflare Dashboard**
   - Allez sur https://dash.cloudflare.com/
   - Connectez-vous à votre compte

2. **Accédez à Pages**
   - Dans le menu de gauche, cliquez sur **"Workers & Pages"**
   - Cliquez sur **"Create application"**
   - Sélectionnez **"Pages"**
   - Cliquez sur **"Upload assets"**

3. **Uploader les fichiers**
   - Sélectionnez **tous les fichiers** du dossier `public/`
   - **Important** : Uploader uniquement le contenu du dossier `public/`, pas le dossier lui-même
   - Attendez que l'upload soit terminé

4. **Configurer le projet**
   - **Project name** : `barberousse-website` (ou le nom de votre choix)
   - **Production branch** : `main` (ou laissez par défaut)
   - Cliquez sur **"Save and Deploy"**

5. **Configurer le domaine personnalisé** (optionnel)
   - Une fois déployé, allez dans **"Custom domains"**
   - Ajoutez `barberousse.org` si vous avez configuré le DNS chez Cloudflare

### ⚠️ Important pour les mises à jour

Pour chaque mise à jour de votre site :
1. Régénérez les fichiers statiques : `hugo --minify`
2. Re-uploader le contenu du dossier `public/` sur Cloudflare Pages

---

## Méthode 2 : Déploiement automatique via Git (Recommandé pour production)

Cette méthode permet un déploiement automatique à chaque push Git.

### Étape 1 : Préparer le dépôt Git

Créez un fichier `.gitignore` à la racine si ce n'est pas déjà fait :

```gitignore
# Hugo
/public/
/resources/_gen/
.hugo_build.lock

# OS
.DS_Store
Thumbs.db
```

### Étape 2 : Créer un dépôt Git

```bash
git init
git add .
git commit -m "Initial commit"
```

Poussez vers GitHub, GitLab ou Bitbucket.

### Étape 3 : Configurer Cloudflare Pages

1. **Connectez-vous à Cloudflare Dashboard**
   - Allez sur **"Workers & Pages"** > **"Create application"** > **"Pages"**
   - Cliquez sur **"Connect to Git"**

2. **Connecter votre dépôt**
   - Autorisez Cloudflare à accéder à votre dépôt Git
   - Sélectionnez votre dépôt

3. **Configurer le build**
   - **Project name** : `barberousse-website`
   - **Production branch** : `main` (ou `master`)
   - **Build command** : `hugo --minify`
   - **Build output directory** : `public`
   - **Hugo version** : Sélectionnez la version appropriée (ou laissez Cloudflare détecter)

4. **Variables d'environnement** (si nécessaire)
   - Si vous utilisez des variables d'environnement, ajoutez-les ici

5. **Sauvegarder et déployer**
   - Cliquez sur **"Save and Deploy"**

### Configuration automatique

Cloudflare Pages détectera automatiquement Hugo et configurera le build. À chaque push sur votre branche principale, le site sera automatiquement reconstruit et redéployé.

---

## Configuration DNS (pour barberousse.org)

Si votre domaine est géré par Cloudflare :

1. Allez dans **"Custom domains"** de votre projet Pages
2. Ajoutez `barberousse.org` et `www.barberousse.org`
3. Cloudflare configurera automatiquement les enregistrements DNS

Si votre domaine n'est pas chez Cloudflare :

1. Ajoutez le domaine dans Cloudflare Pages
2. Cloudflare vous donnera un enregistrement CNAME à ajouter chez votre registrar DNS
3. Pointez `barberousse.org` vers le CNAME fourni

---

## Commandes utiles

### Générer le site localement
```bash
hugo server
```

### Générer pour production
```bash
hugo --minify
```

### Vérifier les fichiers générés
```bash
ls -la public/
```

---

## Notes importantes

- Le dossier `public/` contient tous les fichiers statiques à déployer
- Ne déployez jamais les fichiers sources (hugo.toml, themes/, content/, etc.) directement
- Cloudflare Pages offre un CDN global gratuit
- Les déploiements sont instantanés et gratuits
- SSL/TLS est automatiquement configuré

