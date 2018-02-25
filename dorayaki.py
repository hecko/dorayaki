#!/usr/bin/env python3

from pprint import pprint

# zakladna definicia
muka = 75
cukor = 30
vajce = 1
prasok = 4
mlieko = 90
kusy = 7

vajec = 3

def kolko(vajec):
    out = {}
    out['vajec_kus'] = vajec
    out['muka_g'] = muka * vajec
    out['cukor_g'] = cukor * vajec
    out['prasok_do_peciva_g'] = prasok * vajec
    out['mlieko_g'] = mlieko * vajec
    return out

print("Pri {} vajciach pouzi:".format(vajec))
pprint(kolko(vajec))
print("Predpokladany pocet porcii pri 0.04l odmerke: {}".format(vajec * kusy))
