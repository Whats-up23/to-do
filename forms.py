from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Todoのタイトルを入力'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '説明を入力（任意）',
                'rows': 3
            }),
        }
