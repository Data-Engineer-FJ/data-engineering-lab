# ==========================================
# DATA ENGINEERING LAB - MAKEFILE FINAL
# ==========================================

CLI=./de-cli

# 📦 Versionado
VERSIONS_DIR=template_versions
BACKUP_DIR=~/backups/data-engineering-lab
TIMESTAMP=$(shell date +%Y%m%d_%H%M%S)

.PHONY: help init reset rebuild \
        generate-data preview-data clean-data \
        bronze silver gold medallion \
        bootstrap-pipelines remove-pipelines \
        backup-project safe-run \
        generate-diagram generate-medallion-diagram \
        tree clean

# ==========================================
# HELP
# ==========================================

help:
	@echo ""
	@echo "🚀 DATA ENGINEERING LAB"
	@echo ""
	@echo "ENVIRONMENT"
	@echo " make init                  -> Crear entorno virtual"
	@echo " make reset                 -> Limpiar proyecto"
	@echo " make rebuild               -> Reset + pipeline completo"
	@echo ""
	@echo "DATA"
	@echo " make generate-data         -> Generar datasets"
	@echo " make preview-data          -> Ver datasets"
	@echo ""
	@echo "PIPELINE"
	@echo " make bronze                -> Ejecutar Bronze"
	@echo " make silver                -> Ejecutar Silver"
	@echo " make gold                  -> Ejecutar Gold"
	@echo " make medallion             -> Ejecutar pipeline completo"
	@echo ""
	@echo "PIPELINES STRUCTURE"
	@echo " make bootstrap-pipelines   -> Crear pipelines"
	@echo " make remove-pipelines      -> Eliminar pipelines"
	@echo ""
	@echo "VERSIONING"
	@echo " make backup-project        -> Snapshot completo del proyecto"
	@echo " make safe-run              -> Snapshot + pipeline"
	@echo ""
	@echo "UTILS"
	@echo " make tree                  -> Ver estructura"
	@echo " make clean                 -> Limpiar temporales"
	@echo ""

# ==========================================
# ENVIRONMENT
# ==========================================

init:
	@echo "🚀 Inicializando entorno..."
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt

	mkdir -p data/bronze data/silver data/gold
	mkdir -p docs/diagrams docs/screenshots
	mkdir -p $(VERSIONS_DIR)

	@echo "✅ Entorno listo"


reset:
	@echo "🧹 Limpiando proyecto..."

	rm -rf data/bronze/* data/silver/* data/gold/*
	rm -rf src/pipelines
	rm -rf venv

	rm -rf __pycache__ .pytest_cache
	find . -name "*.pyc" -delete

	@echo "✅ Proyecto limpio"


rebuild: reset init bootstrap-pipelines generate-data medallion
	@echo "🚀 Proyecto reconstruido"


# ==========================================
# DATA
# ==========================================

generate-data:
	@echo "📊 Generating datasets..."
	python scripts/generate_data.py
	@echo "✅ Data generada"


preview-data:
	@echo "📊 Preview datasets"
	csvlook data/bronze/customers.csv || true
	csvlook data/bronze/products.csv || true


clean-data:
	rm -f data/bronze/*.csv
	@echo "✅ Datos eliminados"


# ==========================================
# PIPELINE
# ==========================================

bronze:
	@echo "🥉 Bronze Layer..."
	PYTHONPATH=. python scripts/run_bronze.py


silver:
	@echo "🥈 Silver Layer..."
	PYTHONPATH=. python scripts/run_silver.py


gold:
	@echo "🥇 Gold Layer..."
	PYTHONPATH=. python scripts/run_gold.py


medallion:
	@echo "🚀 Running Medallion Pipeline..."
	$(MAKE) bronze
	$(MAKE) silver
	$(MAKE) gold
	@echo "🎉 Pipeline completado"


# ==========================================
# PIPELINE STRUCTURE
# ==========================================

bootstrap-pipelines:
	@echo "🏗 Creando estructura de pipelines..."
	python scripts/bootstrap_pipelines.py
	@echo "✅ Pipelines creados"


remove-pipelines:
	@echo "🧹 Eliminando pipelines..."
	rm -rf src/pipelines
	@echo "✅ Pipelines eliminados"


# ==========================================
# VERSIONING (FULL PROJECT SNAPSHOT)
# ==========================================

backup-project:
	@echo "📦 Creating project snapshot..."

	mkdir -p $(VERSIONS_DIR)
	mkdir -p $(BACKUP_DIR)

	# Snapshot interno (repo)
	rsync -av \
		--exclude 'venv' \
		--exclude '__pycache__' \
		--exclude '.git' \
		--exclude '$(VERSIONS_DIR)' \
		./ $(VERSIONS_DIR)/project_$(TIMESTAMP)

	# Snapshot externo (PC)
	rsync -av \
		--exclude 'venv' \
		--exclude '__pycache__' \
		--exclude '.git' \
		--exclude '$(VERSIONS_DIR)' \
		./ $(BACKUP_DIR)/project_$(TIMESTAMP)

	@echo "✅ Snapshot creado:"
	@echo "   Repo: $(VERSIONS_DIR)/project_$(TIMESTAMP)"
	@echo "   PC: $(BACKUP_DIR)/project_$(TIMESTAMP)"


# ==========================================
# SAFE EXECUTION
# ==========================================

safe-run:
	@echo "🛡 Running pipeline with snapshot..."
	$(MAKE) backup-project
	$(MAKE) medallion


# ==========================================
# DIAGRAMS
# ==========================================

generate-diagram:
	@echo "📊 Generando diagrama arquitectura..."
	python scripts/generate_architecture_diagram.py


generate-medallion-diagram:
	@echo "📊 Generando diagrama Medallion..."
	python scripts/generate_medallion_architecture.py


# ==========================================
# UTILITIES
# ==========================================

tree:
	tree -L 2


clean:
	rm -rf __pycache__ .pytest_cache
	find . -name "*.pyc" -delete