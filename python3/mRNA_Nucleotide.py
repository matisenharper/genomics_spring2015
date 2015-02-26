__author__ = 'matisencale'

class mRNA_Nucleotide:
    '''

    '''
    def __init__(self, DNA_nucleotide_as_string):
        self.symbol = str.upper(DNA_nucleotide_as_string)
        self.description = self.get_description()

    def get_description(self):
        symbol_description = {'A':"adenine",'C':"cytosine",'G':"guanine",'U':"uracil"}
        return symbol_description[self.symbol]

'''
mRNA_nucleotide_test_A = mRNA_Nucleotide("A")
mRNA_nucleotide_test_C = mRNA_Nucleotide("C")
mRNA_nucleotide_test_G = mRNA_Nucleotide("G")
mRNA_nucleotide_test_U = mRNA_Nucleotide("U")


print("test A")
print("A : " + str(mRNA_nucleotide_test_A))
print("A.symbol : " + str(mRNA_nucleotide_test_A.symbol))
print("A.description : " + str(mRNA_nucleotide_test_A.description))

print("test C")
print("C : " + str(mRNA_nucleotide_test_C))
print("C.symbol : " + str(mRNA_nucleotide_test_C.symbol))
print("C.description : " + str(mRNA_nucleotide_test_C.description))

print("test G")
print("G : " + str(mRNA_nucleotide_test_G))
print("G.symbol : " + str(mRNA_nucleotide_test_G.symbol))
print("G.description : " + str(mRNA_nucleotide_test_G.description))

print("test U")
print("U : " + str(mRNA_nucleotide_test_U))
print("U : " + str(mRNA_nucleotide_test_U.symbol))
print("U : " + str(mRNA_nucleotide_test_U.description))
'''