from driver import Driver

class GP:
    def init(self, name):
        self._name = name
        self._gp_list: list[Driver] = []

    def add_driver(self, driver: Driver):
        self._gp_list.append(driver)
        print('gp ga driver qo\'shildi')

    @property
    def name(self):
        return self._name
    
    def str(self) -> str:
        return self.name

    def get_gp_parking(self):
        return self._gp_list
    
    def get_position(self, name, orin):
        for i in self._gp_list:
            if i.name == name:
                return f'{name} ning olgan o\'rni{orin}'
            