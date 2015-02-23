__author__ = 'matisencale'

class FASTA_Parser:
    '''

    '''
    def __init__(self, FASTA_file):
        self.FASTA_file = FASTA_file
        self.genome_id = self.get_id()
        self.genome_description = self.get_description()
        self.genome = self.get_genome()

    def get_id(self):
        pass

    def get_description(self):
        pass

    def get_genome(self):
        pass