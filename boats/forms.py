from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
        max_length=25,
        error_messages={
            'max_length': "Invalid first name length.",
            'required': "Please enter your first name."})

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
        max_length=25,
        error_messages={
            'max_length': "Invalid last name length.",
            'required': "Please enter your last name."})

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
        error_messages={
            'invalid': "Invalid e-mail address.",
            'required': "Please enter your e-mail address."})

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Subject"}),
        min_length=2,
        max_length=30,
        error_messages={
            'max_length': "Invalid subject length",
            'required': "Please enter a subject."})

    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message'}),
        max_length=300,
        error_messages={
            'max_length': "Invalid message length",
            'required': "Please enter a message."})
