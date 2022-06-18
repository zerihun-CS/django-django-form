from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
hobbies = ['play football','watch movie','poem','read books']


def view_hobby(request):
   
   return render(request,'view_hobby.html',{'hobby':hobbies})

class NewHobbyForm(forms.Form):
   hobby = forms.CharField(label="add hobby",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'New hobby'}))
def add_hobby(request):
   
   if request.method == 'POST':
      form = NewHobbyForm(request.POST)
      # print(form)
      if form.is_valid():
         hobby  = form.cleaned_data["hobby"]
      
      # hobby= request.POST.get('hobby')
      # print(hobby)
         hobbies.append(hobby)
         print('added')
         return HttpResponseRedirect(reverse("hobby:view_hobby_url"))
      else:
         return render(request,'add_hobby.html',{'form':form})
   else:
      print('not post method')
      return render(request,'add_hobby.html',{'form':NewHobbyForm})
      
      
   return render(request,'add_hobby.html',{'form':NewHobbyForm})
   