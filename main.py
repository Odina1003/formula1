from chempionship import Chempionship
from driver import Driver
from timeform import TimeForm
from gp import GP

chempionship = Chempionship()

gp = GP('mers form')
driver = Driver('ali')
end_time = TimeForm(12, 45, 34, 123)
print(chempionship.set_time(gp, driver, end_time))
print(gp.get_position('ali', 3))
