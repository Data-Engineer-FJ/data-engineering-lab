#!/bin/bash

# =====================================
# Crear versión del proyecto
# =====================================

if [ -z "$1" ]; then
  echo "❌ Debes indicar el nombre de la versión"
  echo "Ejemplo:"
  echo "./scripts/create_release.sh v1_initial_structure"
  exit 1
fi

VERSION_NAME=$1

PROJECT_DIR=$(pwd)

RELEASE_DIR="$PROJECT_DIR/project_releases"

mkdir -p $RELEASE_DIR

RELEASE_PATH="$RELEASE_DIR/$VERSION_NAME"

echo "📦 Creando release: $VERSION_NAME"

mkdir -p $RELEASE_PATH

rsync -av \
--exclude 'project_releases' \
--exclude '.git' \
--exclude '__pycache__' \
./ $RELEASE_PATH

echo "✅ Release creada en:"
echo "$RELEASE_PATH"
