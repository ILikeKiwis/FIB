all: misat misat2 OGsat misat3

misat:	SAT-alumnes.cpp
	g++ -O3 -Wall SAT-alumnes.cpp -o misat

misat2: SAT-alumnes-H2.cpp
	g++ -O3 -Wall SAT-alumnes-H2.cpp -o misat2

misat3: SAT-alumnes-H3.cpp
	g++ -O3 -Wall SAT-alumnes-H3.cpp -o misat3

OGsat: SAT-alumnesOG.cpp
	g++ -O3 -Wall SAT-alumnesOG.cpp -o OGsat


clean:
	rm -f misat OGsat