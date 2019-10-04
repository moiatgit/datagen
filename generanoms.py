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

import sys
import os
import random
import argparse

_VERSION = '1.1'
#
_FITXER_NOMS = "noms.dat"
_FITXER_COGNOMS = "cognoms.dat"
_FREQ_NOMS = 0.5       # 20% dels noms generats seran dels freqüents
_FREQ_COGNOMS = 0.5    # 10% dels noms generats seran dels freqüents
_FREQ_DOS_COGNOMS = 0.98    # 98% tenen dos cognoms


def compose_argparse():
    """ composes and returns an ArgumentParser """
    p = argparse.ArgumentParser(description = "Name generator")

    p.add_argument('-n', action='store', default=10, type=int,
            help=u"Number of results. Default 10.", dest='how_many')

    p.add_argument('-f', '--format', action='store',
                   choices = ['nss', 'scn'],
                   default = 'nss',
                   help=u"Output format. 'nss': name-space-surnames (default). 'scn': surname-coma-name")
    p.add_argument('-v', '--version', action='version',
                   version='%s %s' % (sys.argv[0], _VERSION))
    return p


class GeneradorNoms:
    def __init__(self, output_format):
        """ Given the output format, initializes the instance """

        self.output_format = output_format
        self.noms = []
        self.cognoms = []
        self.noms_freq = []
        self.cognoms_freq = []

        self.carrega_fitxers()


    def carrega_fitxers(self):
        carrega_valors(_FITXER_NOMS, self.noms, self.noms_freq)
        carrega_valors(_FITXER_COGNOMS, self.cognoms, self.cognoms_freq)

    def genera_nom(self):
        """ returns a random name from the list of names """
        llista = self.selecciona_llista_noms()
        nom = random.choice(llista)
        return nom

    def genera_cognom(self, accepta_frequent=True):
        """ returns a random surname from the list of surnames
            accepta_frequent: when False, this method won't result in a
                              frequent surname
        """
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
            compte la freqüència dels cognoms.

            It returns a tuple with one or more surnames.
            """
        if accepta_un:
            frequent = random.random() < _FREQ_DOS_COGNOMS
        else:
            frequent = True
        if frequent:
            cognoms = (self.genera_cognom(), self.genera_cognom())
        else:
            cognoms = (self.genera_cognom(False),)

        return cognoms


    def genera_nom_cognoms(self, accepta_frequent=True, accepta_un_cognom=True):
        """ composa i retorna un nom amb un o dos cognoms """

        name = self.genera_nom()
        surnames = self.genera_cognoms()

        if self.output_format == 'scn':
            result = '%s, %s' % (' '.join(surnames), name)
        else:
            result = '%s %s'%(name, " ".join(surnames))
        return result


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
    """ checks commandline args and performs accordingly """

    p = compose_argparse()
    options = p.parse_args()
#
    generador = GeneradorNoms(options.format)
    for i in range(options.how_many):
        print(generador.genera_nom_cognoms())
    return 0
#
if __name__=="__main__":
    sys.exit(main())

