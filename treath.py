from chimera_ant import ChimeraAnt
from phantom_team import PhantomTeamMember

class Treath(ChimeraAnt, PhantomTeamMember):
    def __init__(self,name, specie, level, nen):
        self.name = name
        self.specie = specie
        self.level = level
        self.nen = nen
    
    def awake_nen(self):
        if self.nen == True:
            self.is_awake = True
