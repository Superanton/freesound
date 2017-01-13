import json
import base64
from django import forms
from models import DonationCampaign

class DonateForm(forms.Form):
    RADIO_CHOICES = []

    donation_type = forms.ChoiceField(widget=forms.RadioSelect(), choices=RADIO_CHOICES)
    name_option = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DonateForm, self).__init__(*args, **kwargs)

        choices = [
            ('1', "Anonymous"),
            ('2', "Other: "),
        ]
        if user.username:
            self.user_id = user.id
            choices.insert(0, ('0', user.username))
            self.initial['donation_type'] = '0'
        else:
            self.initial['donation_type'] = '1'

        self.fields['donation_type'] = forms.ChoiceField(
                    widget=forms.RadioSelect(), choices=choices)

    def clean(self):
        campaign = DonationCampaign.objects.order_by('date_start').last()
        returned_data = {"campaign_id": campaign.id}

        annon = self.cleaned_data['donation_type']

        # We store the user even if the donation is annonymous
        if self.user_id :
            returned_data['user_id'] = self.user_id

        if annon == '1':
            returned_data['name'] = "Anonymous"
        elif annon == '2':
            returned_data['name'] = self.cleaned_data.get('name_option', '')

        # Paypal gives only one field to add extra data so we send it as b64
        self.encoded_data = base64.b64encode(json.dumps(returned_data))