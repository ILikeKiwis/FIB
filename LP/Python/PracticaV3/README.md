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
L'intèrpret té una estructura molt bàsica. La gramàtica que es troba a `g.g4`, la classe `Evaler.py` i el programa principal `g.py`.
1. **`g.g4`**
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
2. **`Evaler.py`**
    En aquesta classe trobem l'implementació de totes les operacions fent servir el **visitador**.
    Hi trobem definides les funcions següents (seguint el mateix ordre que a l'arxiu): 
    * `__init__`. Aquí el que fem és inicialitzar el diccionari d'assignacions anomenat `self.vars`.
    * `visitProgram`. Aquesta funció recull la llista de *statements* i evalúa cada un.
    * `visitAssignSt`. És una funció que simplement recull el fill `assign` del contexte *AssignSt* i el visita per fer l'assignació.
    * `visitExprSt`. Recull el fill `expr` del contexte *ExprSt* i recull el resultat d'evaluar aquesta expressió. Posteriorment l'envia per la sortida estandar.
    * `visitCom`. Simplement ignora els comentaris. Recull el text ja que en el J Playground els comentaris es veien a la consola, pero per indicació del professorat aquests s'ignoren. Si es volgués veure per la sortida estandar simplement hem de fer print de la variable `ret` que recull el text del comentari.
    * `visitAssign`. S'encarrega de fer **l'assignació** de variables i funcions. Guarda al diccionari `self.vars` la clau `ID` i el valor `expr`.
    * `visitAsExpr`. Aquí passa tota la *màgia* de les funcions. S'encarrega de executar correctament les funcions creades per composició. Com ho fa? Per tal de respectar l'associativitat cap a la dreta, recull ambdues *expressions* i executa primer la de la **dreta**, guardant el resultat a una variable arbitrària `__identity__` (per veure més informació d'aquesta variable, anar a l'apartat adient), i seguidament executa *l'expressió* de **l'esquerra**. També abans d'executar aquesta segona *expressió* guarda l'estat de `self.vars` per poder recuperar-lo més tard en cas que hi hagi més funcions compostes dins *l'expresió* de l'esquerra. Finalment retorna el **resultat** de la funció.
    * `visitOnlyUnitary`. És la funció encarregada de tractar les funcions que contenen operadors unaris. El que fem és fer servir com a valor el contingut de la variable `__identity__`, ja que abans d'entrar en aquest node hem passat per un node que guarda el *paràmetre* de la funció (*l'expressió* que te a la **dreta**), ja sigui `visitAsExpr` o `visitIdValue` o `visitBinaryOP`. Entés això, la funció és trivial, aplica la lògica de l'operador que hi ha dins de `uop`, i si n'hi ha a `BOP` dins del contexte *uop*, al valor que hem trobat a la variable com hem explicat anteriorment.
    * `visitBinaryOP`. Funció encarregada de les operacions **binàries**. Evalua les *expressions* que té, aplica els `flip` que pertoquin per canviar els operands d'ordre, i finalment, aplica la lògica que pertoca pel operador que ve donat per `BOP`. 
    * `visitUnitaryOP`. Idèntica a `visitOnlyUnitary` però pren com a valor l'evaluació del `expr` que ve donat. 
    * `visitIdValue`. És la funció encarregada de la **crida** a funcions. El que fem és evaluar `expr` i guardar el resultat dins de `__identity__`. Després visitem el que hi hagi dins de `self.vars[ID]`, i gràcies a `__identity__` tenim sobre que aplicar la funció. 
    * `visitPrio`. Trivial. S'encarrega de lús de `()`.
    * `visitList`. Ens retorna el tipus base de **G**. Evalua la `numList` que té dins del *context* i la transforma en un `np.array`.
    * `visitFilterOP`. Com fem servir `#` tant com operador unari com binari, necesitem donar precedència a l'operació binària, sinó aquesta operació es tractaria dins de `visitBinaryOP`.
    * `visitIdentity`. Funció que fem servir quan les funcions acaben en `]`. Ens retorna el valor de la variable `__identity__`. És el que ens permet que les funcions es passin els resultats.
    * `visitId`. Encarregada de retornar el valor de les variables. Molt simple, `self.vars[ID]`.
    * `visitNum`. Ens retorna cada número a `numList`.
    * `visitComment`. Tracta el text dels comentaris per si es volguesin treure per sortida estandar com ho fa el **J Playground**. 
    
    * **`__identity__`**. És una variable que trobem definida dins de `self.vars[__identity__]`. Porta els `__` ja que la **expressió regular** que captura els *IDs* no permet que comencin amb `_` entre altres. És l'encarregada de passar els *paràmetres* a les funcions que es poden definir a **G**. És a dir, ens ajuda a aplicar una funció al valor que te a la **dreta**.

3. **`g.py`**
    El programa principal de l'intèrpret. 
    1. Llegiex l'arxiu `.j` que rep com a paràmentre. 
    2. Amb `gLexer` fem l'**analisi lèxic**.
    3. Després conjuntament amb el `token stream` creem l'`AST` amb el `gParser`.
    4. Agafem l'arrel del progama `tree.program()` i li pasem a l'`Evaler`.