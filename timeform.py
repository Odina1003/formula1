class TimeForm:
    def init(self, hour, minut, second, ms):
        self.hour = hour
        self.minut = minut
        self.second = second
        self.ms = ms
    
    def to_string(self) -> str:
        return f'{self.hour} : {self.minut} : {self.second} : {self.ms}'
    