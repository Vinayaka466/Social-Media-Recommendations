from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop = models.OneToOneField('Shop',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.shop.shop_name}'

class Shop(models.Model):
    CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('restaurants', 'Restaurants'),
    ('grocery', 'Grocery'),
    ('furniture', 'Furniture'),
    ('beauty', 'Beauty & Personal Care'),
    ('books', 'Books'),
    ('sports', 'Sports Equipment'),
    ('toys', 'Toys & Games'),
    ('automotive', 'Automotive'),
    ('home_appliances', 'Home Appliances'),
    ('jewelry', 'Jewelry'),
    ('healthcare', 'Healthcare'),
    ('pet_supplies', 'Pet Supplies'),
    ('pharmacy', 'Pharmacy'),
    ('toiletries', 'Toiletries'),
    ('kitchenware', 'Kitchenware'),
    ('gardening', 'Gardening'),
    ('flowers', 'Flowers & Plants'),
    ('crafts', 'Crafts & DIY'),
    ('music', 'Musical Instruments'),
    ('office_supplies', 'Office Supplies'),
    ('watches', 'Watches'),
    ('liquor', 'Liquor'),
    ('baby_products', 'Baby Products'),
    ('shoes', 'Shoes'),
    ('bags', 'Bags & Luggage'),
    ('accessories', 'Fashion Accessories'),
    ('hardware', 'Hardware'),
    ('technology', 'Technology'),
    ('gaming', 'Gaming'),
    ('supermarket', 'Supermarket'),
    ('bakery', 'Bakery'),
    ('butcher', 'Butcher'),
    ('fish_market', 'Fish Market'),
    ('frozen_food', 'Frozen Food'),
    ('organic', 'Organic Products'),
    ('dairy', 'Dairy'),
    ('convenience_store', 'Convenience Store'),
    ('cosmetics', 'Cosmetics'),
    ('cell_phones', 'Cell Phones'),
    ('fabrics', 'Fabrics & Textiles'),
    ('cleaning_supplies', 'Cleaning Supplies'),
    ('toys_games', 'Toys & Games'),
    ('frozen_items', 'Frozen Items'),
    ('art', 'Art Supplies'),
    ('bikes', 'Bicycles & Accessories'),
    ('liquor_store', 'Liquor Store'),
    ('gourmet', 'Gourmet Foods'),
    ('specialty_foods', 'Specialty Foods'),
    ('shaving_supplies', 'Shaving Supplies'),
    ('wine', 'Wine & Spirits'),
    ('vape', 'Vape Products'),
    ('craft_beer', 'Craft Beer'),
    ('sunglasses', 'Sunglasses'),
]
    user = models.ForeignKey(User, related_name="Shop", on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    cateory = models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    description = models.TextField()
    cantact_email = models.EmailField()
    cantact_phone = models.CharField(max_length=20)
    address = models.TextField()
    lattitude = models.FloatField()
    langitude = models.FloatField()
    working_ours = models.CharField(max_length=100)
    payment_methods = models.CharField(max_length=10)
    image = models.ImageField(upload_to='shops/images/')
    
    def __str__(self):
        return self.shop_name
    
    @property
    def average_rating(self):
        """calcute avarage ratings"""
        reviews = self.reviews.all()
        if reviews.exists():
            return reviews.aggregate(models.Avg('rating'))['rating_avg']
        return 0
    def get_review_count(self):
        """return the views for the shop"""
        return self.reviews.count()
        
class Review(models.Model):
    shop = models.ForeignKey(Shop, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f' Review by {self.user.username}-{self.shop.shop_name}'
    
    class Meta:
        ordering = ['created_at']
        
class Complaints(models.Model):
    custmoer_name = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    complaint_text = models.TextField()
    
    def __str__(self):
        return self.custmoer_name
        
        
