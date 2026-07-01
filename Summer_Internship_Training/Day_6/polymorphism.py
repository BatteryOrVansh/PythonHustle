class DietPlan:
    pass

# Child Class 1: Keto Diet
class KetoDiet(DietPlan):
    def get_breakfast(self):
        return "Scrambled eggs with avocado"
    
# Child class 2: Vegan Diet
class VeganDiet(DietPlan):
    def get_breakfast(self):
        return "Oatmeal with fruits and nuts"

# Child class 3: High Protein Diet plan
class HighProteinDiet(DietPlan):
    def get_breakfast(self):
        return "Greek yogurt with berries and chia seeds"

# Polymorphic function
# This function accept any diet objecgt and call its get_breakfast method
def print_morning_routine(diet_plan):
    print(f"Today's suggestion: {diet_plan.get_breakfast()}")
    
# Create an instance of each diet plan``
my_keto_diet = KetoDiet()
my_vegan_diet = VeganDiet()
my_high_protein_diet = HighProteinDiet()

# Pass the differnt diet objects to the polymorphic function
print_morning_routine(my_keto_diet)
print_morning_routine(my_vegan_diet)
print_morning_routine(my_high_protein_diet)
