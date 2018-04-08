from django import forms
from .models import Application, Applicant, Documents

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('FirstName', 'MiddleName', 'LastName', 'DateOfBirth', 'Gender', 'FlatNo', 'State', 'City', 'PlaceOfBirth')

class RegisterApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('FirstName', 'LastName', 'UserName', 'MailId', 'Password', 'PhoneNo')

class LoginApplicantForm(forms.Form):
    username = forms.CharField(label="Enter Mail Id", widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=False)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginAdmin(forms.Form) :
    username = forms.CharField(label="Enter Mail Id", widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=False)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('BirthCertificate', 'AddressProof', 'PaymentReceipt')
    
    
