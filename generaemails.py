#! /usr/bin/env python
# encoding: utf-8
#
# Generador aleatòri d'emails "creïbles"
# Requereix de l'existència del fitxer emails.dat amb una llista
# de dominis de correu creïbles (un per línia)

# atenció: no he tingut en comptes criteris d'optimització a l'hora de
# desenvolupar aquest codi. Cada cop que es crida, torna a carregar-ho
# tot!

import sys, random

_FREQ_EMAILS = 0.5       # 50% dels emails generats seran dels freqüents

def carrega_emails(llista, llista_frequents):
    """ carrega la llista de dominis de emails, distingint les
    freqüents """
    with open("emails.dat") as emails:
        valors = emails.readlines()
    guarda_llista(valors, llista, llista_frequents)

def guarda_llista(valors_originals, llista, llista_frequents):
    for element in valors_originals:
        element = element.strip()
        if element.startswith("$"):
            element = element[1:]
            llista_frequents.append(element)
        else:
            llista.append(element)

def genera_email(nom, cognoms, any_neixement):
    """ a partir de les dades d'una persona, genera un email creïble
    """
    dominis = []
    dominis_frequents = []
    carrega_emails(dominis, dominis_frequents)
    return composa_email(nom, cognoms, data_naixement, dominis, dominis_frequents)


def composa_email(nom, cognoms, any_naixement, dominis, dominis_frequents):
    nom_net = neteja_caracters_especials(nom)
    cognoms_net = neteja_caracters_especials(cognoms)
    any_neixement = any_naixement if any_naixement > 2000 else int(str(any_naixement)[:2])

    # selecció del domini
    frequent = random.random() < _FREQ_EMAILS
    if frequent:
        llista = dominis_frequents
    else:
        llista = dominis

XXX TODO: falta completar
    Fixa't que hauries de ser capaç de distingir els correus
    corporatius on apareixerà el nom i cognoms d'una forma més o menys
    ordenada, mentre que els no corporatius (massius) poden tenir més
    varietat.
    Planteja't fins a quin punt val la pena tanta credibilitat




