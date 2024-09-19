#!/bin/bash
export PYTHONPATH=$(dirname $(dirname $(realpath $0)))
python frontend/chat_app.py