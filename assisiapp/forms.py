from django import forms
from .models import Provinical_Administration,Event_Details
from .models import News_Category,Latest_News_Model,Event_Details
from .models import EnquiryModel,Wishes
from .models import GalleryModel,FriarsModel,Obituary_Model,Provincial_administation,Telengana_delegation,Kolkata_Mission,Srilankan_Mission,Saints_Model,About_Model,VideoGallery,NoticeModel

class Saints_Form(forms.ModelForm):
    class Meta:
        model = Saints_Model
        fields = '__all__'

class Event_Details_Form(forms.ModelForm):
    class Meta:
        model = Event_Details
        fields = '__all__'

class Provinical_Administration_Form(forms.ModelForm):
    class Meta:
        model = Provinical_Administration
        fields = '__all__'


class News_Category_Form(forms.ModelForm):
    class Meta:
        model = News_Category
        fields = '__all__'

class News_Form(forms.ModelForm):
    class Meta:
        model = Latest_News_Model
        fields = ['category','heading','description','news_images','date','status']

# class Event_Categoty_Form(forms.ModelForm):
#     class Meta:
#         model = Event_Categoty
#         fields = '__all__'

# class Event_Form(forms.ModelForm):
#     class Meta:
#         model = Event_Model
#         fields = '__all__'

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryModel
        fields = '__all__'

class FriarsForm(forms.ModelForm):
    class Meta:
        model = FriarsModel
        fields = '__all__'


class Obituary_Form(forms.ModelForm):
    class Meta:
        model = Obituary_Model
        fields = '__all__'

class Wishes_Form(forms.ModelForm):
    class Meta:
        model = Wishes
        fields = '__all__'

class Provincial_Form(forms.ModelForm):
    class Meta:
        model = Provincial_administation
        fields = '__all__'

class Telengana_delegation_Form(forms.ModelForm):
    class Meta:
        model = Telengana_delegation
        fields = '__all__'


class Kolkata_Mission_Form(forms.ModelForm):
    class Meta:
        model = Kolkata_Mission
        fields = '__all__'
    
class Srilankan_Mission_Form(forms.ModelForm):
    class Meta:
        model = Srilankan_Mission
        fields = '__all__'

class About_Form(forms.ModelForm):
    class Meta:
        model = About_Model
        fields = '__all__'
        
class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeModel
        fields = '__all__'