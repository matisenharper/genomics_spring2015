__author__ = 'matisencale'

class Genome:
    '''

    '''
    def __init__(self, is_single_stranded, positive_strand_5prime_to_3prime):
        self.single_stranded=is_single_stranded
        self.positive_strand=positive_strand_5prime_to_3prime
        self.negative_strand=self.__get_negative_strand__(self.ps)

    def __get_negative_strand__(self):
        pass