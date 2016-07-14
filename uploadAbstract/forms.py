from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from uploadAbstract.models import SubmittedAbstract


class UserForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices=(("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms."), ("Dr.", "Dr."),
                                            ("Prof.", "Prof."), ("Sir", "Sir"), ("Lady", "Lady"), ("Lord", "Lord")),
                                   required=True)
    first_name = forms.CharField(max_length=35)
    last_name = forms.CharField(max_length=35)
    co_authors_names = forms.CharField(max_length=770, required=False, help_text="Separate each author with a comma")
    email = forms.EmailField(max_length=60, required=True)
    paper_title = forms.CharField(max_length=300, required=True)
    abstract = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('/uploadAbstract/', 'Upload Abstract', css_class='btn-primary'))

    class Meta:
        model = SubmittedAbstract
        fields = ('salutation', 'first_name', 'last_name',
                  'co_authors_names', 'email', 'paper_title', 'abstract')
