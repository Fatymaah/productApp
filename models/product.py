from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("product.db")


class Product(Model):

  heading = TextField(default="Good image")
  subtitle = TextField(default="Good image")
  thumbnail_link = CharField(max_length=1000)
  fullimage_link = CharField(max_length=1000)

  class Meta:
        database = db


def initialize():
    try:
       Product.create_table()
    except OperationalError:
        pass
    try:
        Product.create(

          heading="Make-up",
          subtitle="While stocks Last",
          thumbnail_link="static/make-up-1209798_640.jpg",
          fullimage_link="static/make-up-1209798_1920.jpg"
            )
    except IntegrityError:
        pass
    try:
            Product.create(

                
              heading="Full Make-up Kit",
              subtitle="80% Discount",
              thumbnail_link="static/makeup-brush-1761648_640.jpg",
              fullimage_link="static/makeup-brush-1761648_1920.jpg"
            )
    except IntegrityError as e:
        pass                                                                                                                                                                                                          