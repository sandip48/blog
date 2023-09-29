from django import forms
from post.models import Post
# class PostForm(forms.Form):
#     title=forms.CharField(
#                           max_length=50,
#                           required=True,
#                           widget=forms.TextInput(
#                           attrs={
#                               'class':"form-control",
#                               'placeholder':"Please provide title of the post.",
#                           }
#                     ),
#              )
#     content=forms.CharField(
#         required=True,
#         widget=forms.Textarea(
#             attrs={
#                 "class":"form-text",
#             }
#         ),
#     )
#     image=forms.FileField(required=True, widget=forms.FileInput(attrs={"class":"form-control"}))

#     def clean_content(self):
#         content=self.cleaned_data.get('content')
#         if len(content)<10:
#             raise forms.ValidationError("Content should be at least contain 10 letter.")
#         return content
#     def clean_title(self):
#         title=self.cleaned_data.get('title')
#         if not str(title).startswith("Django"):
#             raise forms.ValidationError("Title should contain Django word.")
#         return title
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','image']

        widgets={
            'title':forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Please Provide TItle for Post",
                }
            ),
            "content":forms.Textarea(
                attrs={
                    "class":"forms-cotntrol",
                }
            ),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }