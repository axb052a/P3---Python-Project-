class User:
    def __init__(self, name, height_ft, height_inches, weight):
        self.name = name
        self.height_ft = height_ft
        self.height_inches = height_inches
        self.weight = weight
        self.workouts = []

@property
def name(self):
    return self._name
@name.setter
def name(self, new_name):
     if isinstance(new_name, str) and 2 <= len(new_name) <= 25:  
            self._name = new_name
     else:
         raise Exception("Name must be a string with a length between 2 and 25 characters.")
@property
def height_ft(self):
    return self._height_ft
@height_ft.setter
def height_ft(self, new_height_ft):
    self._height_ft = new_height_ft
    
@property
def height_inches(self):
    return self._height_inches

@height_inches.setter
def height_inches(self, new_height_inches):
    self._height_inches = new_height_inches
    
@property
def weight(self):
    return self._weight
@weight.setter
def weight(self, new_weight):
    self._weight = new_weight
    
def add_height(self, new_height_ft, new_height_inches):
    # Validate inputs for height
    if not isinstance(new_height_ft, int) or not isinstance(new_height_inches, int):
        raise Exception("Height values must be integers.")
    
    if new_height_ft < 0 or new_height_ft > 10 or new_height_inches < 0 or new_height_inches >= 12:
        raise Exception("Invalid height values. Height must be within the range of 0-10 feet and 0-11 inches.")
    
    self.height_ft = new_height_ft
    self.height_inches = new_height_inches
    
    
def add_weight(self, new_weight):
    # Validate input for weight
    if not isinstance(new_weight, (float, int)):
        raise Exception("Weight must be a float or integer.")
    
    if new_weight <= 0:
        raise ValueError("Weight must be greater than 0.")
    
    self.weight = new_weight

