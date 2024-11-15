
def UserName():
    added=False
    while not added:
        user_name = input("First Name:")
        if user_name:
            added=True
    return user_name

def UserLastName():
    added = False
    while not added:
        last_name = input("Last Name:")
        if last_name:
            added=True
    return last_name


def UserBirthYear():
    added = False
    while not added:
        birth_year = int(input("Birth Year:"))
        if birth_year:
            added=True
    return birth_year

def UserBirthDay():
    added = False
    while not added:
        birth_day= int(input("Birth Day:"))
        if birth_day:
            added=True
    return birth_day

def UserBirthMonth():
    added = False
    while not added:
        birth_month= int(input("Birth Month:"))
        if birth_month:
            added=True
    return birth_month

def Usernationality():
    added = False
    while not added:
        nationality = input("Nationality:")
        if nationality:
            added=True
    return nationality

def UserCountryRes():
    added = False
    while not added:
        country_res = input("Country of residence:")
        if country_res:
            added=True
    return country_res

def UserDegree():
    added = False
    while not added:
        degree = input("University degree:")
        if degree:
            added=True
    return degree

def UserGradYear():
    added = False
    while not added:
        grad_year = int(input("Graduation Year:"))
        if grad_year:
            added=True
    return grad_year

def UserAvailability():
    added = False
    while not added:
        availability = int(input("Availability per week in hours:"))
        if availability:
            added=True
    return availability

def UserStudyStatus():
    added = False
    while not added:
        study_status = input("Alumni/Student:")
        if study_status:
            added=True
    return study_status

def UserGPA():
    added = False
    while not added:
        GPA = int(input("GPA:"))
        if GPA:
            added=True
    return GPA

def UserInterests():
    interests=[]
    add_more=True
    while add_more:
        user_looking_for = input("Characteristics of your interest <Enter to end>:")
        interests.append(user_looking_for)
        if not user_looking_for:
            add_more=False
    return interests

def UserEmail():
    added = False
    while not added:
        email_address = input("Email Address:")
        if email_address:
            added=True
    return email_address

def UserPhoneNumber():
    phone_number = int(input("Phone Number:"))
    if not phone_number:
        phone_number = None
    return phone_number

def UserAdditionalInformation():
    additional = input("additional info:")
    if not additional:
        additional = None
    return additional


def main():
    user_profile = []
    user_name = UserName()
    user_profile.append(user_name)
    last_name = UserLastName()
    user_profile.append(last_name)
    birth_year = UserBirthYear()
    user_profile.append(birth_year)
    birth_day = UserBirthDay()
    user_profile.append(birth_day)
    birth_month = UserBirthMonth()
    user_profile.append(birth_month)
    nationality = Usernationality()
    user_profile.append(nationality)
    degree = UserDegree()
    user_profile.append(degree)
    grad_year = UserGradYear()
    user_profile.append(grad_year)
    avalibility = UserAvailability()
    user_profile.append(avalibility)
    study_status = UserStudyStatus()
    user_profile.append(study_status)
    User_GPA = UserGPA()
    user_profile.append(User_GPA)
    interests = UserInterests()
    user_profile.append(interests)
    user_email = UserEmail()
    user_profile.append(user_email)
    User_phone_number= UserPhoneNumber()
    user_profile.append(User_phone_number)
    additional_info = UserAdditionalInformation()
    user_profile.append(additional_info)


    print(user_profile)



main()
