#! /usr/bin/env python
# encoding: utf-8
#
# Generador aleatòri de dnis vàlids
# És a dir, els DNIs generats respecten la fòrmula de validació.

import sys, random

def calcula_lletra(dni):
    """ a partir dels números d'un DNI, retorna la lletra que li
    correspon per ser un NIF.
    """
    assert(isinstance(dni, str))
    assert(len(dni)==8)
    assert(dni.isdigit())
    lletres = "TRWAGMYFPDXBNJZSQVHLCKE"
    return lletres[int(dni)%23]

def genera_dni():
    """ retorna un DNI aleatòri en forma de string """
    nums = []
    for i in range(8):
        nums.append(random.randint(0, 9))
    return "".join(str(n) for n in nums)

def genera_nif():
    """ retorna un NIF aleatòri vàlid """
    dni = genera_dni()
    nif = dni + calcula_lletra(dni)
    return nif

#
def main():
    try:
        n = int(sys.argv[1])
    except:
        n = 10
    for i in range(n):
        print genera_nif()
    return 0
#
if __name__=="__main__":
    sys.exit(main())

