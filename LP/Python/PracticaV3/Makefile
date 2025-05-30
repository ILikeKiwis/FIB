# Variables per crear el venv en cas de que sigui necesari
V_DIR := venv

# Tests
T_DIR := JocsDeProva
TESTS:= $(wildcard $(T_DIR)/*.j)
OUT_TESTS := $(TESTS:.j=.out)

# En cas que es necesiti el venv
ifeq ($(MAKECMDGOALS),tests_all_venv)
	VENV := 1
else 
	VENV:= 0
endif

# Els fitxers que no s'han de borrar al fer make clean.
INT_TEMP := $(shell find . -maxdepth 1	! -name Makefile \
										! -name README.md \
										! -name g.py \
										! -name Evaler.py \
										! -name g.g4 \
										! -name . \
										! -name JocsDeProva \
										! -name ..)


all: 
	@echo "==== Preparant interpret ===="
	@antlr4 -Dlanguage=Python3 -no-listener -visitor g.g4


venv: 
	@python3 -m venv $(V_DIR)
	@$(V_DIR)/bin/pip install antlr4-tools
	@$(V_DIR)/bin/pip install antlr4-python3-runtime
	@$(V_DIR)/bin/pip install numpy


tests_all: all $(OUT_TESTS)

tests_all_venv: tests_all


$(T_DIR)/%.out: $(T_DIR)/%.j
	@echo "==== Executant tests ===="
	$(if $(filter 1,$(VENV)),$(V_DIR)/bin/python3,python3) g.py "$<" > "$@"



clean:
	rm -rf $(OUT_TESTS)
	rm -rf $(INT_TEMP)


.PHONY: all venv tests_all clean tests_all_venv