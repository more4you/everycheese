from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from everycheese.cheeses.models import Cheese
from faker import Faker 

class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    country_of_origin = factory.Faker('country_code', )

    fake = Faker({'en-US': 1}) 
    fake.country_code()

    class Meta:
        model = Cheese
