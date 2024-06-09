from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Saints_Model,Provinical_Administration,GalleryModel
from .models import News_Category,Latest_News_Model,Event_Details,EnquiryModel,FriarsModel,Obituary_Model,Provincial_administation,Telengana_delegation,Kolkata_Mission,Srilankan_Mission,Wishes,About_Model,VideoGallery,NoticeModel
from .forms import Saints_Form,Provinical_Administration_Form,News_Category_Form,News_Form,GalleryForm,Event_Details_Form,EnquiryForm,FriarsForm,Obituary_Form,Provincial_Form,Telengana_delegation_Form,Kolkata_Mission_Form,Srilankan_Mission_Form,Wishes_Form,About_Form,VideoGalleryForm,NoticeForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.db import transaction
# Create your views here.



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again....")
            print("Invalid login attempt")  # Debug print
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_pages/admin_dashboard.html')
    else:
        return redirect('user_login')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')


def index(request):  
    current_date = timezone.now().date()
    saints = Saints_Model.objects.filter(date__date=current_date)
    active_events = Event_Details.objects.filter(end_date__gte=timezone.now())
    news = News_Category.objects.filter(status=0) 
    gallery = GalleryModel.objects.all()
    about = About_Model.objects.order_by('-id').first()
    context = {'saints':saints,
               'active_events':active_events,
               'news':news,
               'gallery':gallery,
               'about':about,               
               }
    return render(request,'index.html',context)


@login_required(login_url='user_login')
def admin_add_friars(request):
    if request.method == 'POST':
        form = FriarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('friars_view') 
    else:
        form = FriarsForm()
    return render(request, 'admin_pages/admin_add_friars.html', {'form': form})

@login_required(login_url='user_login')
def friars_view(request):
    friars = FriarsModel.objects.all().order_by('-id')
    return render(request,'admin_pages/friars_view.html',{'friars':friars})

@login_required(login_url='user_login')
def update_friars(request, pk):
    friars = get_object_or_404(FriarsModel, pk=pk)

    if request.method == 'POST':
        form = FriarsForm(request.POST, request.FILES, instance=friars)
        if form.is_valid():
            form.save()
            return redirect('friars_view')
    else:
        form = FriarsForm(instance=friars)

    return render(request, 'admin_pages/update_friars.html', {'form': form,'friars':friars})

@login_required(login_url='user_login')
def delete_friars(request,pk):
    friars = FriarsModel.objects.get(pk=pk)
    friars.delete()
    return redirect('friars_view')

@login_required(login_url='user_login')
def add_provincial_administaration(request):
    if request.method == 'POST':
        form = Provincial_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_provincial_administration') 
    else:
        form = Provincial_Form()
    return render(request, 'admin_pages/add_provincial_administaration.html', {'form': form})

@login_required(login_url='user_login')
def view_provincial_administration(request):
    province = Provincial_administation.objects.all().order_by('-id')
    return render(request,'admin_pages/view_provincial_administration.html',{'province':province})


@login_required(login_url='user_login')
def update_provincial_administration(request, pk):
    province = get_object_or_404(Provincial_administation, pk=pk)

    if request.method == 'POST':
        form = Provincial_Form(request.POST, request.FILES, instance=province)
        if form.is_valid():
            form.save()
            return redirect('view_provincial_administration')
    else:
        form = Provincial_Form(instance=province)

    return render(request, 'admin_pages/update_provincial_administration.html', {'form': form,'province':province})


@login_required(login_url='user_login')
def delete_provincial_administration(request,pk):
    province = Provincial_administation.objects.get(pk=pk)
    province.delete()
    return redirect('view_provincial_administration')


@login_required(login_url='user_login')
def add_telegana_delegation(request):
    if request.method == 'POST':
        form = Telengana_delegation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_telengana_delegation') 
    else:
        form = Telengana_delegation_Form()
    return render(request, 'admin_pages/add_telegana_delegation.html', {'form': form})


@login_required(login_url='user_login')
def view_telengana_delegation(request):
    telengana = Telengana_delegation.objects.all().order_by('-id')
    return render(request,'admin_pages/view_telengana_delegation.html',{'telengana':telengana})

