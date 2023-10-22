from driver import Driver
from gp import GP
from timeform import TimeForm

class Time:
    def init(self, gp: GP, driver: Driver, tugash_vaqti: TimeForm):
        self._gp = gp
        self._driver = driver
        self._tugash_vaqti = tugash_vaqti
    
    def str(self) -> str:
        a = self._tugash_vaqti
        return a.to_string()
    