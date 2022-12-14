import pytest
from django.urls import reverse, resolve 
from .factories import cheese

pytestmark = pytest.mark.django_db

def test_list_reverse():
    """ cheeses:list should reverse to /cheeses/ """
    assert reverse('cheeses:list') == '/cheeses/'

def test_list_resolve():
    """ /cheeses/ should resolve to cheeses:list """
    assert resolve('/cheeses/').view_name == 'cheeses:list'

def test_add_reverse():
    """ cheeses:add should reverse to /cheeses/add/ """
    assert reverse('cheeses:add') == '/cheeses/add/'

def test_add_resolve():
    """ /cheese/add/ should resolve to cheeses:add """
    assert resolve('/cheeses/add/').view_name == 'cheeses:add'

def test_details_reverse(cheese):
    """ cheese:detail should reverse to /cheeses/cheeseslug """
    assert reverse('cheeses:detail', kwargs={"slug": cheese.slug}) == f'/cheeses/{cheese.slug}/'

def test_details_resolve(cheese):
    """ /cheeses/cheeseslug/ should resolve to cheeses:detail """
    url = f'/cheeses/{cheese.slug}/'
    assert resolve(url).view_name == 'cheeses:detail'

