from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import numpy as np
#from .views import detail_view
from django.urls import path

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import os
import pandas as pd
import pickle

# def homepage1(request):
#     return render(request,"homepage1.html")

# def tpage(request):
#     return render(request,"t.html")



#model code form
def landing(request):
    return render(request, 'landing.html')

def index(request):
    return render(request,'index.html')

my_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(my_dir, 'lr_clf.pkl')
with open(pickle_file_path, 'rb') as pickle_file:
    model = pickle.load(pickle_file)
# model=pickle.load(open(r'C:\Users\aarbs\new_project2\finalapp\lr_clf.pkl','rb+'))
def predict(request):
     if request.method=='POST':       
        temp={}
        p={} #personality dict
        d={"Strongly Disagree": 1,"Disagree":2,"Slightly Disagree":3,"Neutral":4,"Slightly Agree":5,"Agree":6,"Strongly Agree":7}
        temp['1']=int(request.POST.get('db_rating')) 
        temp['2']=int(request.POST.get('comp_arch_rating')) 
        temp['3']=int(request.POST.get('dist_comp_rating')) 
        temp['4']=int(request.POST.get('cybersecurity')) 
        temp['5']=int(request.POST.get('networking')) 
        temp['6']=int(request.POST.get('development')) 
        temp['7']=int(request.POST.get('programmingskills')) 
        temp['8']=int(request.POST.get('project_management_rating')) 
        temp['9']=int(request.POST.get('computer_forensics_fundamental_rating')) 
        temp['10']=int(request.POST.get('technical_communication_rating')) 
        temp['11']=int(request.POST.get('ai_ml_rating')) 
        temp['12']=int(request.POST.get('software_eng_rating')) 
        temp['13']=int(request.POST.get('business_analysis_rating')) 
        temp['14']=int(request.POST.get('communication_skills_rating')) 
        temp['15']=int(request.POST.get('data_science_rating')) 
        temp['16']=int(request.POST.get('troubleshooting-rating')) 
        temp['17']=int(request.POST.get('graphics-designing-rating')) 

        p['ext1']=int(d[request.POST.get('ext1')])
        p['ext2']=int(d[request.POST.get('ext2')])
        p['ext3']=int(d[request.POST.get('ext3')])
        p['ext4']=int(d[request.POST.get('ext4')])
        p['est1']=int(d[request.POST.get('est1')])
        p['est2']=int(d[request.POST.get('est2')])
        p['est3']=int(d[request.POST.get('est3')])
        p['est4']=int(d[request.POST.get('est4')])

        p['agr1']=int(d[request.POST.get('agr1')])
        p['agr2']=int(d[request.POST.get('agr2')])
        p['agr3']=int(d[request.POST.get('agr3')])
        p['agr4']=int(d[request.POST.get('agr4')])
        p['csn1']=int(d[request.POST.get('csn1')])
        p['csn2']=int(d[request.POST.get('csn2')])
        p['csn3']=int(d[request.POST.get('csn3')])
        p['csn4']=int(d[request.POST.get('csn4')])
        p['opn1']=int(d[request.POST.get('opn1')])
        p['opn2']=int(d[request.POST.get('opn2')])
        p['opn3']=int(d[request.POST.get('opn3')])
        p['opn4']=int(d[request.POST.get('opn4')])
        p['otc']=int(d[request.POST.get('otc')])
        p['hed']=int(d[request.POST.get('hed')])

        p['ste1']=int(d[request.POST.get('ste1')])
        p['ste2']=int(d[request.POST.get('ste2')])
        p['ste3']=int(d[request.POST.get('ste3')])
        p['ste4']=int(d[request.POST.get('ste4')])

        p['con']=int(d[request.POST.get('con')])
        p['emo']=int(d[request.POST.get('emo')])

        p['set1']=int(d[request.POST.get('set1')])
        p['set2']=int(d[request.POST.get('set2')])
        p['set3']=int(d[request.POST.get('set3')])
        p['set4']=int(d[request.POST.get('set4')])
        
        
        # Create features dictionary with proper names for model prediction
        features = {}
        features['Database Fundamentals'] = temp['1']
        features['Computer Architecture'] = temp['2']
        features['Distributed Computing Systems'] = temp['3']
        features['Cyber Security'] = temp['4']
        features['Networking'] = temp['5']
        features['Software Development'] = temp['6']
        features['Programming Skills'] = temp['7']
        features['Project Management'] = temp['8']
        features['Computer Forensics Fundamentals'] = temp['9']
        features['Technical Communication'] = temp['10']
        features['AI ML'] = temp['11']
        features['Software Engineering'] = temp['12']
        features['Business Analysis'] = temp['13']
        features['Communication skills'] = temp['14']
        features['Data Science'] = temp['15']
        features['Troubleshooting skills'] = temp['16']
        features['Graphics Designing'] = temp['17']
        
        # Calculate OCEAN personality traits
        features['Openness'] = int((p['opn1'] + p['opn2'] + p['opn3'] + p['opn4'])/4)
        features['Conscientousness'] = int((p['csn1'] + p['csn2'] + p['csn3'] + p['csn4'])/4)  # Note: misspelling matches model
        features['Extraversion'] = int((p['ext1'] + p['ext2'] + p['ext3'] + p['ext4'])/4)
        features['Agreeableness'] = int((p['agr1'] + p['agr2'] + p['agr3'] + p['agr4'])/4)
        
        # Calculate emotional range (based on emotional stability/neuroticism)
        features['Emotional_Range'] = int((p['est1'] + p['est2'] + p['est3'] + p['est4'])/4)
        
        # Other personality dimensions
        features['Conversation'] = int(d[request.POST.get('con')])
        features['Openness to Change'] = int(d[request.POST.get('otc')])
        features['Hedonism'] = int(d[request.POST.get('hed')])
        features['Self-enhancement'] = int((p['set1'] + p['set2'] + p['set3'] + p['set4'])/4)
        features['Self-transcendence'] = int((p['ste1'] + p['ste2'] + p['ste3'] + p['ste4'])/4)

        testdata=pd.DataFrame(features, index=[0])
        scoreval=model.predict(testdata)[0]
        pred=''
        if scoreval == 0:
               pred = 'AI ML Specialist'
        elif scoreval==1:
            pred = 'API Specialist'
        elif scoreval ==2:
            pred = 'Application Support Engineer'
        elif scoreval ==3:
            pred = 'Business Analyst'
        elif scoreval ==4:
            pred = 'Customer Service Executive'
        elif scoreval ==5:
            pred = 'Cyber Security Specialist'
        elif scoreval ==6:
            pred = 'Database Administrator'
        elif scoreval ==7:
            pred = 'Graphics Designer'
        elif scoreval ==8:
            pred = 'Hardware Engineer'
        elif scoreval ==9:
            pred = 'Helpdesk Engineer'
        elif scoreval ==10:
            pred = 'Information Security Specialist'
        elif scoreval ==11:
            pred = 'Networking Engineer'
        elif scoreval ==12:
            pred = 'Project Manager'
        elif scoreval ==13:
            pred = 'Software Developer'
        elif scoreval ==14:
            pred = 'Software tester'
        elif scoreval ==15:
            pred ='Technical Writer'
        
        #for top 3
        probs_1= model.predict_proba(testdata)
        
        probs=probs_1[0]
        m=len(probs)
        roles={probs[0]:'AI ML Specialist',probs[1]:'API Specialist', probs[2]:'Application Support Engineer',
        probs[3]:'Business Analyst'
        ,probs[4]:'Customer Service Executive',probs[5]:'Cyber Security Specialist',
        probs[6]:'Database Administrator'
        ,probs[7]:'Graphics Designer'
        ,probs[8]:'Hardware Engineer',probs[9]:'Helpdesk Engineer',probs[10]:'Information Security Specialist',
        probs[11]:'Networking Engineer'
        ,probs[12]:'Project Manager',probs[13]:'Software Developer',probs[14]:'Software tester',probs[15]:'Technical Writer'}

        x=np.sort(probs)
        top=x[13:16]
        l=[]

        for i in range(2,-1,-1):
            l.append([roles[top[i]],int(top[i]*100)])
        
        # --- Skill Gap Analysis Logic ---
        # Defining ideal skill targets (on a scale of 1-7) for each role
        role_skill_requirements = {
            'AI ML Specialist': {'AI ML': 7, 'Data Science': 6, 'Programming Skills': 6, 'Software Engineering': 5, 'Database Fundamentals': 4},
            'API Specialist': {'Software Development': 6, 'Programming Skills': 6, 'Networking': 5, 'Distributed Computing Systems': 4, 'Database Fundamentals': 4},
            'Application Support Engineer': {'Troubleshooting skills': 7, 'Software Development': 5, 'Database Fundamentals': 5, 'Networking': 5, 'Communication skills': 4},
            'Business Analyst': {'Business Analysis': 7, 'Communication skills': 6, 'Project Management': 5, 'Software Development': 4, 'Data Science': 4},
            'Customer Service Executive': {'Communication skills': 7, 'Technical Communication': 6, 'Troubleshooting skills': 5, 'Business Analysis': 4},
            'Cyber Security Specialist': {'Cyber Security': 7, 'Networking': 6, 'Computer Forensics Fundamentals': 6, 'Programming Skills': 5, 'Distributed Computing Systems': 4},
            'Database Administrator': {'Database Fundamentals': 7, 'Distributed Computing Systems': 6, 'Troubleshooting skills': 5, 'Computer Architecture': 4},
            'Graphics Designer': {'Graphics Designing': 7, 'Communication skills': 5, 'Technical Communication': 4, 'Project Management': 3},
            'Hardware Engineer': {'Computer Architecture': 7, 'Troubleshooting skills': 6, 'Networking': 5, 'Distributed Computing Systems': 4},
            'Helpdesk Engineer': {'Troubleshooting skills': 7, 'Communication skills': 6, 'Networking': 5, 'Computer Architecture': 4, 'Database Fundamentals': 4},
            'Information Security Specialist': {'Cyber Security': 7, 'Computer Forensics Fundamentals': 6, 'Networking': 6, 'Troubleshooting skills': 5, 'Database Fundamentals': 4},
            'Networking Engineer': {'Networking': 7, 'Troubleshooting skills': 6, 'Cyber Security': 5, 'Distributed Computing Systems': 4, 'Computer Architecture': 4},
            'Project Manager': {'Project Management': 7, 'Communication skills': 6, 'Business Analysis': 5, 'Software Engineering': 5, 'Technical Communication': 5, 'Software Development': 4},
            'Software Developer': {'Programming Skills': 7, 'Software Development': 7, 'Software Engineering': 6, 'Database Fundamentals': 5, 'Distributed Computing Systems': 4},
            'Software tester': {'Software Engineering': 6, 'Software Development': 5, 'Troubleshooting skills': 6, 'Programming Skills': 5, 'Database Fundamentals': 4},
            'Technical Writer': {'Technical Communication': 7, 'Communication skills': 6, 'Software Engineering': 4, 'Software Development': 4, 'Project Management': 4}
        }

        def get_skill_assessment(role_name):
            skills_assessed = []
            has_gaps = False
            if role_name in role_skill_requirements:
                required_skills = role_skill_requirements[role_name]
                for skill, target_score in required_skills.items():
                    user_score = features.get(skill, 0)
                    gap_val = max(0, target_score - user_score)
                    is_gap = gap_val > 0
                    if is_gap:
                        has_gaps = True
                    skills_assessed.append({
                        'skill': skill,
                        'current': user_score,
                        'target': target_score,
                        'gap': gap_val,
                        'is_gap': is_gap
                    })
            # Sort: gaps first, then by target score descending
            skills_assessed.sort(key=lambda x: (not x['is_gap'], -x['target']))
            return {'skills': skills_assessed, 'has_gaps': has_gaps}

        all_skill_gaps = [
            {'role': l[0][0], **get_skill_assessment(l[0][0])},
            {'role': l[1][0], **get_skill_assessment(l[1][0])},
            {'role': l[2][0], **get_skill_assessment(l[2][0])}
        ]
        # --------------------------------

        # pages={'AI ML Specialist':'https://resources.workable.com/machine-learning-engineer-job-description#:~:text=Designing%20and%20developing%20machine%20learning,Implementing%20appropriate%20ML%20algorithms'}
        # yy=pages[l[0][0]]
        return render(request,'result.html',{'result':pred,'x':l[0][0],'y':l[1][0],'z':l[2][0], 'all_skill_gaps': all_skill_gaps})
        #return render(request,'result.html',{'result':pred,'x':l[0][0],'y':l[1][0],'z':l[2][0],'po':yy})
     else:
         return render(request,'index.html')
