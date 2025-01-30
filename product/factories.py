import factory

from product.models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True

    title = factory.Faker('word')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if isinstance(extracted, (list, tuple)):
            for cat in extracted:
                self.category.add(cat)
        else:
            self.category.add(extracted)