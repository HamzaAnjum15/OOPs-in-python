class animal:
    animaltype='mammal'
class pets(animal):
    color='white'
class dogs(pets):
    @staticmethod
    def bark():
        print("bow bow!")
c=dogs()
c.bark()