
class Lfnmf(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        self.aname = "lnmf"
        self.amodels = ["nmf_std"]
        self.aseeds = ["random", "fixed", "nndsvd"]
        
    def factorize(self, model):
        self.__dict__.update(model.__dict__)
        