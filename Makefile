
default: help


build : ##Build package
	python setup.py build

sdist : ##Create dist file
	python setup.py sdist

wheel : ##Create wheel file
	python setup.py bdist_wheel --universal

upload-wheel : wheel ##Create wheel file
	python setup.py bdist_wheel --universal upload

clean : ##Clean
	$(RM) -r build/
	$(RM) -r dist/
	$(RM) -r whitespacelint.egg-info
	$(RM) -r .tox/
	-find . -name "*.pyc"      -delete 2>/dev/null; true
	-find . -name __pycache__  -delete 2>/dev/null; true

.PHONY: help
help  : ##Show this help
	@echo "-----------------------------------------------------------------"
	@echo "  Available make targets"
	@echo "-----------------------------------------------------------------"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -rn "s/(\S+)\s+:+?\s##(.*)/\1 \"\2\"/p" | xargs printf " %-20s    : %5s\n"
	@echo
