from .resources import PersonResource

person_resource = PersonResource()
dataset = person_resource.export()
dataset.csv