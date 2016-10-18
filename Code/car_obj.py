class car(object):
  def __init__(self,speed,fuel,mileage,price=2000):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    # self.tax
  def display_all():
    print self.price
    print self.speed
  def tax():
    if self.price>10000:
      self.taxrate=.15
    else:
      self.taxrate=.12
    self.tax = self.taxrate * self.price

myauto = car(55,"Full",25000,14000)
myauto.display_all
