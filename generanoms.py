#! /usr/bin/env python3
#
# Generador aleatòri de noms "creïbles"
# Pressuposa l'existència dels fitxers: noms.dat i cognoms.dat
# a aquests fitxers es troba la llista de noms i cognoms
# respectivament separats per salt de línia.
# Els noms/cognoms que apareguin precedits per $ es consideraran de
# alta freqüència i apareixeran amb més probabilitat als generadors

# Nota: aquesta versió simplement peta si no troba els fitxers
#
import sys, os, random
#
_FITXER_NOMS = "noms.dat"
_FITXER_COGNOMS = "cognoms.dat"
_FREQ_NOMS = 0.5       # 20% dels noms generats seran dels freqüents
_FREQ_COGNOMS = 0.5    # 10% dels noms generats seran dels freqüents
_FREQ_DOS_COGNOMS = 0.98    # 98% tenen dos cognoms
#
class GeneradorNoms:
    def __init__(self):

        self.noms = []
        self.cognoms = []
        self.noms_freq = []
        self.cognoms_freq = []

        self.carrega_fitxers()

    def carrega_fitxers(self):
        carrega_valors(_FITXER_NOMS, self.noms, self.noms_freq)
        carrega_valors(_FITXER_COGNOMS, self.cognoms, self.cognoms_freq)

    def genera_nom(self):
        llista = self.selecciona_llista_noms()
        nom = random.choice(llista)
        return nom

    def genera_cognom(self, accepta_frequent=True):
        """ Es pot indicar quan no sigui acceptable un cognom freqüent."""
        if accepta_frequent:
            llista = self.selecciona_llista_cognoms()
        else:
            llista = self.cognoms
        cognom = random.choice(llista)
        return cognom

    def genera_cognoms(self, accepta_frequent=True, accepta_un=True):
        """ genera cognoms, majoritàriament dos.
            En cas que accepta_un sigui fals, sempre en genera dos.
            En cas que accepta_frequent sigui fals, no es tindrà en
            compte la freqüència dels cognoms """
        if accepta_un:
            frequent = random.random() < _FREQ_DOS_COGNOMS
        else:
            frequent = True
        if frequent:
            cognoms = "%s %s"%(self.genera_cognom(), self.genera_cognom()) 
        else:
            cognoms = "%s"%(self.genera_cognom(False)) 
        return cognoms

    def genera_nom_cognoms(self, accepta_frequent=True, accepta_un_cognom=True):
        """ composa i retorna un nom amb un o dos cognoms """
        cognoms = self.genera_cognoms(accepta_frequent, accepta_un_cognom)
        return "%s %s"%(self.genera_nom(), cognoms) 

    def selecciona_llista_noms(self):
        """ retorna la llista de noms generals o la freqüent, depenent
        d'un valor aleatòri """
        frequent = random.random() < _FREQ_NOMS
        if frequent:
            llista = self.noms_freq
        else:
            llista = self.noms
        return llista

    def selecciona_llista_cognoms(self):
        """ retorna la llista de cognoms generals o la freqüent, depenent
        d'un valor aleatòri """
        frequent = random.random() < _FREQ_COGNOMS
        if frequent:
            llista = self.cognoms_freq
        else:
            llista = self.cognoms
        return llista

#
def guarda_llista(valors_originals, llista, llista_frequents):
    """ donats uns valors en forma de llista
    filtra els elements que comencen per $ i els duplica a llista i
    llista_frequents. La resta els deixa a llista """
    for element in valors_originals:
        element = element.strip()
        if element.startswith("$"):
            element = element[1:]
            llista_frequents.append(element)
        else:
            llista.append(element)

def carrega_valors(nom_fitxer, llista, llista_frequents):
    with open(nom_fitxer) as f:
        valors = f.readlines()
    guarda_llista(valors, llista, llista_frequents)

#
def main():
    try:
        n = int(sys.argv[1])
    except:
        n = 10
    generador = GeneradorNoms()
    for i in range(n):
        print(generador.genera_nom_cognoms())
    return 0
#
if __name__=="__main__":
    sys.exit(main())

