from haydovchi import Driver

class Championship:
    def __init__(self, driver, ism: Driver):
        self._driver = driver
        self.ism: list(Driver) = []

    @property
    def driver(self):
        return self._driver
    
    def get_drivers(self):
        if self.ism != None:
            for i in self.ism:
                return self.ism 