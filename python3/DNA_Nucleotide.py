__author__ = 'matisencale'

class DNA_Nucleotide:
    '''

    '''
    def __init__(self, DNA_nucleotide_as_string):
        self.symbol = str.upper(DNA_nucleotide_as_string)
        self.description = self.get_description()

    def get_description(self):
        symbol_description = {'A':"adenine",'C':"cytosine",'G':"guanine",'T':"thymine"}
        return symbol_description[self.symbol]

'''
dna_nucleotide_test_A = DNA_Nucleotide("A")
dna_nucleotide_test_C = DNA_Nucleotide("C")
dna_nucleotide_test_G = DNA_Nucleotide("G")
dna_nucleotide_test_T = DNA_Nucleotide("T")

print("test A")
print("A : " + str(dna_nucleotide_test_A))
print("A.symbol : " + str(dna_nucleotide_test_A.symbol))
print("A.description : " + str(dna_nucleotide_test_A.description))

print("test C")
print("C : " + str(dna_nucleotide_test_C))
print("C.symbol : " + str(dna_nucleotide_test_C.symbol))
print("C.description : " + str(dna_nucleotide_test_C.description))

print("test G")
print("G : " + str(dna_nucleotide_test_G))
print("G.symbol : " + str(dna_nucleotide_test_G.symbol))
print("G.description : " + str(dna_nucleotide_test_G.description))

print("test T")
print("T : " + str(dna_nucleotide_test_T))
print("T : " + str(dna_nucleotide_test_T.symbol))
print("T : " + str(dna_nucleotide_test_T.description))
'''