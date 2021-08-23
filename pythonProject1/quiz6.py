class Electronicdevice:
    resistor=1
    pass
class Pocketgadget(Electronicdevice):
    display=1
    pass
class Phone(Pocketgadget):
    features=1
    pass
gmeter=Electronicdevice()
pager=Pocketgadget()
honor=Phone()
print(honor.resistor)