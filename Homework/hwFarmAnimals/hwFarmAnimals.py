class FarmAnimals:
  names = None

class Artiodactyls(FarmAnimals):
  food = 1 # kg/h
  distance = 0
  
# 1. COWS

class CowBrown(Artiodactyls):
  milk_yield = 15 # liters/day
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
  def amount_of_milk_per_week(self):
    self.milk_yield * 7

class CowBlack(Artiodactyls):
  milk_yield = 15 # liters/day
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
  def amount_of_milk_per_week(self):
    self.milk_yield * 7

# 2. GOAT
    
class GoatWhite(Artiodactyls):
  milk_yield = 5 # liters/day
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
  def amount_of_milk_per_week(self):
    self.milk_yield * 7

# 3. SHEEPS
    
class Sheeps(Artiodactyls):
  wool = 5 # kg gives one sheep at a time
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
  def amount_of_wool_per_year(self):
    self.wool * 2

# 4. PIGS

class Pigs(Artiodactyls):
  meat = 70 # kg
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
    
  def total_meat(self, number_of_pigs):
    self.meat * number_of_pigs
    
class Birds(FarmAnimals):
  food = 1 # kg/h
  distance = 0

# 5. DUCKS

class Ducks(Birds):
  meat = 2 # kg
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
    
  def total_meat(self, number_of_ducks):
    self.meat * number_of_ducks
    
# 6. CHICKEN

class Chicken(Birds):
  eggs = 3 # pieces per week
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
  def number_of_eggs_per_month(self):
    self.eggs * 4
    
# 7. GEESE

class Geese(Birds):
	meat = 5 # kg

	def total_meat(self, number_of_geese):
    	self.meat * number_of_geese

class GeesWhite(Geese):
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers

class GeesGray(Geese):
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers        
    
class GeesPinto(Geese):
  
  def amount_of_food_per_day(self, hours):
    self.food * hours
    
  def distance_night(self):
    self.distance = 0
  
  def distans_day(self, kilometers):
    self.distance += kilometers
  
    

artiodactyls1 = Artiodactyls()
birds1 = Birds()
cow1 = CowBrown()
cow2 = CowBlack()
goat1 = GoatWhite()
geese0 = Geese()
geese1 = GeesWhite()
geese2 = GeesGray()
geese3 = GeesPinto()

print(artiodactyls1, birds1, cow1, cow2, goat1, geese0, geese1, geese2, geese3)