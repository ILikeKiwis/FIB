# Variables per crear el venv en cas de que sigui necesari
V_DIR := venv


# Tests
T_DIR := JocsDeProva
TESTS:= $(wildcard $(T_DIR)/*.j)
OUT_TESTS := $(TESTS:.j=.out)

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

acti: 
	@python3 -m venv $(V_DIR)
	@source $(V_DIR)/bin/activate
	@pip install antlr4-tools
	@pip install antlr4-python3-runtime 

deact: 
	@deactivate 

tests_all: all $(OUT_TESTS)


$(T_DIR)/%.out: $(T_DIR)/%.j
	@echo "==== Executant tests ===="
	python3 g.py "$<" > "$@"


clean:
	rm -rf $(OUT_TESTS)
	rm -rf $(INT_TEMP)



.PHONY: all acti tests_all clean deact 