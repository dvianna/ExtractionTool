from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from forms import *
from django.forms.formsets import formset_factory
from neemi.data import get_user_data, get_all_user_data
from neemi.search import *
from neemi.stats import *
from neemi.parse import *
from neemi.index import *
import time, datetime

def getQueryConditions2(form):
        keys = {}
        values = {}

        if (form.cleaned_data['howKey'] != ''):
            keys['how'] = form.cleaned_data['howKey']
        if (form.cleaned_data['whatKey'] != ''):
            keys['what'] = form.cleaned_data['whatKey']
        if (form.cleaned_data['whenKey'] != ''):
            keys['when'] = form.cleaned_data['whenKey']
        if (form.cleaned_data['whereKey'] != ''):
            keys['where'] = form.cleaned_data['whereKey']
        if (form.cleaned_data['whoKey'] != ''):
            keys['who'] = form.cleaned_data['whoKey']
        if (form.cleaned_data['whyKey'] != ''):
            keys['why'] = form.cleaned_data['whyKey']

        if (form.cleaned_data['howValue'] != ''):
            values['how'] = form.cleaned_data['howValue']
        if (form.cleaned_data['whatValue'] != ''):
            values['what'] = form.cleaned_data['whatValue']
        if (form.cleaned_data['whenValue'] != ''):
            values['when'] = form.cleaned_data['whenValue']
        if (form.cleaned_data['whereValue'] != ''):
            values['where'] = form.cleaned_data['whereValue']
        if (form.cleaned_data['whoValue'] != ''):
            values['who'] = form.cleaned_data['whoValue']
        if (form.cleaned_data['whyValue'] != ''):
            values['why'] = form.cleaned_data['whyValue']
        return keys, values


def getQueryConditions(forms):
    for form in forms:
        print form.cleaned_data   


def index(request, template='index.html'):
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response


def register(request, template='register.html'):
    services = REGISTER_CHOICES
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response


def search2(request, template='search.html'):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print [form.data]
            print "GOOD DATA"
            print [form.cleaned_data]
            keys, values = getQueryConditions(form)
            print "keys: ", keys
            print "values: ", values
            search = Search(request)
            search.simple_search(request=request, keys=keys, values=values)
            results = search.getResults()
        else:
            print "invalid form"
            #dform = form
    else:
        form = SearchForm()
        
    response = render_to_response(
    template, locals(), context_instance=RequestContext(request,{'form':form})
        )
    return response

       
def search(request, template='search.html'):
    SearchFormSet = formset_factory(SearchServicesForm)
    forms = SearchFormSet()
    if request.method == 'POST':
        print(request.POST)
        formset = SearchFormSet(request.POST)
        if formset.is_valid() :
            if 'search_and' in request.POST:
                search = Search(request)
                search.simple_searchAND(request=request, formValues=formset.cleaned_data)
                results = search.getResults()
        else:
            print "invalid form"
 
    response = render_to_response(
    template, locals(), context_instance=RequestContext(request,{'forms':forms})
        )
    return response
    
def search_parsed_data(request, template='search_parsed_data.html'):
    SearchFormSet = formset_factory(SearchForm)
    forms = SearchFormSet()
    if request.method == 'POST':
        formset = SearchFormSet(request.POST)
        if formset.is_valid() :
            if 'addform' in request.POST:
                forms = SearchFormSet(initial=formset.cleaned_data)
            elif 'search_or' in request.POST:
                search = Search(request)
                search.parsed_searchOR(request=request, formValues=formset.cleaned_data)
                results = search.getResults()
            elif 'search_and' in request.POST:
                search = Search(request)
                search.parsed_searchAND(request=request, formValues=formset.cleaned_data)
                results = search.getResults()
        else:
            print "invalid form"
 
    response = render_to_response(
    template, locals(), context_instance=RequestContext(request,{'forms':forms})
        )
    return response


def query_results(request, template='results.html'):
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response

def get_data(request, template='data.html'):
    if request.method == 'POST':
        form = GetDataForm(request.POST)
        if form.is_valid():
            print [form.data]
            print "GOOD DATA"
            print [form.cleaned_data]
            if 'bt_search' in form.data:
                return get_all_user_data(request=request,
                                         service=form.cleaned_data['service'])
            elif 'bt_get_data_since' in form.data:
                return get_user_data(request=request,
                                     service=form.cleaned_data['service'],
                                     from_date="since_last",
                                     to_date=None,
                                     lastN=None)
            else:
                if form.cleaned_data['from_date'] != None:
                    from_date_epoch=int(time.mktime(form.cleaned_data['from_date'].timetuple()))//1*1000
                else:
                    from_date_epoch = None

                if form.cleaned_data['to_date'] != None:
                    to_date_epoch=int(time.mktime(form.cleaned_data['to_date'].timetuple()))//1*1000
                else:
                    to_date_epoch=None
        
                return get_user_data(request=request,
                                     service=form.cleaned_data['service'],
                                     from_date=from_date_epoch,
                                     to_date=to_date_epoch,
                                     lastN=form.cleaned_data['lastN'])
        else:
            print "invalid form"
            dform = form
    else:
        dform = GetDataForm()
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request,{'form':dform})
        )
    return response


def delete(request, template='delete.html'):
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response


def get_stats(request, template='stats.html'):
    if request.method == 'GET':
        stats = DBAnalysis(request)
        html_stats = stats.basic_stats()   

    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )

#    response = render_to_response(template, locals(), context_instance=RequestContext(request),#{"html_stats":html_stats})

    return response
        

def parse_data(request, template='parser.html'):
    print "views.py/parse_data"
    if request.method == 'POST':
        print "request.method == POST"
        form = GetDataForm(request.POST)
        if form.is_valid():
            print [form.data]
            print "GOOD DATA"
            print [form.cleaned_data]
            if 'parse_data_service' in form.data:
                print "parse_data_service"
                parser = DBParser(request)
                parser.parse_service_data(request=request, service=form.cleaned_data['service'])
            else:
                print "parse_all_data"
        else:
            print "invalid form"
            form = form
    else:
        print "request.method == GET"
        form = GetDataForm()
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request,{'form':form})
        )
    return response


def create_indexes(request, template='create_indexes.html'):
    if request.method == 'GET':
        parser = DBParser(request)
        if parser.exist_collection() and parser.exist_user_document():
            status = True
            last_access = parser.get_last_access()
            msg = "The data was parsed for the last time on ", str(last_access)
        else:
            status = False
            msg = "There are no parsed data! Please, parse your data before indexing."
        print "Message: ", msg
    elif request.method == 'POST':
        index = DBIndexing(request)
        if 'index_data' in request.POST:
            return index.create_indexes()
        elif 'delete_pair_index' in request.POST:
            return index.drop_pair_indexes()
        elif 'delete_key_index' in request.POST:
            return index.drop_key_indexes()
        elif 'delete_value_index' in request.POST:
            return index.drop_value_indexes()

    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response


def error(request, template='error.html'):
    message = request.GET.get('message')
    print "Message: ", message
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response


