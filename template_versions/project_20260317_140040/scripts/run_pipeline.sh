#!/bin/bash

echo "🚀 Ejecutando pipelines medallion"

python3 src/pipelines/bronze/ingest_personas.py
python3 src/pipelines/silver/transform_personas.py
python3 src/pipelines/gold/aggregate_personas.py
