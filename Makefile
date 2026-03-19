# ==========================================
# DATA ENGINEERING LAB - PRO VERSION
# ==========================================

CLI=./de-cli

.PHONY: help init reset rebuild \
        generate-data preview-data clean-data \
        bronze silver gold medallion dag \
        bootstrap-pipelines remove-pipelines \
        generate-diagram generate-medallion-diagram generate-dag \
        create backup release version backup-full \
        tree clean


# ==========================================
# HELP
# ==========================================

help:
	@echo ""
	@echo "🚀 DATA ENGINEERING LAB COMMANDS"
	@echo ""
	@echo "ENVIRONMENT"
	@echo " make init                  -> Setup environment"
	@echo " make reset                 -> Clean project (FULL reset)"
	@echo " make rebuild               -> Reset + Init + Run pipeline"
	@echo ""
	@echo "DATA"
	@echo " make generate-data         -> Generate test datasets"
	@echo " make preview-data          -> Preview CSV data"
	@echo " make clean-data            -> Remove datasets"
	@echo ""
	@echo "PIPELINE"
	@echo " make bronze                -> Run Bronze layer"
	@echo " make silver                -> Run Silver (parallel)"
	@echo " make gold                  -> Run Gold (parallel)"
	@echo " make medallion             -> Run full pipeline"
	@echo " make dag                   -> Run DAG pipeline (dependency aware)"
	@echo ""
	@echo "PIPELINE STRUCTURE"
	@echo " make bootstrap-pipelines   -> Create pipeline structure"
	@echo " make remove-pipelines      -> Remove pipelines"
	@echo ""
	@echo "DIAGRAMS"
	@echo " make generate-dag          -> Generate DAG diagram"
	@echo ""
	@echo "VERSIONING"
	@echo " make version               -> Save project snapshot"
	@echo ""
	@echo "UTILS"
	@echo " make tree                  -> Show structure"
	@echo " make clean                 -> Clean temp files"
	@echo ""


# ==========================================
# ENVIRONMENT
# ==========================================

init:
	@echo "🚀 Initializing environment..."
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt

	mkdir -p data/bronze data/silver data/gold
	mkdir -p docs/diagrams docs/screenshots
	mkdir -p versions

	@echo "✅ Environment ready"


reset:
	@echo "🧹 FULL reset..."

	rm -rf data
	rm -rf venv
	rm -rf __pycache__
	rm -rf .pytest_cache

	rm -rf src/pipelines/bronze
	rm -rf src/pipelines/silver
	rm -rf src/pipelines/gold

	find . -name "*.pyc" -delete

	@echo "✅ Project cleaned"


rebuild: reset init
	@echo "🚀 Rebuild completed"


# ==========================================
# DATA
# ==========================================

generate-data:
	@echo "📊 Generating datasets..."
	PYTHONPATH=. python scripts/generate_data.py


preview-data:
	@echo "📊 Preview data..."
	csvlook data/bronze/customers.csv || true


clean-data:
	rm -f data/bronze/*.csv


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
	@echo "🚀 Full pipeline..."
	$(MAKE) bronze
	$(MAKE) silver
	$(MAKE) gold


dag:
	@echo "🚀 DAG execution..."
	PYTHONPATH=. python scripts/run_dag.py


# ==========================================
# PIPELINE STRUCTURE
# ==========================================

bootstrap-pipelines:
	@echo "🏗 Creating pipelines..."
	PYTHONPATH=. python scripts/bootstrap_pipelines.py


remove-pipelines:
	@echo "🧹 Removing pipelines..."
	rm -rf src/pipelines/bronze src/pipelines/silver src/pipelines/gold


# ==========================================
# DIAGRAMS
# ==========================================

generate-dag:
	@echo "📊 Generating DAG diagram..."
	PYTHONPATH=. python scripts/generate_dag_diagram.py


# ==========================================
# VERSIONING (🔥 IMPORTANTE)
# ==========================================

version:
	@echo "📦 Creating project snapshot..."
	mkdir -p versions
	tar --exclude='venv' --exclude='__pycache__' --exclude='versions' \
	    -czf versions/project_$(shell date +%Y%m%d_%H%M%S).tar.gz .
	@echo "✅ Snapshot saved in /versions"


# ==========================================
# UTILS
# ==========================================

tree:
	tree -L 2 || ls


clean:
	rm -rf __pycache__ .pytest_cache
	find . -name "*.pyc" -delete