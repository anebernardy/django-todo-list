from django.utils import timezone
from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.fields["deadline"].widget.attrs["min"] = (
                timezone.localdate().isoformat()
            )

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        today = timezone.localdate()

        if self.instance.pk and deadline == self.instance.deadline:
            return deadline

        if deadline < today:
            raise forms.ValidationError(
                "A data de entrega não pode ser no passado."
            )
        
        return deadline
    