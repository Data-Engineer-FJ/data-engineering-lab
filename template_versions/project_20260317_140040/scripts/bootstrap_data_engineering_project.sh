#!/bin/bash
# =========================
# Backup automático del script
# =========================

VERSION=$(date +"%Y%m%d_%H%M%S")

BACKUP_DIR="template_versions"

mkdir -p $BACKUP_DIR

SCRIPT_NAME=$(basename "$0")

cp "$SCRIPT_NAME" "$BACKUP_DIR/${SCRIPT_NAME}_v$VERSION"

# =====================================
# Data Engineering Project Bootstrap
# Professional Medallion Architecture
# =====================================

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "❌ Debes indicar el nombre del proyecto"
  echo "Uso: ./bootstrap_data_engineering_project.sh nombre_proyecto"
  exit 1
fi

echo "🚀 Creando proyecto: $PROJECT_NAME"

# =========================
# Crear estructura
# =========================

mkdir -p $PROJECT_NAME/{airflow/dags,configs,data/{bronze,silver,gold},docker,docs,logs,notebooks,scripts}

mkdir -p $PROJECT_NAME/data/{bronze/personas,silver/personas,gold/personas}

mkdir -p $PROJECT_NAME/src/{config,utils}

mkdir -p $PROJECT_NAME/src/pipelines/{ingestion,bronze,silver,gold}

mkdir -p $PROJECT_NAME/tests

# =========================
# Archivos base
# =========================

touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/Makefile
touch $PROJECT_NAME/.env

touch $PROJECT_NAME/docker/docker-compose.yml
touch $PROJECT_NAME/docker/Dockerfile

touch $PROJECT_NAME/airflow/dags/medallion_pipeline.py

touch $PROJECT_NAME/notebooks/exploration.ipynb

touch $PROJECT_NAME/src/config/settings.py

touch $PROJECT_NAME/src/utils/helpers.py
touch $PROJECT_NAME/src/utils/spark_utils.py

touch $PROJECT_NAME/tests/test_pipeline.py

# =========================
# Crear paquetes Python
# =========================

touch $PROJECT_NAME/src/__init__.py
touch $PROJECT_NAME/src/config/__init__.py
touch $PROJECT_NAME/src/utils/__init__.py
touch $PROJECT_NAME/src/pipelines/__init__.py

# =========================
# Dataset ejemplo
# =========================

cat <<EOL > $PROJECT_NAME/data/bronze/personas/personas.csv
id,nombre,edad,ciudad
1,Ana,30,Lima
2,Carlos,40,Arequipa
3,Lucia,25,Cusco
EOL

# =========================
# Script para correr pipeline
# =========================

cat <<EOL > $PROJECT_NAME/scripts/run_pipeline.sh
#!/bin/bash

echo "🚀 Ejecutando pipelines medallion"

python src/pipelines/bronze/ingest_personas.py
python src/pipelines/silver/transform_personas.py
python src/pipelines/gold/aggregate_personas.py
EOL

chmod +x $PROJECT_NAME/scripts/run_pipeline.sh

# =========================
# .gitignore
# =========================

cat <<EOL > $PROJECT_NAME/.gitignore
__pycache__/
*.pyc
.env
.venv
data/silver
data/gold
notebooks/.ipynb_checkpoints
logs/
.DS_Store
EOL

# =========================
# requirements
# =========================

cat <<EOL > $PROJECT_NAME/requirements.txt
pyspark
pandas
apache-airflow
delta-spark
EOL

# =========================
# README inicial
# =========================

cat <<EOL > $PROJECT_NAME/README.md
# $PROJECT_NAME

Proyecto de Data Engineering basado en arquitectura **Medallion**.

## Arquitectura

Bronze → Silver → Gold

### Bronze
Datos crudos

### Silver
Datos transformados

### Gold
Datos agregados para analytics

## Tecnologías

- Python
- PySpark
- Apache Airflow
- Docker
EOL

# =========================
# Inicializar git
# =========================

cd $PROJECT_NAME

git init > /dev/null 2>&1

echo "✅ Proyecto creado correctamente"
echo ""
echo "📂 Estructura generada:"
tree 2>/dev/null || ls -R
