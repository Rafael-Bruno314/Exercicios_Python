'''
  Sobre heranças:
    Existem diversos tipos de heranças com diferenças sutis entre eles, um programa pode ter várias delas, mas em geral uma classe filha herda os métodos da classe(s) pai.
'''

#Exemplo de uma herança hierarquica, nada demais...
class Car:
  def __init__(self, company, speed, color, year):
    self.company = company
    self.speed = speed
    self.color = color
    self.year = year

  def get_speed(self):
    print(self.speed)

  def get_company(self):
    print(self.company)

  def get_color(self):
    print(self.color)

  def get_year(self):
    print(self.year)
    
class Trike(Car):
  def __init__(self, company, speed, color, year):
    self.company = company
    self.speed = speed
    self.color = color
    self.year = year
    
class Cycle(Car):
  def __init__(self, company, speed, color, year):
    self.company = company
    self.speed = speed
    self.color = color
    self.year = year

Car1 = Car("ABC", 125, "RED", 2019)
Car2 = Car("XYZ", 150, "BLUE", 2020)
Car3 = Car("LMN", 200, "YELLOW", 2020)

Trike1 = Trike("GHJ", 90, "Grey", 2020)
Trike2 = Trike("DFG", 80, "Violet", 2019)

Cycle1 = Cycle("WER", 30, "RED", 2020)

Trike1.get_company()
Cycle1.get_color()
