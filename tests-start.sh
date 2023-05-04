#! /usr/bin/env sh
set -e

python3.8 tests_pre_start.py

sh ./scripts/test.sh "$@"
