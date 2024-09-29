from django import forms
from category.models import Category

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = "__all__"

class CategoryForms(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['category_name', 'sort_order', 'draft_status', 'description', 'url', 'meta_title', 'meta_keyword', 'meta_content']