@login_required(login_url='user_login')
def update_telengana_delegation(request, pk):
    telengana = get_object_or_404(Telengana_delegation, pk=pk)

    if request.method == 'POST':
        form = Telengana_delegation_Form(request.POST, request.FILES, instance=telengana)
        if form.is_valid():
            form.save()
            return redirect('view_telengana_delegation')
    else:
        form = Telengana_delegation_Form(instance=telengana)

    return render(request, 'admin_pages/update_telengana_delegation.html', {'form': form,'telengana':telengana})


@login_required(login_url='user_login')
def delete_telengana_delegation(request,pk):
    telengana = Telengana_delegation.objects.get(pk=pk)
    telengana.delete()
    return redirect('view_telengana_delegation')


@login_required(login_url='user_login')
def add_kolkata_mission(request):
    if request.method == 'POST':
        form = Kolkata_Mission_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_kolkata_mission') 
    else:
        form = Kolkata_Mission_Form()
    return render(request, 'admin_pages/add_kolkata_mission.html', {'form': form})


@login_required(login_url='user_login')
def view_kolkata_mission(request):
    kolkata_mission = Kolkata_Mission.objects.all().order_by('-id')
    return render(request,'admin_pages/view_kolkata_mission.html',{'kolkata_mission':kolkata_mission})

@login_required(login_url='user_login')
def update_kolkata_mission(request, pk):
    kolkata_mission = get_object_or_404(Kolkata_Mission, pk=pk)

    if request.method == 'POST':
        form = Kolkata_Mission_Form(request.POST, request.FILES, instance=kolkata_mission)
        if form.is_valid():
            form.save()
            return redirect('view_kolkata_mission')
    else:
        form = Kolkata_Mission_Form(instance=kolkata_mission)

    return render(request, 'admin_pages/update_kolkata_mission.html', {'form': form,'kolkata_mission':kolkata_mission})


@login_required(login_url='user_login')
def delete_kolkata_mission(request,pk):
    kolkata_mission = Kolkata_Mission.objects.get(pk=pk)
    kolkata_mission.delete()
    return redirect('view_kolkata_mission')


@login_required(login_url='user_login')
def add_srilankan_mission(request):
    if request.method == 'POST':
        form = Srilankan_Mission_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_srilankan_mission') 
    else:
        form = Srilankan_Mission_Form()
    return render(request, 'admin_pages/add_srilankan_mission.html', {'form': form})


@login_required(login_url='user_login')
def view_srilankan_mission(request):
    srilankan_mission = Srilankan_Mission.objects.all().order_by('-id')
    return render(request,'admin_pages/view_srilankan_mission.html',{'srilankan_mission':srilankan_mission})


@login_required(login_url='user_login')
def update_srilankan_mission(request, pk):
    srilankan_mission = get_object_or_404(Srilankan_Mission, pk=pk)

    if request.method == 'POST':
        form = Srilankan_Mission_Form(request.POST, request.FILES, instance=srilankan_mission)
        if form.is_valid():
            form.save()
            return redirect('view_srilankan_mission')
    else:
        form = Srilankan_Mission_Form(instance=srilankan_mission)

    return render(request, 'admin_pages/update_srilankan_mission.html', {'form': form,'srilankan_mission':srilankan_mission})


@login_required(login_url='user_login')
def delete_srilankan_mission(request,pk):
    srilankan_mission = Srilankan_Mission.objects.get(pk=pk)
    srilankan_mission.delete()
    return redirect('view_srilankan_mission')



@login_required(login_url='user_login')
def add_saints(request):
    if request.method == 'POST':
        form = Saints_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_saints') 
    else:
        form = Saints_Form()

    return render(request, 'admin_pages/add_saints.html', {'form': form})


@login_required(login_url='user_login')
def view_saints(request):
    saints = Saints_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_saints.html', {'saints': saints})


@login_required(login_url='user_login')
def update_saints(request,id):
    saints = get_object_or_404(Saints_Model, id=id)
    if request.method == 'POST':
        form = Saints_Form(request.POST, request.FILES, instance=saints)
        if form.is_valid():
            form.save()
            return redirect('view_saints')
    else:
        form = Saints_Form(instance=saints)
    return render(request, 'admin_pages/update_saints.html', {'form': form, 'saints': saints})


@login_required(login_url='user_login')
def delete_saints(request,id):
    saints = Saints_Model.objects.get(id=id)
    saints.delete()
    return redirect('view_saints')


