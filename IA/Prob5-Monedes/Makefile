J = java
JC = javac 

SRC=$(shell find src -name "*.java")

all: exec

comp: 
	@$(JC) -cp lib/** -d bin $(SRC)

exec:comp
	@$(J) -cp "bin:lib/*" Main