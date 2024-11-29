from flask import Blueprint, render_template, request,session,url_for,redirect
from userclass import User  # Class user.py
from datetime import datetime
import os
import ast
from validation import validation_function

account_bp = Blueprint('account', __name__)
user_data = {}

# Ruta para mostrar el perfil y los datos del usuario
@account_bp.route('/account_page', methods=['GET', 'POST'])
def account_page():
    if session.get('IsLogged') != True:
        return redirect(url_for('login'))     
    user_data = User.get_user_data_from_csv(session['email'])
    topics = [
    "Architecture", "Business", "Culinary Arts", "CrossFit", "Cycling", "Dance", 
    "Development", "Education", "Entrepreneurship", "Feminism", "Film", "Fitness", 
    "Gymnastics", "International Relations", "Languages", "Mindfulness", 
    "Outdoor Activities", "Physics", "Public Policy", "Rock Climbing", "Sailing", 
    "Skateboarding", "Skiing", "Sports", "Surfing", "Sustainability", "Tennis", 
    "Travel", "Vegetarianism", "Yoga"
]
   
    if request.method == 'POST':
            # Get form data
              first_name = request.form.get('first_name')
              last_name = request.form.get('last_name')  
              description = request.form.get('description')
              additional_info = request.form.get('additional_info')              
              dob = request.form.get('dob')
              nationality = request.form.get('nationality')
              country_residence = request.form.get('country_residence')
              degree = request.form.get('degree_studied')
              graduation_year = request.form.get('graduation_year')
              gpa = request.form.get('gpa')  
              availability = request.form.get('availability')
              topics_of_interest = request.form.getlist('topics')             
              user_type = request.form.get('user_type')
              linkedin = request.form.get('linkedin')
              file = request.files['imagef']
             # Get the "mentor" checkbox value
              mentor = request.form.get('mentor')  
              image = request.form.get('image')   
                      
              if file and file.filename: 
                try:   
                  image = file.filename 
                  file_path =  os.path.join('static', 'images', image)              
                  file.save(file_path)
                except Exception as e:                  
                  print(f"Error saving file: {e}")   
                               
              birthdate=datetime.strptime(dob, "%Y-%m-%d")
              today = datetime.today()
              age = today.year -birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
              age=int(age)
              
              if mentor:
                  mentor = True
              else:
                  mentor = False
                  
              email = user_data['Email']
              password=user_data['Password']
              rating=user_data['Rating']
              matched_topics = request.form.get('selected_topics').split(', ')
              other_topics = request.form.get('other_topics').split(', ')
              all_topics = matched_topics + other_topics 
             
              cleaned_topics = [] 

              for topic in all_topics:  
                cleaned_topic = topic.strip('"')  
                if cleaned_topic:  
                  cleaned_topics.append(cleaned_topic)  
                  
              topics_of_interest = cleaned_topics 
                       
              # Create User object
              user = User(first_name, last_name, email, password, description, additional_info, rating,
                    age, dob, nationality, country_residence, degree, graduation_year, gpa,
                    availability, topics_of_interest, user_type, linkedin,mentor,image)
          
             # Validate user data
              vValid, verr = validation_function(user,1)     
              if vValid==1:
                    return render_template('app/templates/profile.html', user=user_data, error_message=verr)
              else:
                    
                    User.save_to_csv(user)                  
                    user_data = User.get_user_data_from_csv(session['email'])   
                    
                    user_data =user_Topics_function(user_data,topics) 
                                 
                    return render_template('app/templates/profile.html', user=user_data,topics=topics)  
    else:
       user_data = User.get_user_data_from_csv(session['email'])   
       
       user_data =user_Topics_function(user_data,topics)                           
                
       return render_template('app/templates/profile.html', user=user_data, topics=topics)
  
  
  
  
      
def user_Topics_function(user_data,topicsList):
        user_topics_str = user_data.get('Topics of Interest')  
       

        if user_topics_str is not None:
            try:
              user_topics = ast.literal_eval(user_topics_str) 
            except (ValueError, SyntaxError) as e:
              user_topics = []  
        else:
            user_topics = []  
        
        
        matched_topics = []  
        for topic in topicsList:  
            if topic in user_topics:  
                matched_topics.append(topic)       
      
        unmatched_topics = []  
        for topic in user_topics:  
            if topic not in topicsList:  
                unmatched_topics.append(topic)  
        
        # Actualizar datos del usuario
        user_data['Matched Topics'] = matched_topics
        user_data['Other Topics'] = unmatched_topics           
        return user_data
           