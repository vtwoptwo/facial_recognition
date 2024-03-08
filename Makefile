make env: 
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

make activate:
	. .venv/bin/activate
