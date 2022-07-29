from django.template.defaultfilters import slugify
import pytest

import factory
import factory.fuzzy

from everycheese.users.tests.factories import UserFactory

from ..models import Cheese


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3)
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    country = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Cheese
    
@pytest.fixture
def cheese():
    return CheeseFactory()
