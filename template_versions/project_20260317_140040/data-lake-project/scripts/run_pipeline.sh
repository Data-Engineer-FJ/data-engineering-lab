#!/bin/bash

echo "🚀 Ejecutando pipelines medallion"

python src/pipelines/bronze/ingest_personas.py
python src/pipelines/silver/transform_personas.py
python src/pipelines/gold/aggregate_personas.py
