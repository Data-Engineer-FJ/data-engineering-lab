# ==========================================
# DATA ENGINEERING LAB - PRO VERSION 🚀
# ==========================================

CLI=./de-cli
PYTHON=PYTHONPATH=. python

.PHONY: help init reset rebuild \
        generate-data preview preview-bronze preview-silver preview-gold \
        clean-data \
        bronze silver gold medallion dag \
        bootstrap-pipelines remove-pipelines clean-pipelines \
        generate-dag \
        version backup-full \
        tree clean


# ==========================================
# HELP
# ==========================================

help:
	@echo ""
	@echo "🚀 DATA ENGINEERING LAB COMMANDS"
	@echo ""
	@echo "ENVIRONMENT"
	@echo " make init              -> Setup environment"
	@echo " make reset             -> Clean data (safe reset)"
	@echo " make rebuild           -> Reset + Init"
	@echo ""
	@echo "DATA"
	@echo " make generate-data     -> Generate test datasets"
	@echo " make preview           -> Preview ALL pipeline data"
	@echo " make preview-bronze    -> Preview Bronze"
	@echo " make preview-silver    -> Preview Silver"
	@echo " make preview-gold      -> Preview Gold"
	@echo ""
	@echo "PIPELINE"
	@echo " make bronze            -> Run Bronze layer"
	@echo " make silver            -> Run Silver layer"
	@echo " make gold              -> Run Gold layer"
	@echo " make medallion         -> Run full pipeline"
	@echo " make dag               -> Run DAG pipeline"
	@echo ""
	@echo "PIPELINE STRUCTURE"
	@echo " make bootstrap-pipelines -> Create pipeline structure"
	@echo " make clean-pipelines     -> Remove pipeline files (keep folders)"
	@echo ""
	@echo "DIAGRAMS"
	@echo " make generate-dag      -> Generate DAG diagram"
	@echo ""
	@echo "VERSIONING"
	@echo " make version           -> Save project snapshot"
	@echo ""
	@echo "UTILS"
	@echo " make tree              -> Show structure"
	@echo " make clean             -> Clean temp files"
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
	@echo "🧹 Safe reset (data only)..."

	# Clean data only
	rm -f data/bronze/*.csv
	rm -f data/silver/*.csv
	rm -f data/gold/*.csv

	# Cache
	rm -rf __pycache__ .pytest_cache
	find . -name "*.pyc" -delete

	@echo "✅ Data cleaned (pipelines preserved)"


rebuild: reset init
	@echo "🚀 Rebuild completed"


# ==========================================
# DATA
# ==========================================

generate-data:
	@echo "📊 Generating datasets..."
	$(PYTHON) scripts/generate_data.py
	@echo "✅ Data generated in /data/bronze"


clean-data:
	@echo "🧹 Cleaning Bronze data..."
	rm -f data/bronze/*.csv


# ==========================================
# PREVIEW (🔥 NUEVO)
# ==========================================

preview:
	@echo "📊 FULL PIPELINE PREVIEW"

	@echo "\n🥉 BRONZE"
	@csvlook data/bronze/customers.csv | head -n 5 || true
	@csvlook data/bronze/products.csv | head -n 5 || true

	@echo "\n🥈 SILVER"
	@csvlook data/silver/customers_clean.csv | head -n 5 || true
	@csvlook data/silver/products_clean.csv | head -n 5 || true

	@echo "\n🥇 GOLD"
	@csvlook data/gold/revenue_by_country.csv | head -n 5 || true


preview-bronze:
	@echo "🥉 BRONZE DATA"
	@csvlook data/bronze/customers.csv | head -n 10 || true


preview-silver:
	@echo "🥈 SILVER DATA"
	@csvlook data/silver/customers_clean.csv | head -n 10 || true


preview-gold:
	@echo "🥇 GOLD DATA"
	@csvlook data/gold/revenue_by_country.csv | head -n 10 || true


# ==========================================
# PIPELINE
# ==========================================

bronze:
	@echo "🥉 Bronze Layer..."
	$(PYTHON) scripts/run_bronze.py


silver:
	@echo "🥈 Silver Layer..."
	$(PYTHON) scripts/run_silver.py


gold:
	@echo "🥇 Gold Layer..."
	$(PYTHON) scripts/run_gold.py


medallion:
	@echo "🚀 Full pipeline..."
	$(MAKE) bronze
	$(MAKE) silver
	$(MAKE) gold


dag:
	@echo "🚀 DAG execution..."
	$(PYTHON) scripts/run_dag.py


# ==========================================
# PIPELINE STRUCTURE
# ==========================================

bootstrap-pipelines:
	@echo "🏗 Creating pipelines..."
	$(PYTHON) scripts/bootstrap_pipelines.py


clean-pipelines:
	@echo "🧹 Cleaning pipeline files (keeping structure)..."
	rm -f src/pipelines/bronze/*.py
	rm -f src/pipelines/silver/*.py
	rm -f src/pipelines/gold/*.py


# ==========================================
# DIAGRAMS
# ==========================================

generate-dag:
	@echo "📊 Generating DAG diagram..."
	$(PYTHON) scripts/generate_dag_diagram.py


# ==========================================
# VERSIONING
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