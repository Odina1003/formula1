from gp import GP

class Driver:
    def init(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def str(self):
        return self.name
    
    def get_reced(self, name):
        pass

    def ball(self, orin, ball):
        overall = []
        overall.append(orin, ball)
        return overall
    