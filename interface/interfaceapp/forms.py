from django import forms
from .models import Shop,Complaints


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name', 'cateory', 'description', 'cantact_email', 'cantact_phone', 'address', 'lattitude', 'langitude', 'working_ours', 'payment_methods', 'image']
        
class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['custmoer_name','email','complaint_text']