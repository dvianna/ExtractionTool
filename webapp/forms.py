import datetime
from django import forms
from django.forms.formsets import formset_factory
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Select

SERVICE_CHOICES=(('facebook','Facebook'),
                 ('foursquare','foursquare'),
                 ('twitter','Twitter'),
                 ('linkedin','LinkedIn'),
                 ('gmail','Gmail'), 
                 ('gcal','Google Calendar'),
                 ('googleplus', 'Google+'),
                 ('googlecontacts', 'Google Contacts'),
                 ('dropbox','Dropbox'),
                 ('firefoxHistory','Firefox History'),
                 ('firefoxSearchHistory','Firefox Search History'),
                 ('chromeHistory', 'Chrome History'),
                 ('chromeSearchHistory', 'Chrome Search History'),
                 ('bank', 'Bank Data')
                )

REGISTER_CHOICES=(('facebook','Facebook'),
                 ('foursquare','foursquare'),
                 ('twitter','Twitter'),
                 ('linkedin','LinkedIn'),
                 ('gmail','Gmail'), 
                 ('gcal','Google Calendar'),
                 ('googleplus', 'Google+'),
                 ('googlecontacts', 'Google Contacts'),
                 ('dropbox','Dropbox'),
                )

DATATYPES=(('HOME','FB-HOME'),
                 ('LINK','FB-LINK'),
                 ('POST','FB-POST'),
                 ('PHOTO','FB-PHOTO'),
                 ('ALBUM','FB-ALBUM'), 
                 ('PROFILE','FB-PROFILE'),
                 ('EVENT', 'FB-EVENT'),
                 ('FEED', 'FB-FEED'),
                 ('STATUS','FB-STATUS'),
		 ('FRIEND', 'FB-FRIEND'),
		 ('GROUP', 'FB-GROUP'),
		 ('NOTE', 'FB-NOTE'),
		 ('INBOX','GMAIL-INBOX'),
                 ('SENT','GMAIL-SENT'),
                 ('ALL_MAIL','GMAIL-ALL_MAIL'),
		 ('MSG_RECEIVED','TWITTER-MSG_RECEIVED'),
                 ('MSG_SENT','TWITTER-MSG_SENT'),
                 ('TIMELINE','TWITTER-TIMELINE'),
                 ('FOLLOWER','TWITTER-FOLLOWER'),
		 ('FRIEND','TWITTER-FRIEND'),
		 ('TWEET','TWITTER-TWEET'),
		 ('FAVORITE','TWITTER-FAVORITE'),
		 ('MENTION','TWITTER-MENTION'),
		 ('RETWEET', 'TWITTER-RETWEET'),
		 ('PEOPLE','GPLUS-PEOPLE'),
                 ('ACTIVITIES','GPLUS-ACTIVITIES'),
                 ('COMMENTS','GPLUS-COMMENTS'),
		 ('CONTACT','GCONTACTS-CONTACT'),
		 ('METADATA','GCALENDAR-METADATA'),
		 ('EVENT','GCALENDAR-EVENT'),
		 ('FOLDERS','DROPBOX-FOLDERS'),
		 ('FILES','DROPBOX-FILES'),
		 ('BADGE','4SQUARE-BADGE'),
		 ('CHECKIN','4SQUARE-CHECKIN'),
                 ('RECENT', '4SQUARE-RECENT'),
		 ('CONNECTION','LINKEDIN-CONNECTION'),
		 ('UPDATE','LINKEDIN-UPDATE'),
		 ('PROFILE', 'LINKEDIN-PROFILE'),
		 )

DIMENSIONS=(('how','How'),
           ('what','What'),
           ('when','When'),
           ('where','Where'),
           ('who','Who'), 
           ('why','Why'),
                )

  
    #YEAR_CHOICES = reversed(range(2005,2013))


class GetDataForm(forms.Form):
    service = forms.ChoiceField(label="Service",choices=SERVICE_CHOICES)
    #from_date = forms.DateField(label="From (optional)",widget=SelectDateWidget(years=range(2013,2005,-1)),required=False)
    #to_date = forms.DateField(label="To (optional)",widget=SelectDateWidget(years=range(2013,2005,-1)),required=False)
    #lastN = forms.IntegerField(label="Result limit (optional)", required=False)

class SearchForm2(forms.Form):
    #service = forms.ChoiceField(label="Service",choices=SERVICE_CHOICES)
    howKey = forms.CharField(required=False)
    howValue = forms.CharField(required=False)
    whatKey = forms.CharField(required=False)
    whatValue = forms.CharField(required=False)
    whenKey = forms.CharField(required=False)
    whenValue = forms.CharField(required=False)
    whereKey = forms.CharField(required=False)
    whereValue = forms.CharField(required=False)
    whoKey = forms.CharField(required=False)
    whoValue = forms.CharField(required=False)
    whyKey = forms.CharField(required=False)
    whyValue = forms.CharField(required=False)

class SearchForm(forms.Form):
    dimension = forms.ChoiceField(choices=DIMENSIONS)
    key = forms.CharField(required=False)
    value = forms.CharField(required=False)

class SearchHowForm(forms.Form):
    howKey = forms.CharField(required=False)
    howValue = forms.CharField(required=False)

class SearchWhatForm(forms.Form):
    whatKey = forms.CharField(required=False)
    whatValue = forms.CharField(required=False)

class SearchServicesForm(forms.Form):
    service = forms.ChoiceField(choices=SERVICE_CHOICES)
    data_type = forms.ChoiceField(choices=DATATYPES)
    fromYear = forms.CharField(required=False)
    fromMonth = forms.CharField(required=False)
    fromDay = forms.CharField(required=False)
    tillYear = forms.CharField(required=False)
    tillMonth = forms.CharField(required=False)
    tillDay = forms.CharField(required=False)
    fromResult =  forms.CharField(required=False)
    untilResult =  forms.CharField(required=False)








