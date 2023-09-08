from django.forms import *
from .models import Category


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# esto para no repetir codigo en el attrs de abajo
        # self.fields['name'].widget.attrs['autofocus'] = True
        # for form in self.visible_fields():
        #             form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {'name': TextInput(
            attrs={
                'placeholder': 'Nombre',
            }
        ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Descripción',
                    'rows': 3,
                    'cols': 3,
                }
            )
        }
