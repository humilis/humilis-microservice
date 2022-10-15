HUMILIS := .env/bin/humilis
PIP := .env/bin/pip
PYTHON := .env/bin/python
TOX := .env/bin/tox
TWINE:= .env/bin/twine
STAGE := DEV
HUMILIS_ENV_PATH := tests/integration/
HUMILIS_ENV := humilis-microservice

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt

# run integration tests
test: .env
	$(PIP) install tox
	$(TOX)

# remove .tox and .env dirs
clean:
	rm -rf .env .tox

# configure humilis
configure:
	$(HUMILIS) configure --local

# deploy the test environment
create: develop
	$(HUMILIS) create \
		--stage $(STAGE) \
		--output $(HUMILIS_ENV)-$(STAGE).outputs.yaml \
		$(HUMILIS_ENV_PATH)$(HUMILIS_ENV).yaml.j2

# update the test deployment
update: develop
	$(HUMILIS) update \
		--stage $(STAGE) \
		--output $(HUMILIS_ENV)-$(STAGE).outputs.yaml \
		$(HUMILIS_ENV_PATH)$(HUMILIS_ENV).yaml.j2

# delete the test deployment
delete: develop
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV_PATH)$(HUMILIS_ENV).yaml.j2

# upload to Pypi
pypi: develop
	rm -rf dist
	$(PYTHON) setup.py sdist
	$(TWINE) upload dist/*
