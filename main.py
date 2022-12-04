class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, number):
    self.numberOfStudents = number
  
  def __repr__(self):
    print("A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents))
  
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(self, name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return print(parentRepr + "The pickup policy is {}".format(pickupPolicy = self.pickupPolicy))

class Highschool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    return print("The sports teams are {}".format(self.sportsTeams))

a = School("NOVA", "college", 100) 
a.set_numberOfStudents(100)
print(a.get_name())
print(a.get_level())
print(a)

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())
print(b)

c = Highschool("DeMatha", 750, ["Football", "LaCrosse"])
print(c.get_sportsTeams())
print(c)