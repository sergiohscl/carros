from django import forms
from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 15000:
            self.add_error(
                'value', 'Valor mínimo do carro deve ser de R$15.000,00'
            )
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1970:
            self.add_error(
                'factory_year', 'Não é possível cadastrar carros fabricados antes de 1970'  # noqa E501
            )
        return factory_year
