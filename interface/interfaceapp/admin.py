from django.contrib import admin
from.models import Shop,Review,Owner,Complaints
# Register your models here.

"""allow add  review inline in admin page """
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    
class ShopAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ('id' , 'shop_name','cateory','description','cantact_email','cantact_phone','address','lattitude','langitude','working_ours','payment_methods','image')


admin.site.register(Shop,ShopAdmin)
admin.site.register(Review)
admin.site.register(Complaints)