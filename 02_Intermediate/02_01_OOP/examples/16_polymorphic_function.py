
# 16_polymorphic_function.py
class India:
    def capital(self):
        print("Capital of India is New Delhi")
    def language(self):
        print("Hindi is widely spoken")
class USA:
    def capital(self):
        print("Capital of USA is Washington D.C.")
    def language(self):
        print("English is widely spoken")
# Polymorphic Function
def country_info(country):
    country.capital()
    country.language()
    print("-" * 30)
# Using the same function with different objects
india = India()
usa = USA()
country_info(india)
country_info(usa)

