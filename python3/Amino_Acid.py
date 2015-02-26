__author__ = 'matisencale'

from python3.tRNA import tRNA

class Amino_Acid:
    '''

    '''
    def __init__(self, codon):
        self.name = tRNA.produce_amino_acid(codon)