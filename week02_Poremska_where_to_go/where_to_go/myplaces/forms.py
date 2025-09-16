from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["title", "location", "comment", "rating"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5, "step": 0.5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Рейтинг має бути від 1 до 5")
        return rating