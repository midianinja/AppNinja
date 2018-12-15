PYTHON = python
CHECKSCRIPT = tools/pep8/pep8ninja.py
NOSETESTS = $(PYTHON) -m nose.core

hook:
	cp tools/pep8/pre-commit.githook ../.git/hooks/pre-commit
	chmod +x ../.git/hooks/pre-commit

style:
	$(PYTHON) $(CHECKSCRIPT) .

test:
	$(NOSETESTS) tests

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  hook           add Pep-8 checking as a git precommit hook"
	@echo "  style          to check Python code for style hints."
	@echo "  testing        make unittest (nosetests)"
