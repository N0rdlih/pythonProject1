from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.shortcuts import render
from .models import Bb, Rubric
from  django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse
from  django.views.generic.base import TemplateView
from  django.views.generic.detail import DetailView
from django.views.generic.list import ListView



class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = '/bboard/'# reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context

#That class is using TempalateView
class BbByRubricView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name='bbs'
    def get_queryset(self):
        return Bb.object.filter(rubric=self.kwargs['rubric_id'])
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        context['current_rubric']=Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context



class BbByRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['bbs']=Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics']=Rubric.objects.all()
        context['current_rubric']=Rubric.object.get(pk=context['rubric_id'])
        return context

class BbDetailView(DetailView):
    model=Bb
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
             'current_rubric': current_rubric}
    print("Slava rody")
    print(current_rubric)
    return render(request, 'bboard/by_rubric.html', context)

def add_and_save(request):
    if request.method=='POST':
        bbf=BbForm(request.POST)
        if  bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context={'form':bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf=BbForm()
        context={'form':bbf}
        return render(request, 'bboard/create.html', context)




#this is my old controller for add
#def add(request):
 #   bbf=BbForm()
 #   context={'form':bbf}
  #  return render(request, 'bboard/create.html', context)


#this is my old controller for add save
#def add_save(request):
#    bbf=BbForm(request.POST)
#    if bbf.is_valid():
#        bbf.save()
#        return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#    else:
#        context={'form':bbf}
#        return render(request, 'bboard/create.html', context)





def index(request) :
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    template= get_template('bboard/index.html')

    #that's for lowlevel answer
   # resp=HttpResponse("Тут буде ", content_type='text/plain; charset=utf-8')
   #resp.write('головна')
   # resp.writelines(('сторінка',' сайту'))
    #resp['keywords']='Python, Django'
   # return resp

    return HttpResponse(template.render(context=context, request=request))
    #return render(request, 'bboard/index.html', context)


#def index(request):
    #s = 'Список объявлений\r\n\r\n\r\n'
    #for bb in Bb.objects.order_by('-published'):
    #    s += bb.title + '\r\n'+bb.content + '\r\n\r\n'
    #return HttpResponse(s, content_type='text/plain; charset=utf-8')
#def index(request):
#    template=loader.get_template('bboard/index.html')
#    bbs=Bb.objects.order_by('-published')
#     context={'bbs':bbs}
#     return HttpResponse(template.render(context, request))
#def index(request):
#    bbs=Bb.objects.order_by('-published')
#    return render(request,'bboard/index.html',{'bbs':bbs})


#This function displays error "404"
#def detail(request, bb_id):
#    try:
#        bb=Bb.objects.get(pk=bb_id)
#    except Bb.DoesNotExist:
#        return HttpResponseNotFound('Оголошення не існує')

