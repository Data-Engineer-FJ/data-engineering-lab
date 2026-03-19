#!/bin/bash

echo "🧹 Cleaning project..."

# =========================
# 1. REMOVE UNUSED SCRIPTS
# =========================
echo "🗑 Removing unnecessary scripts..."

rm -f scripts/backup_project.sh
rm -f scripts/bootstrap_data_engineering_project.sh
rm -f scripts/create_release.sh
rm -f scripts/generate_architecture_diagram.py
rm -f scripts/generate_medallion_architecture.py
rm -f scripts/inspect_csv.py
rm -f scripts/reset_pipeline.py
rm -f scripts/run_pipeline.sh

# OPTIONAL
# rm -f scripts/bootstrap_pipelines.py

# =========================
# 2. CLEAN DATA OUTPUTS
# =========================
echo "🧹 Cleaning data folders..."

rm -rf data/bronze/*
rm -rf data/silver/*
rm -rf data/gold/*

# =========================
# 3. CLEAN GENERATED DIAGRAMS
# =========================
echo "🖼 Removing generated diagrams..."

rm -f docs/diagrams/*.png

# =========================
# 4. CLEAN LOGS (if exist)
# =========================
echo "📄 Cleaning logs..."

rm -rf logs/*

# =========================
# 5. CLEAN CACHE
# =========================
echo "⚡ Cleaning cache..."

find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# =========================
# DONE
# =========================
echo "✅ Project cleaned successfully!"
