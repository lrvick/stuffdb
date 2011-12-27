from django import forms
from main.models import Domain, Thing, Tag

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ('date_created','date_modified','barcode','domain','attachments','slug','short_url')
    def __init__(self, *args, **kwargs):
        super(ThingForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.CheckboxSelectMultiple()
        self.fields['tags'].queryset = Tag.objects.all()
        self.fields['tags'].help_text = None
        for field in self.fields.keys():
            self.fields[field].widget.attrs['class'] = field
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label = ''
