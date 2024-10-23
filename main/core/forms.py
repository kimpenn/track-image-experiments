from django import forms


class GetForeignKeyName(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name)


class GetManyToManyName(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name)
