#!/bin/bash

# ======================================
# Backup completo del proyecto
# ======================================

PROJECT_DIR=$(pwd)

PROJECT_NAME=$(basename "$PROJECT_DIR")

BACKUP_DIR="$PROJECT_DIR/project_versions"

mkdir -p $BACKUP_DIR

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

BACKUP_FILE="$BACKUP_DIR/${PROJECT_NAME}_v$TIMESTAMP.tar.gz"

echo "📦 Creando backup del proyecto..."

tar -czf $BACKUP_FILE --exclude="$BACKUP_DIR" .

echo "✅ Backup creado en:"
echo "$BACKUP_FILE"
