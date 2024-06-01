from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.text import slugify
from django.forms import ModelForm,widgets

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["username"].widget.attrs.update({
                'required':'username is required',
                'aria-label':'Full Name',
                'aria-describedby':'basic-addon1',
                'name':'ComplaintName',
                'id':'Complaint',
                'type':'text',
                'class':'form-control',
                'placeholder':'Enter Your Username'

            })
            self.fields["password"].widget.attrs.update({
                'required':'',
                'name':'form-floating',
                'id':'floatingTextarea',
                'type':'textarea',
                'class':'form-control',
                'placeholder':'Enter Your password'

            })
class RegistrationForm(UserCreationForm):
    fullname=forms.CharField(max_length=100,required=True,label="Full Name")
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["fullname"].widget.attrs.update({
                'required':'full name is required',
                'aria-label':'Full Name',
                'aria-describedby':'basic-addon1',
                'name':'ComplaintName',
                'id':'Complaint',
                'type':'text',
                'class':'form-control',
                'placeholder':'Enter Your Full Name'

            })
            self.fields["username"].widget.attrs.update({
                'required':'',
                'name':'form-floating',
                'id':'floatingTextarea',
                'type':'textarea',
                'class':'form-control',
                'placeholder':'Enter Your Username'

            })
            self.fields["email"].widget.attrs.update({
                'required':'',
                'name':'ComplaintCategory',
                'id':'exampleFormControlInput1',
                'type':'email',
                'class':'form-control',
                'placeholder':'name@example.com'

            })
            self.fields["password1"].widget.attrs.update({
                'required':'',
                'name':'Image',
                'id':'imagee',
                'type':'image',
                'class':'form-control',
                'placeholder':'Enter your password'

            })
            self.fields["password2"].widget.attrs.update({
                'required':'',
                'name':'Image',
                'id':'imagee',
                'type':'image',
                'class':'form-control mb-5',
                'placeholder':'Confirm Your Password'


            })
    class Meta:
        model=User
        fields=['fullname','username','email','password1','password2']

class ComplaintForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["name"].widget.attrs.update({
                'required':'',
                'aria-label':'Complaint Name',
                'aria-describedby':'basic-addon1',
                'name':'ComplaintName',
                'id':'Complaint',
                'type':'text',
                'class':'form-control',
                'placeholder':'Enter your Complaint'

            })
            def as_p(self):
        
                rendered_fields = super().as_p()
                rendered_fields = rendered_fields.replace('ComplaintName', '<i class="fa fa-comment"></i> ComplaintName')
                return rendered_fields
            self.fields["email"].widget.attrs.update({
                'required':'',
                'name':'form-floating',
                'id':'floatingTextarea',
                'type':'textarea',
                'class':'form-control',
                'placeholder':''

            })
            self.fields["description"].widget.attrs.update({
                'required':'',
                'name':'form-floating',
                'id':'floatingTextarea',
                'type':'textarea',
                'class':'form-control',
                'placeholder':''

            })
            self.fields["category"].widget.attrs.update({
                'required':'',
                'name':'ComplaintCategory',
                'id':'inputGroupSelect01',
                'type':'select',
                'class':'form-select',
                'placeholder':'Enter your Complaint'

            })
            self.fields["image"].widget.attrs.update({
                
                'name':'Image',
                'id':'formFile',
                'type':'image',
                'class':'form-control'

            })
    class Meta:
        model = Complaint
        fields = ['name','email', 'description', 'category', 'image']
        
        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)  # Generate slug from the complaint's name
            super().save(*args, **kwargs)
        

      