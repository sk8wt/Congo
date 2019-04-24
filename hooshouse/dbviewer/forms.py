from django import forms

class apt_form(forms.Form):
    address = forms.CharField(label = 'Building Address')
    units = forms.IntegerField()
    name = forms.CharField(label = 'Building Name')
    year = forms.CharField(label = 'Year Constructed')

class unit_form(forms.Form):
    # address = forms.CharField(label = 'Building Address')
    # apt_number = forms.IntegerField()
    YES_NO = (('yes', 'yes'), ('no', 'no'))
    occupied = forms.ChoiceField(widget=forms.Select(),choices=YES_NO)
    furnished = forms.ChoiceField(widget=forms.Select(), choices =YES_NO)
    sq_footage = forms.IntegerField()
    num_bathrooms = forms.IntegerField()
    num_bedrooms = forms.IntegerField()
    internet = forms.ChoiceField(widget=forms.Select(),choices=YES_NO)
    laundry = forms.ChoiceField(widget=forms.Select(),choices=YES_NO)
    kitchen = forms.ChoiceField(widget=forms.Select(),choices=YES_NO)
class maintains_form(forms.Form):
    #company_name = forms.CharField()
    #office_address = forms.CharField()
    phone_number = forms.CharField()
    email_address = forms.CharField()
    #apt_address = forms.CharField()
class lease_form(forms.Form):
    computing_id = forms.CharField()
    apt_address = forms.CharField()
    apt_number = forms.CharField()
    rent_amount = forms.CharField()
    term = forms.CharField()

class tenant_form(forms.Form):
    computing_id = forms.CharField()
    name = forms.CharField()
    perm_address = forms.CharField()
    current_address = forms.CharField()
    #phone_number = forms.CharField()
    email = forms.CharField()
