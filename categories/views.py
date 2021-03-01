from django.http import response
from django.shortcuts import render,redirect
from categories.models import AreaEn
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q

def articles(request):
    return render(request,'articles.html')

def dataUsersWorkshop(request):
    return render(request,'dataUsersWorkshop.html')      

def factsheets(request):
    india=AreaEn.objects.values('area_code','area_name').filter(area_parent_id=-1)
    states=AreaEn.objects.values('area_code','area_name').filter(area_parent_id=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')
    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)>1:
            for s in individual_name:
                if flag:
                    str+=s +'-'
                    flag=False
                else:
                    str+=s    
                    flag=True
        else :
            str=individual_name[0]            
        states[i]['area_code'] = 'static/factsheets/CNNS-v6-factsheet-' + str + '.pdf' 
    for i in range(len(india)):    
        india[i]['area_code']=  'static/factsheets/CNNS-v6-factsheet-' + india[i]['area_name'] + '.pdf'  
    return render(request,'factsheets.html',{'states':states,'india':india})   

def index(request):
    return render(request,'index.html')

def keyFindings(request):
    return render(request,'keyFindings.html')

def presentations(request):

    states=AreaEn.objects.values('area_code','area_name').filter(area_parent_id=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')
   
    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)==2:
            for s in individual_name:
                if flag:
                    str+=s +'_'
                    flag=False
                else:
                    str+=s   
        elif len(individual_name)==3:
            temp=2
            for s in individual_name:
                if temp:
                    str+=s +'_'
                    temp-=1
                    continue
                else:
                    str+=s   
        else :
            str=individual_name[0]
        states[i]['area_code'] = 'static/presentations/CNNS_Presentations_' + str + '.pdf'  
    return render(request,'presentations.html',{'states':states})

def report(request):
    return render(request,'report.html')    

def stateAndDistrict (request):

    selected_state_value='India'
    india=AreaEn.objects.values('area_code','area_name').filter(area_parent_id=-1)
    states=AreaEn.objects.values('area_code','area_name','area_id').filter(area_parent_id=1).order_by('area_name')

    for i in range(len(states)):
        states[i]['area_code'] = 'static/stateAndDistrict/NutritionInfo_' + states[i]['area_code']+ '_' + states[i]['area_name'] + '.pdf'  
    for i in range(len(india)):    
        india[i]['area_code']= 'static/stateAndDistrict/NutritionInfo_' + india[i]['area_code']+ '_' + india[i]['area_name'] + '.pdf'   

    if request.method == 'POST':
        try:
            selected_state_value=request.POST['selected_state']
        except MultiValueDictKeyError:
           selected_state_value = '' 

        if selected_state_value!='India':   
            areaId=AreaEn.objects.values('area_id').filter(area_name=selected_state_value).first() 
            id=areaId['area_id']
            district=AreaEn.objects.values('area_code','area_name').filter(area_parent_id=id).order_by('area_name')
            for i in range(len(district)):    
                district[i]['area_code']= 'static/stateAndDistrict/NutritionInfo_' + district[i]['area_code']+ '_' + district[i]['area_name'] + '.pdf'  
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'district':district,'selected_state_value':selected_state_value})  
        else :          
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value})      
    else :          
        return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value}) 
   

def thematicReport(request):
    return render(request,'thematicReport.html')
    

