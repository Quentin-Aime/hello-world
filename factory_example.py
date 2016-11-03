# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import factory
import factory.fuzzy #import du random de factory
# import model_1

class Model_1Factory(factory.django.DjangoModelFactory):
  class Meta:
    model = model_1

   # use factory.SubFactory(other_factory) for foreignkey one to one
   # use factory.fuzzy.fuzzy_fct or factory.Faker('faker_fct') for random attributes
   
   # use post_generation for foreign key many_to_many
   #    @factory.post_generation
   # def variables(self, create, extracted, **kwargs):
   #     if not create:
   #         return
   #     if extracted:
   #         for variable in extracted:
   #             self.variables.add(variable)

  # use lazy_attribute if you wanna attribute a variable through a fct
  #    @factory.lazy_attribute
  #  def variable(self):
  #      ...
  #      variable = ...
  #      ....
  #      return next(variable)