@login_required(login_url='user_login')
def admin_add_obituary(request):
    if request.method == 'POST':
        form = Obituary_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('obituary_view') 
    else:
        form = Obituary_Form()

    return render(request, 'admin_pages/add_obituary.html', {'form': form})


@login_required(login_url='user_login')
def obituary_view(request):
    obituary = Obituary_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_obituary.html', {'obituary': obituary})


@login_required(login_url='user_login')
def update_obituary(request,id):
    obituary = get_object_or_404(Obituary_Model, id=id)
    if request.method == 'POST':
        form = Obituary_Form(request.POST, request.FILES, instance=obituary)
        if form.is_valid():
            form.save()
            return redirect('obituary_view')
    else:
        form = Obituary_Form(instance=obituary)
    return render(request, 'admin_pages/update_obituary.html', {'form': form, 'obituary': obituary})

@login_required(login_url='user_login')
def add_wishes(request):
    if request.method == 'POST':
        form = Wishes_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wishes_view') 
    else:
        form = Wishes_Form()
    return render(request, 'admin_pages/add_wishes.html', {'form': form})


@login_required(login_url='user_login')
def wishes_view(request):
    wishes = Wishes.objects.all().order_by('-id')
    return render(request, 'admin_pages/wishes_view.html', {'wishes': wishes})

@login_required(login_url='user_login')
def update_wishes(request,id):
    wishes = get_object_or_404(Wishes, id=id)
    if request.method == 'POST':
        form = Wishes_Form(request.POST, request.FILES, instance=wishes)
        if form.is_valid():
            form.save()
            return redirect('wishes_view')
    else:
        form = Wishes_Form(instance=wishes)
    return render(request, 'admin_pages/update_wishes.html', {'form': form, 'wishes': wishes})

@login_required(login_url='user_login')
def delete_wishes(request,id):
    wishes = Wishes.objects.get(id=id)
    wishes.delete()
    return redirect('wishes_view')

@login_required(login_url='user_login')
def event_details(request, event_name):
    events = Event_Details.objects.get(event_name=event_name)
    return render(request, 'event_details.html', {'events':events})



@login_required(login_url='user_login')
def delete_obituary(request,id):
    obituary = Obituary_Model.objects.get(id=id)
    obituary.delete()
    return redirect('obituary_view')


@login_required(login_url='user_login')
def admin_add_Provinical_Administration(request):
    if request.method == 'POST':
        form = Provinical_Administration_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_Provinical_Administration') 
    else:
        form = Provinical_Administration_Form()

    return render(request, 'admin_pages/admin_add_Provinical_Administration.html', {'form': form})


@login_required(login_url='user_login')
def admin_view_Provinical_Administration(request):
    administration = Provinical_Administration.objects.all().order_by('-id')
    return render(request, 'admin_pages/admin_view_Provinical_Administration.html', {'administration': administration})


@login_required(login_url='user_login')
def admin_update_Provinical_Administration(request,id):
    administration = get_object_or_404(Provinical_Administration, id=id)
    if request.method == 'POST':
        form = Provinical_Administration_Form(request.POST, instance=administration)
        if form.is_valid():
            form.save()
            return redirect('admin_view_Provinical_Administration')
    else:
        form = Provinical_Administration_Form(instance=administration)
    return render(request, 'admin_pages/admin_update_Provinical_Administration.html', {'form': form, 'administration': administration})


@login_required(login_url='user_login')
def admin_delete_Provinical_Administration(request,id):
    administration = Provinical_Administration.objects.get(id=id)
    administration.delete()
    return redirect('admin_view_Provinical_Administration')

# admin latest news start

@login_required(login_url='user_login')
def admin_add_news_category(request):
    if request.method == 'POST':
        form = News_Category_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_add_latest_news') 
    else:
        form = News_Category_Form()

    return render(request, 'admin_pages/admin_add_news_category.html', {'form': form})


@login_required(login_url='user_login')
def admin_view_category(request):
    category = News_Category.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_category.html',{'category':category})


