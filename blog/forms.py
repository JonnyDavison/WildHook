from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'author',
                  'categories', 'tags',
                  'meta_description', 'meta_keywords']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='shop-now-button'))
