from django import forms

class PiazzaAuthForm(forms.Form):
    lti_message_type = forms.CharField()
    lti_version = forms.CharField()
    resource_link_id = forms.CharField()
    resource_link_title = forms.CharField()
    resource_link_description = forms.CharField()
    user_id = forms.CharField()
    lis_person_name_full = forms.CharField()
    lis_person_contact_email_primary = forms.CharField()
    lis_person_sourcedid = forms.CharField()
    tool_consumer_instance_description = forms.CharField()
    launch_presentation_return_url = forms.CharField()
    ext_lti_message_type = forms.CharField()
    ext_submit = forms.CharField()
    roles = forms.CharField()
    context_label = forms.CharField()
    context_id = forms.CharField()
    context_title = forms.CharField()
    context_type = forms.CharField()
    oauth_callback = forms.CharField()
    oauth_signature = forms.CharField()

