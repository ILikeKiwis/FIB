#include "CacheSim.h"
#include <stdio.h>
/* Posa aqui les teves estructures de dades globals
 * per mantenir la informacio necesaria de la cache
 * */
typedef struct{
	unsigned int tag;
	unsigned int v;
} via;

typedef struct{	
	via via0;
	via via1;
	unsigned int LRU; // 0/1
} conj;


conj cache[64];
unsigned int nMiss, nHit;



/* La rutina init_cache es cridada pel programa principal per
 * inicialitzar la cache.
 * La cache es inicialitzada al comen�ar cada un dels tests.
 * */
void init_cache ()
{
    totaltime=0.0;
	/* Escriu aqui el teu codi */
	for(int i = 0; i<64; i++) {
		cache[i].LRU = cache[i].via0.v = cache[i].via1.v = 0;
	}
	nMiss = nHit = 0;
}

/* La rutina reference es cridada per cada referencia a simular */ 
void reference (unsigned int address)
{
	unsigned int byte;
	unsigned int bloque_m; 
	unsigned int conj_mc;
	unsigned int via_mc;
	unsigned int tag;
	unsigned int miss;	   // boolea que ens indica si es miss
	unsigned int replacement;  // boolea que indica si es reempla�a una linia valida
	unsigned int tag_out;	   // TAG de la linia reempla�ada
	float t1,t2;		// Variables per mesurar el temps (NO modificar)
	
	t1=GetTime();
	/* Escriu aqui el teu codi */
	byte = address & 0b11111;				
	bloque_m = address >> 5;				
	conj_mc = bloque_m & 0b111111;
	tag = bloque_m >> 6;

	if (cache[conj_mc].via0.v == 0) {		// No hi ha res a aquest conjunt
		replacement = 0;
		miss = 1;
		nMiss++;
		via_mc = 0;
		cache[conj_mc].LRU = 1;
		cache[conj_mc].via0.v = 1;
		cache[conj_mc].via0.tag = tag;
	}
	else {	
		if (cache[conj_mc].via0.tag != tag){	// vi0 es miss
			if (cache[conj_mc].via1.v == 0){	// via 1 no valida
				replacement = 0;
				miss = 1;
				nMiss++;
				via_mc = 1;
				cache[conj_mc].LRU = 0;
				cache[conj_mc].via1.v = 1;
				cache[conj_mc].via1.tag = tag;
			}
			else 
				if (cache[conj_mc].via1.tag != tag){		// Cap de les dues vies té el tag i son valides / miss 
					miss = 1;
					nMiss++;
					replacement = 1;
					if (cache[conj_mc].LRU == 1){			// Mirem LRU per saber on posar el tag
						cache[conj_mc].LRU = 0;
						via_mc = 1;
						tag_out = cache[conj_mc].via1.tag;
						cache[conj_mc].via1.tag = tag;

					}
					else {
						cache[conj_mc].LRU = 1;
						via_mc = 0;
						tag_out = cache[conj_mc].via0.tag;
						cache[conj_mc].via0.tag = tag;
					}
			}
			else {	// via1 HIT
				cache[conj_mc].LRU = 0;
				miss = 0;
				replacement = 0;
				via_mc = 1;
				nHit++;
			}
		}
		else {		// via0 HIT
			cache[conj_mc].LRU = 1;
			miss = 0;
			replacement = 0;
			via_mc = 0;
			nHit++;
		}
	}




	/* La funcio test_and_print escriu el resultat de la teva simulacio
	 * per pantalla (si s'escau) i comproba si hi ha algun error
	 * per la referencia actual. Tamb� mesurem el temps d'execuci�
	 * */
	t2=GetTime();
	totaltime+=t2-t1;
	test_and_print2 (address, byte, bloque_m, conj_mc, via_mc, tag,
			miss, replacement, tag_out);
}

/* La rutina final es cridada al final de la simulacio */ 
void final ()
{
 	/* Escriu aqui el teu codi */ 
  printf("nHit : %d, nMiss %d \n", nHit, nMiss);
  
}
