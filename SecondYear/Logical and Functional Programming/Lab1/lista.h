#ifndef LISTA_H
#define LISTA_H


//tip de data generic (for the moment it is an integer)
typedef int TElem;

//referire a structurii Nod;
struct Nod;

//defining PNod as the address of a node
typedef Nod *PNod;

typedef struct Nod{
    TElem e;
	PNod urm;
};

typedef struct{

//prim este adresa primului Nod din lista

	PNod _prim;

} Lista;

//operatii pe lista - INTERFATA

//crearea unei liste din valori citite pana la 0

    Lista creare();

//tiparirea elementelor unei liste

    void tipar(Lista l);

// destructorul listei

	void distruge(Lista l);

#endif
