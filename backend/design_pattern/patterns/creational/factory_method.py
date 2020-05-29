from django.db import models


class Creator():
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self):
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        product.operation()


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


class ConcreteProduct1(models.Model):
    name = models.CharField(max_length=200)

    def operation(self):
        self.name = "Nguyen Quang Huy"
        self.save()
        print(ConcreteProduct1.objects.all())

    def __str__(self):
        return self.name


class ConcreteProduct2(models.Model):
    def operation(self):
        print("Running ConcreteProduct2 method")


def client_code(creator: Creator):
    """
    The client code works with an instance of a concrete creator,
    albeit through its base interface. As long as the client keeps
    working with the creator via the base interface, you can pass it
    any creator's subclass.
    """

    creator.some_operation()


def main():
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
