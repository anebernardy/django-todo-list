from django import forms
from django.utils import timezone

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadLine"]
        widgets = {
            "deadLine": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["deadLine"].widget.attrs["min"] = timezone.localdate().isoformat()

    def clean_deadLine(self):
        deadline = self.cleaned_data["deadLine"]

        if deadline < timezone.localdate():
            raise forms.ValidationError("A data de entrega não pode ser no passado.")
        return deadline
    