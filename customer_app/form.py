from django import forms

from customer_app.models import Customer


class Customerform(forms.ModelForm):
    
    class Meta:
        model=Customer
        
        fields=["name","address","contactNumber","emailId"]
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
           
            # Add more fields and their classes as needed
        }
        
    def clean_contactNumber(self):
            print("celadsifn phone")
            phone=self.cleaned_data['contactNumber']
            if not phone.isdigit() or len(phone) != 10:
                print("error")
                raise forms.ValidationError("phonenumber should be 10 digiti")
            return phone