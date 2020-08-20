from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from everycheese.cheeses.models import Cheese
from faker import Faker
from everycheese.users.tests.factories import UserFactory

class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    # fake = Faker({'en-US': 1}) 
    # fake.country_code()
    # country_of_origin = Faker('country_code' )
    creator = factory.SubFactory(UserFactory)

    

    class Meta:
        model = Cheese
