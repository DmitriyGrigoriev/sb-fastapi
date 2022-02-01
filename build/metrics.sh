#!/usr/bin/env bash

if [ -n "$DEBUG" ]; then
	set -x
fi

set -o errexit
set -o nounset
set -o pipefail

DIR=$(cd $(dirname "${BASH_SOURCE}") && pwd -P)

poetry run flake8 --select=E,W,I --max-line-length 80 --import-order-style pep8 --exclude .git,__pycache__,.eggs,*.egg,.pytest_cache,sb_backend/version.py,sb_backend/__init__.py --tee --output-file=pep8_violations.txt --statistics --count sb_backend
poetry run flake8 --select=D --ignore D301 --tee --output-file=pep257_violations.txt --statistics --count sb_backend
poetry run flake8 --select=C901 --tee --output-file=code_complexity.txt --count sb_backend
poetry run flake8 --select=T --tee --output-file=todo_occurence.txt --statistics --count sb_backend tests
poetry run black -l 80 --check sb_backend
