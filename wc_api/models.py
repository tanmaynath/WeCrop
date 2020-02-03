from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    username = models.CharField(max_length=20, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    company = models.CharField(max_length=40)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    rating = models.FloatField(max_length=3)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Seller(models.Model):
    seller_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    notes = models.TextField(max_length=200)
    website = models.URLField()
    # product_type = models.CharField(max_length=30) ?

    def __str__(self):
        return self.user.username


class Cities(models.Model):
    city_name = models.CharField(max_length=20)
    city_code = models.CharField(max_length=3)

    def __str__(self):
        return self.city_name


class State(models.Model):
    state_name = models.CharField(max_length=20)
    state_code = models.CharField(max_length=3)


class ZipCode(models.Model):
    zip_code = models.IntegerField(max_length=6)
    city = models.ForeignKey(Cities)


class Country(models.Model):
    country_name = models.CharField(max_length=20)
    country_phone_code = models.IntegerField(max_length=3)


class MeasureUnit(models.Model):
    unit = models.CharField(max_length=20)
    unit_acronym = models.CharField(max_length=3)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    street = models.CharField(max_length=50, null=False, blank=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE(), null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE(), null=False, blank=False)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE(), null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE(), null=False, blank=False)


class ProductCategory(models.Model):
    category = models.CharField(max_length=20)
    shelf_life = models.Charfield(max_length=10)


class Product(models.Model):
    # add photo field later #
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE())
    product_name = models.CharField(max_length=30, null=False, blank=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE())
    price = models.FloatField(null=False, blank=False)
    measurement_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE())
    quantity_available = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=150, null=False, blank=False)
    advanced_order = models.BooleanField(default=False)
    tags = models.CharField(max_length=15)

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    buyer = models.OneToOneField(User)
    seller = models.OneToOneField(Seller)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateField(default=None)
    amount = models.FloatField(null=False)
    seller_approval = models.BooleanField(blank=True)
    # invoice_details = models.OneToOneField(Invoice)


class Shipping(models.Model):
    order = models.ForeignKey(Orders)
    shipping_company = models.Charfield()
    shipping_url = models.URLField()
    seller = models.ForeignKey()


class Payment(models.Model):
    PAYMENT_METHODS = [(u'1', 'Paypal'),
                       (u'2', 'Sofort'),
                       (u'3', 'Credit Card')]
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS)
    amount_paid = models.FloatField(null=False, blank=False)
    order = models.OneToOneField(Orders)














