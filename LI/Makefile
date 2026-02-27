all: misat misat2 OGsat

misat:	SAT-alumnes.cpp
	g++ -O3 -Wall SAT-alumnes.cpp -o misat

misat2: SAT-alumnes-H2.cpp
	g++ -O3 -Wall SAT-alumnes-H2.cpp -o misat2

OGsat: SAT-alumnesOG.cpp
	g++ -O3 -Wall SAT-alumnesOG.cpp -o OGsat


clean:
	rm -f misat OGsat