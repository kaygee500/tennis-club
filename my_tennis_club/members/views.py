from django.http import HttpResponse , JsonResponse
from django.template import loader
from .models import Member
from .serializers import MembersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context={
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context={
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    # mydata = Member.objects.filter(firstname='Emil').values()
    template = loader.get_template('template.html')
    context={
        #   'mymembers': mydata,
        'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'], 
        # 'y': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'], 
    }
    return HttpResponse(template.render(context, request))

@api_view (['GET', 'POST'])
def members_list(request, format=None):
    if request.method == 'GET':
        allmembers = Member.objects.all()
        serializer = MembersSerializer(allmembers, many = True)
        #return JsonResponse({"Members List":serializer.data}, safe=False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MembersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET', 'PUT','DELETE'])
def member_detail(request, id, format = None):
    try:
        detail = Member.objects.get(pk=id)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MembersSerializer(detail)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MembersSerializer(detail, data = request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data) 
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
       

    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)