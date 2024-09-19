#!/bin/bash
export PYTHONPATH=$(dirname $(dirname $(realpath $0)))
python scripts/query_docs.py
