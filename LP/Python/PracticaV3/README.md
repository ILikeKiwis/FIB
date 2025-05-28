# Intèrpet G

## 1. Makefile
1. `make`  Prepara l'intèrpret.
2. `make tests_all` Executa tots els tests de **/JocsDeProva**, i desa el resultat en els fitxer `.out`   respectius, si aquests no existeixen els crea. 
3. `make clean` Esborra tots els `.out` dels tests i els fitxers creats per `antlr`.
4. `make acti` En cas que la maquina a la que s'està executant el programa no hi siguin les dependències necesaries per l'execució, aquesta regla crea un **venv**, instala les dependències i activa l'entorn virtual per poder executar el programa. 
5. `make deact` En cas que s'hagi activat el **venv** el desactiva.
## 2. Jocs de proves
Els jocs de proves es troven dins el directori `/JocsDeProva`. Quan executem amb `make tests_all` es creen els `.out` corresponents. 
1. **Proves_Enunciat**. Són totes les operacions de prova que surten a l'enunciat de la pràctica. 
2. **Proves_OpBinaris**. 
3. **Proves_OpUnaris**. 
4. **Proves_Assignacio**. Són proves amb assignacions, per comprobar el correcte funcionament d'aquesta funcionalitat.
5. **Errors**. Proves d'errors per veure el comportament del intèrpret davant d'aquests.  
## 3. Documentació