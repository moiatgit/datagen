#! /usr/bin/env python
# encoding: utf-8
#
# Generador aleatòri de dades "creïbles" de persones
#
import sys, os, random
import generanoms, generadnis
#
class PersonaAleatoria:
    def __init__(self):
        generador = generanoms.GeneradorNoms()
        self.nom = generador.genera_nom()
        self.cognoms = generador.genera_cognoms()
        self.nif = generadnis.genera_dni()
        self.email = generaemails.genera_email(self.nom, self.cognoms)