@login_required(login_url='user_login')
def admin_update_news_category(request,id):
    category = get_object_or_404(News_Category, id=id)
    if request.method == 'POST':
        form = News_Category_Form(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_view_category')
    else:
        form = News_Category_Form(instance=category)
    return render(request, 'admin_pages/admin_update_news_category.html', {'form': form, 'category': category})


@login_required(login_url='user_login')
def admin_delete_news_category(request,id):
    category = News_Category.objects.get(id=id)
    category.delete()
    return redirect('admin_view_category')


@login_required(login_url='user_login')
def admin_add_latest_news(request):
    if request.method == 'POST':
        news_details = News_Form(request.POST, request.FILES)
        if news_details.is_valid():
            news_details.save()
        
            return redirect('admin_view_latest_news')  
    else:
        news_details = News_Form()
    categories = News_Category.objects.all() 
    return render(request, 'admin_pages/admin_add_latest_news.html', {'news_details': news_details,'categories':categories})


@login_required(login_url='user_login')
def admin_view_latest_news(request):
    news = Latest_News_Model.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_latest_news.html',{'news':news})


@login_required(login_url='user_login')
def admin_update_latest_news(request, id):
    news = get_object_or_404(Latest_News_Model, id=id)
    categories = News_Category.objects.all()  

    if request.method == 'POST':
        form = News_Form(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('admin_view_latest_news')
    else:
        form = News_Form(instance=news)

    return render(request, 'admin_pages/admin_update_latest_news.html', {'form': form, 'news': news, 'categories': categories})

@login_required(login_url='user_login')
def admin_delete_latest_news(request,id):
    news = Latest_News_Model.objects.get(id=id)
    news.delete()
    return redirect('admin_view_latest_news')

@login_required(login_url='user_login')
def admin_add_event_category(request):
    if request.method == 'POST':
        form = Event_Categoty_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_event_category') 
    else:
        form = Event_Categoty_Form()
    return render(request, 'admin_pages/admin_add_event_category.html', {'form': form})


@login_required(login_url='user_login')
def admin_view_event_category(request):
    event = Event_Categoty.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_event_category.html',{'event':event})


@login_required(login_url='user_login')
def admin_update_event_category(request,id):
    event = get_object_or_404(Event_Categoty, id=id)
    if request.method == 'POST':
        form = Event_Categoty_Form(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin_view_event_category')
    else:
        form = Event_Categoty_Form(instance=event)
    return render(request, 'admin_pages/admin_update_event_category.html', {'form': form, 'event': event})


@login_required(login_url='user_login')
def admin_delete_event_category(request,id):
    event = Event_Categoty.objects.get(id=id)
    event.delete()
    return redirect('admin_view_event_category')

@login_required(login_url='user_login')
def admin_add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery_view') 
    else:
        form = GalleryForm()

    return render(request, 'admin_pages/admin_add_gallery.html', {'form': form})


@login_required(login_url='user_login')
def admin_gallery_view(request):
    gallery = GalleryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_gallery_view.html',{'gallery':gallery})


@login_required(login_url='user_login')
def admin_update_gallery(request, id):
    gallery = get_object_or_404(GalleryModel, id=id)

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery_view')
    else:
        form = GalleryForm(instance=gallery)

    return render(request, 'admin_pages/admin_update_gallery.html', {'form': form,'gallery':gallery})


@login_required(login_url='user_login')
def admin_delete_gallery(request,id):
    gallery = GalleryModel.objects.get(id=id)
    gallery.delete()
    return redirect('admin_gallery_view')


@login_required(login_url='user_login')
def admin_add_events(request):
    if request.method == 'POST':
        form = Event_Details_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_events') 
    else:
        form = Event_Details_Form()
    return render(request, 'admin_pages/admin_add_events.html', {'form': form})


@login_required(login_url='user_login')
def admin_view_events(request):
    event = Event_Details.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_events.html',{'event':event})


@login_required(login_url='user_login')
def admin_update_events(request,id):
    events = get_object_or_404(Event_Details, id=id)
    if request.method == 'POST':
        form = Event_Details_Form(request.POST, request.FILES, instance=events)
        if form.is_valid():
            form.save()
            return redirect('admin_view_events')
    else:
        form = Event_Details_Form(instance=events)
    return render(request, 'admin_pages/admin_update_events.html', {'form': form, 'events': events})


@login_required(login_url='user_login')
def admin_delete_events(request,id):
    events = Event_Details.objects.get(id=id)
    events.delete()
    return redirect('admin_view_events')

@login_required(login_url='user_login')
def add_about_video(request):
    if request.method == 'POST':
        form = About_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_video') 
    else:
        form = About_Form()
    return render(request, 'admin_pages/add_about_video.html', {'form': form})

@login_required(login_url='user_login')
def admin_view_video(request):
    about = About_Model.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_video.html',{'about':about})  


@login_required(login_url='user_login')
def update_video_link(request,id):
    about = get_object_or_404(About_Model, id=id)
    if request.method == 'POST':
        form = About_Form(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('admin_view_video')
    else:
        form = About_Form(instance=about)
    return render(request, 'admin_pages/update_video_link.html', {'form': form, 'about': about})


@login_required(login_url='user_login')
def delete_video(request,id):
    about = About_Model.objects.get(id=id)
    about.delete()
    return redirect('admin_view_video')

@login_required(login_url='user_login')
def add_video_gallery(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_video_gallery')
        else:
            # Add this line to see form errors
            print(form.errors)
    else:
        form = VideoGalleryForm()
    return render(request, 'admin_pages/add_video_gallery.html', {'form': form})


@login_required(login_url='user_login')
def view_video_gallery(request):
    video_link = VideoGallery.objects.all().order_by('-id')
    return render(request,'admin_pages/view_video_gallery.html',{'video_link':video_link}) 

@login_required(login_url='user_login')
def update_video_gallery(request,id):
    video_link = get_object_or_404(VideoGallery, id=id)
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES, instance=video_link)
        if form.is_valid():
            form.save()
            return redirect('view_video_gallery')
    else:
        form = VideoGalleryForm(instance=video_link)
    return render(request, 'admin_pages/update_video_gallery.html', {'form': form, 'video_link': video_link})

@login_required(login_url='user_login')
def delete_video_gallery(request,id):
    video_link = VideoGallery.objects.get(id=id)
    video_link.delete()
    return redirect('view_video_gallery')

@login_required(login_url='user_login')
def admin_view_comments(request):
    comments = EnquiryModel.objects.all()
    return render(request,'admin_pages/admin_view_comments.html',{'comments':comments})

@login_required(login_url='user_login')
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_notice') 
    else:
        form = NoticeForm()
    return render(request, 'admin_pages/add_notice.html', {'form': form})


@login_required(login_url='user_login')
def view_notice(request):
    notice = NoticeModel.objects.all().order_by('-id')
    return render(request,'admin_pages/view_notice.html',{'notice':notice})

@login_required(login_url='user_login')
def update_notice(request,id):
    notice = get_object_or_404(NoticeModel, id=id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('view_notice')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'admin_pages/update_notice.html', {'form': form, 'notice': notice})

@login_required(login_url='user_login')
def delete_notice(request,id):
    notice = NoticeModel.objects.get(id=id)
    notice.delete()
    return redirect('view_notice')


def st_francis_of_assisi(request):
    context={      
    }
    return render(request,'about_us/st_francis_of_assisi.html',context)

def conventuals_in_india(requset):
    return render(requset,'about_us/conventuals_in_india.html')

def conventual_charism(requset):
    return render(requset,'about_us/conventual_charism.html')

def history_of_the_order(request):
    return render(request,'about_us/history_of_the_order.html')

def st_maximilian_kolbe(request):
    return render(request,'about_us/st_maximilian_kolbe.html')

def franciscan_saints(request):
    return render(request,'about_us/franciscan_saints.html')

# Administration start

def provinical_administration(request):
    provinical = Provincial_administation.objects.all()
    return render(request,'administration/provinical_administration.html',{'provinical':provinical})

def ap_telengana_delegation(request):
    telengana = Telengana_delegation.objects.all()
    return render(request,'administration/ap_telengana_delegation.html',{'telengana':telengana})

def kolkata_mission(request):
    kolkata = Kolkata_Mission.objects.all()
    return render(request,'administration/kolkata_mission.html',{'kolkata':kolkata})

def sri_lankan_mission(request):
    srilankan_mission = Srilankan_Mission.objects.all()
    return render(request,'administration/sri_lankan_mission.html',{'srilankan_mission':srilankan_mission})


#vocation start

def vocation_1(request):
    return render(request,'vocation/vocation-1.html')


def vocation_2(request):
    return render(request,'vocation/vocation-2.html')

# FRIARIES KERALA start

def Assisi_shanthi_kendra(request):
    context={
    }
    return render(request,'friaries/Assisi_shanthi_kendra.html',context)

def Kolbe_Franciscan_Ashram(request):
    return render(request,'friaries/Kolbe_Franciscan_Ashram.html')

def Nirmalaram_Franciscan_Ashram(request):
    return render(request,'friaries/Nirmalaram_Franciscan_Ashram.html')

def Padua_Franciscan_Ashram(request):
    return render(request,'friaries/Padua_Franciscan_Ashram.html')

def Franciscan_Ashram(request):
    return render(request,'friaries/Franciscan_Ashram.html')

def St_Paul_Franciscan_Ashram(request):
    return render(request,'friaries/St_Paul_Franciscan_Ashram.html')

# FRIARIES  ANDRA start

def St_Maximilian_Franciscan_Ashram(request):
    return render(request,'friaries/St_Maximilian_Franciscan_Ashram.html')

def Bala_Yesu_Franciscan_Ashram(request):
    return render(request,'friaries/Bala_Yesu_Franciscan_Ashram.html')

def San_Cupertino_Franciscan_Ashram(request):
    return render(request,'friaries/San_Cupertino_Franciscan_Ashram.html')

# FRIARIES  KOLKATTA start

def St_Francis_Friary(request):
    return render(request,'friaries/St_Francis_Friary.html')

# FRIARIES  TELEGANA start
def St_Peter_Franciscan_Ashram(request):
    return render(request,'friaries/St_Peter_Franciscan_Ashram.html')

def Assisi_FranciscanAshram(request):
    return render(request,'friaries/Assisi_FranciscanAshram.html')

def St_Anthony_Franciscan_Ashram(request):
    return render(request,'friaries/St_Anthony_Franciscan_Ashram.html')

# FRIARIES  TAMIL NADU start
def Assisi_Snehalaya(request):
    return render(request,'friaries/Assisi_Snehalaya.html')

def Belvedere_Franciscan_Ashram(request):
    return render(request,'friaries/Belvedere_Franciscan_Ashram.html')

# FRIARIES SRI LANKA start

def Padre_Pio_Shrine(request):
    return render(request,'friaries/Padre_Pio_Shrine.html')

def Ave_Maria_Franciscan_Friary(request):
    return render(request,'friaries/Ave_Maria_Franciscan_Friary.html')

def St_Joseph_Vaz_Friary(request):
    return render(request,'friaries/St_Joseph_Vaz_Friary.html')

def St_Anthony_Friary(request):
    return render(request,'friaries/St_Anthony_Friary.html')

def St_FrancisFriary(request):
    return render(request,'friaries/St_FrancisFriary.html')


# MINISTRIS START

def Vocation_And_Formation_Apostolate(request):
    return render(request,'ministries/Vocation_And_Formation_Apostolate.html')

def OFS(request):
    return render(request,'ministries/OFS.html')

def Militia_Of_The_Immaculata(request):
    return render(request,'ministries/Militia_Of_The_Immaculata.html')

def FCPD(request):
    return render(request,'ministries/FCPD.html')

def Franciscan_Centre(request):
    return render(request,'ministries/Franciscan_Centre.html')

# MINISTRIES MERIA AND COMMUNICATIONS START

def Gray_Friars_Publications(request):
    return render(request,'ministries/Gray_Friars_Publications.html')

def Kolbe_Communications(request):
    return render(request,'ministries/Kolbe_Communications.html')

# PREACHING AND RECONCILING APOSTOLATE

def Franiscan_Reconciliation_Retreat(request):
    return render(request,'ministries/Franiscan_Reconciliation_Retreat.html')

def Retreat_Centers(request):
    return render(request,'ministries/Retreat_Centers.html')

def Tuesday_Devotions(request):
    return render(request,'ministries/Tuesday_Devotions.html')

# MINISTRIES SOCIAL APOSTOLATE START

def Social_Apostolate(request):
    return render(request,'ministries/Social_Apostolate.html')

# ministries EDUCATION APOSTOLATE start

def Greyfriars_Degree_College(request):
    return render(request,'ministries/Greyfriars_Degree_College.html')

def Greyfriars_Junior_College(request):
    return render(request,'ministries/Greyfriars_Junior_College.html')

def Oxford_Creativity_School(request):
    return render(request,'ministries/Oxford_Creativity_School.html')

def St_Anthony_School(request):
    return render(request,'ministries/St_Anthony_School.html')

def St_Peter_School(request):
    return render(request,'ministries/St_Peter_School.html')

def Vidyaniketan_Junior_College(request):
    return render(request,'ministries/Vidyaniketan_Junior_College.html')

def St_Padre_Pio_Shrine(request):
    return render(request,'ministries/St_Padre_Pio_Shrine.html')

def St_Maximilian_Kolbe_Church(request):
    return render(request,'ministries/St_Maximilian_Kolbe_Church.html')

def Bala_Yesu_Shrine(request):
    return render(request,'ministries/Bala_Yesu_Shrine.html')

def Green_Park_Pastoral_Community(request):
    return render(request,'ministries/Green_Park_Pastoral_Community.html')

def St_Francis_Of_Assisi_Church(request):
    return render(request,'ministries/St_Francis_Of_Assisi_Church.html')

# SET UP OF THE PROVINCE start

def Friars(request):
    friars = FriarsModel.objects.all()
    return render(request,'set_up_of_the_province/friars.html',{'friars':friars})

def wish(request):
    # Delete wishes uploaded on the previous day
    yesterday = timezone.now() - timedelta(days=1)
    Wishes.objects.filter(uploaded_at__date=yesterday.date()).delete()

    # Retrieve wishes and render the template
    wishes = Wishes.objects.all()
    return render(request, 'wish.html', {'wishes': wishes})


def Events(request):
    events = Event_Details.objects.filter(end_date__gte=timezone.now())
    return render(request,'events.html', {'events':events})


def news_details(request,news_heading):
    news = News_Category.objects.all()
    if(News_Category.objects.filter(news_heading=news_heading, status=0)):
        news_details = Latest_News_Model.objects.filter(category__news_heading=news_heading)
        category_name = News_Category.objects.filter(news_heading=news_heading).first()
        context = {'news_details': news_details,'category_name':category_name,'news':news}
        return render(request,"news_details.html",context)
    else:
        messages.warning(request,"No such category found")
    return render(request,'news_details.html')


def friends_of_smk(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('Comment Submitted Successfully!!!!!')  
            messages.success(request, 'Comment Submitted Successfully!!!!!')
    else:
        form = EnquiryForm()
    return render(request,'friends_of_smk.html',{'form':form})

def gallery(request):
    gallery = GalleryModel.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})


def video_gallery(request):
    video_links = VideoGallery.objects.order_by('-id')  # Corrected the query
    return render(request, 'video_gallery.html', {'video_links': video_links})


def event_details(request, id):
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Events')  
    else:
        form = EnquiryForm()
    events = Event_Details.objects.get(id=id)
    return render(request, 'event_details.html', {'form':form,'events': events})

def Obituary(request):
    obituary = Obituary_Model.objects.all()
    return render(request,'obituary.html',{'obituary':obituary})


def admin_delete_comments(request,id):
    comments = EnquiryModel.objects.get(id=id)
    comments.delete()
    return redirect('admin_view_comments')

def event(request):
    data = Event_Details.objects.all()
    return render(request,'event.html',{'data':data})

def admin_calendar(request):
    return render(request,'admin_pages/calendar.html')

# def calendar(request):
#     return render(request,'calendar.html')

# def test(request):
#     return render(request,'test.html')

# def new(request):
#     return render(request,'new.html')

# def header(request):
#     return render(request,'header.html')

# def slide(request):
#     return render(request,'slider.html')

# def test(request):
#     return render(request,'test.html')

# def index5(request):
#     return render(request,'index5.html')



def wishes(request):
    one_day_ago = timezone.now() - timedelta(days=1)
    Wishes.objects.filter(uploaded_at__lt=one_day_ago).delete()
    wishes = Wishes.objects.filter(uploaded_at__gte=one_day_ago)
    return render(request, 'wishes.html', {'wishes': wishes})

def notice(request):
    notice = NoticeModel.objects.all()
    return render(request,'notice.html',{'notice':notice})

def notice_details(request,heading):
    notice = NoticeModel.objects.get(heading=heading)
    return render(request, 'notice_details.html', {'notice':notice})

