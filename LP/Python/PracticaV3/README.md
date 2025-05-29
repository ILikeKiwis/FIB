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
2. **Proves_OpBinaris**. Conjunt d'operacions per comprobar el correcte funcionament dels operadors binaris.
3. **Proves_OpUnaris**. Molt semblant a *Proves_OpBinaris*, però amb els unaris.
4. **Proves_Assignacio**. Són proves amb assignacions, per comprobar el correcte funcionament d'aquesta funcionalitat.
5. **Errors**. Proves d'errors per veure el comportament del intèrpret davant d'aquests.  
## 3. Documentació
L'intèrpret té una estructura molt bàsica. L'arxiu `g.py`, `Evaler.py` i la gramàtica que es troba a `g.g4`.
1. g.g4
    En aquest arxiu com hem dit abans es troba la gramàtica del subconjunt de J que es demanava. Tracta els operadors demanats, i l'asignació de variables i funcions (que les tractarem igual per simplicitat).  
    Per començar tractarem el nostre programa con un conjunt de *sentències* fins el `EOF`.
    
        program 
            :   statement* EOF
            ;
    
    Aquestes *sentències* poden ser de tres tipus: `assign`, `expr` o `comment`.

    1. **Assign**. 
        Aquest tipus s'encarrega de llegir correctament les diferents assignacions que podem fer, com ara les **variables** o les **funcions**. Ho capturarem d'aquesta manera:

            assign 
                :   ID '=:' assign_expr
                ;
        
        On `ID` és el nom de la variable i `assign_expr` és:

            assign_expr
                :   <assoc=right> assign_expr '@:' assign_expr  #AsExpr
                |   expr                                        #NormalExpr
                |   uop                                         #OnlyUnitary
                ;
    
        * `#AsExpr` serveix pels casos de composició (operador `@`) i ens assegura respectar l'associativitat a la dreta. 
        * `#NormalExpr` ens ajuda a guardar les expresions normals, tant per fer-les servir a les funcions per qualsevol tipus de motiu, o per guardar-les com vairables. Per exemple `a =: 1 2 3 + 1` és una variable vàlida. 
        * `#OnlyUnitary` ens serveix per guardar operadors unitaris que farem servir a les funcions. Per exemple `inc =: 1 + ]`. 
    2. **Expr**. 
        Les expresions s'encarreguen de llegir correctament les diferents operacions que hi ha dins del programa, fent servir com a operands el tipus base de G o bé variables i funcions. 
        
            expr
                :   <assoc=right> expr BOP flip* expr           #BinaryOP
                |   <assoc=right> uop expr                      #UnitaryOP
                |   <assoc=right> ID expr                       #IdValue  
                |   '('expr')'                                  #Prio
                |   numList                                     #List  
                |   expr '#' flip* expr                         #FilterOP
                |   ']'                                         #Identity
                |   ID                                          #Id
                ;   
            
        * `#BinaryOP` és la expressió que farem servir per fer operacions binaries entre dues expresions. Per exemple `1 2 3 + 1 2 3` o siguent `x =: 1 2 3 ` també podem fer `x ^ 2`.
        * `#UnitaryOP` és semblant a *BinaryOP* però ens captura les operacions unaries.
        Per exemple `+/ 1 2 3`  
        * `#IdValue` és la regla que fem servir quan fem crides de funcions.
        Per exemple `inc i. 3`
        * `#Prio` ens permet trencar l'associativitat a la dreta amb parèntesis. 
        * `#List` el tipus base de **G**.
        * `FilterOP` és la operació binària de `#`, però per conflictes amb la seva versió unaria hi ha una expressió només per aquesta operació. 
        * `#Identity` ens permet fer servir `]` a les funcions. 
        * `#Id` captura els *id* de les variables per poder retornar els seus valors. 

        **Coses a tenir en compte**: 
            1. `BOP` és la llista de operadors binaris que s'han d'implementar. 
            2. `flip` és l'operador que gira els operands. Podem tenir molts consecutius. 
            3. `uop` és la llista d'operados unaris. És en minúscules ja que neceistem poder entrar al contexte i mirar si hi ha operadors binaris `BOP` per operadors com `/` o `:`.
            4. L' **expresion regular** per els `ID` és `[A-Za-z] [A-Za-z0-9_]*` que evita començar els noms amb `_` o altres tipus de carràcter i això ho aprofitem més tard al `Evaler`. Per els números tenim `[0-9]+`. 
        
    3. **Comment**. 
        Són els comentaris de G. Comencen per `NB.` i s'ignoren durant l'execució.
    
    \
    Per més detalls es recomana visitar l'arxiu `g.g4`.

