
def UserName():
    added=False
    while not added:
        user_name = input("First Name:")
        if user_name:
            added=True
    return user_name

def UserLastName():
    while not added:
        last_name = input("Last Name:")
        if last_name:
            added=True
    return last_name


def UserBirthYear():
    while not added:
        birth_year = int(input("Birth Year:"))
        if birth_year:
            added=True
    return birth_year

def UserBirthDay():
    birth_day= int(input("Birth Day:"))
    return birth_day

def UserBirthMonth():
    birth_month= int(input("Birth Month:"))
    return birth_month

def Usernationality():
    nationality = input("Nationality:")
    return nationality

def UserCountryRes():
    nationality = input("Country of residence:")
    return nationality

def UserDegree():
    degree = input("University degree:")
    return degree

def UserGradYear():
    grad_year = int(input("Graduation Year"))
    return grad_year

def UserAvalibility():
    avalibility = int(input("Availability per week in hours"))
    return avalibility

def UserStudyStatus():
    study_status = input("Alumni/Student")
    return study_status

def User_GPA():
    study_status = input("GPA")
    return study_status

def UserLookingFor():
    looking_for_info=[]
    add_more=True
    while add_more:
        user_looking_for = input("Characteristics <Enter to end>:")
        looking_for_info.append(user_looking_for)
        if not user_looking_for:
            add_more=False
    return looking_for_info

def UserInterests():
    interests=[]
    add_more=True
    while add_more:
        user_looking_for = input("Characteristics <Enter to end>:")
        interests.append(user_looking_for)
        if not user_looking_for:
            add_more=False
    return interests

def UserEmail():
    email_address = input("Email Address:")
    return email_address

def UserPhoneNumber():
    phone_number = int(input("Phone Number:"))
    return phone_number

def UserLinkedin():
    Linkedin = input("Phone Number:")
    return Linkedin


#def main():
    user_name = UserName()
    last_name = UserLastName()
    birth_year = UserBirthYear()
    birth_day = UserBirthDay()
    birth_month = UserBirthMonth()
    nationality = Usernationality()
    degree = UserDegree()
    grad_year = UserGradYear()
    avalibility = UserAvalibility()
    study_status = UserStudyStatus()
    User_GPA = User_GPA()
    looking_for = UserLookingFor()
    interests = UserInterests()

main()
