#!/usr/bin/env bash
cd $(dirname "$0")/../netatmo/
source .venv/bin/activate
python main.py
