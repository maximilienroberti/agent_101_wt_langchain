.PHONY: clean_install

clean_install:
	rm -rf .venv
	@PYTHON_BIN=$$(for py in python3.13 python3.12 python3.11 python3; do \
		if command -v $$py >/dev/null 2>&1; then \
			$$py -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' >/dev/null 2>&1 && { echo $$py; break; }; \
		fi; \
	done); \
	if [ -z "$$PYTHON_BIN" ]; then \
		echo "Python 3.11 or newer is required."; \
		exit 1; \
	fi; \
	echo "Using $$PYTHON_BIN"; \
	$$PYTHON_BIN -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
