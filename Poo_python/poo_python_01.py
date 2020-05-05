'''
  Estrutura básica da criação de uma classe com um construtor, alguns métodos e instanciamentos (criação de objetos). Além da noção de atributos (variáveis da classe) públicos e privados (__var) (encapsulação).
'''

class Car:
  def __init__(self, company, speed, color, year):
    self.__company = company
    self.__speed = speed
    self.color = color
    self.year = year
  
  def get_speed(self):
    print(self.__speed)
  
  def get_company(self):
    print(self.__company)

  def get_color(self):
    print(self.color)
  
  def get_year(self):
    print(self.year)

Car1 = Car('ABC', 125, 'red', 2019)
Car2 = Car('XYZ', 150, 'blue', 2020)
Car3 = Car('LMN', 200, 'yellow', 2020)

#Não vai dar certo pois esse atributo é algo privado que só pode ser alterado dentro da classe.
Car2.__speed = 300

Car1.get_company()
Car2.get_speed()
Car3.get_color()

