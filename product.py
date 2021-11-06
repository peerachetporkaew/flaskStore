from peewee import *
import fire
import uuid

db = SqliteDatabase('product.db')

class Product(Model):
    id        = UUIDField(primary_key=True) #Required for Peewee
    productid = CharField()
    name      = CharField()
    price     = FloatField()

    class Meta:
        database = db


def create():
    db.connect()
    db.create_tables([Product])
    db.close()


def addItem():
    db.connect()
    iphone13 = Product(id=uuid.uuid4(), productid="0001",name="IPhone 13", price=32000)
    iphone13.save(force_insert=True)
    db.close()


def addProduct_1():
    db.connect()
    id = input("Product ID : ")
    name = input("Product Name : ")
    price = float(input("Product Price : "))
    product = Product(id=uuid.uuid4(), productid=id,name=name, price=price)
    product.save(force_insert=True)
    db.close()

def addProduct(id,name,price):
    db.connect()
    product = Product(id=uuid.uuid4(), productid=id,name=name, price=price)
    product.save(force_insert=True)
    db.close()

class CMDHelper:

    def create(self):
        create()

    def add(self,id,name,price):
        addProduct(id,name,price)


if __name__ == "__main__":
    fire.Fire(CMDHelper)

