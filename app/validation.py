def validation_function(user,vorigen):
    #origen 0: Register
    #origen 1: Profile    
        vValid=0
        verr='' 
        if vorigen==0:  
            if not user.validate_email():
                error_message = "Invalid email format"
                vValid=1
                verr = verr + '<br>' + error_message
            if not user.validate_password():
                error_message = "Password must be at least 8 characters long, with at least one uppercase letter, one number, and one special character"
                vValid=1
                verr = verr + '<br>' + error_message          
            if user.email_exists(user.email):
                error_message = "Email is already registered"
                vValid=1
                verr = verr + '<br>' + error_message
      #en todos los demas casos en los que no es cero empezara desde aquí
        if not user.validate_age():
            error_message = "Age must be between 18 and 120"
            vValid=1
            verr = verr + '<br>' + error_message                 
        if not user.validate_dob():
            error_message = "Invalid date format for Date of Birth. Use YYYY-MM-DD"
            vValid=1
            verr = verr + '<br>' + error_message                
        if not user.validate_linkedin():
            error_message = "Invalid LinkedIn URL format"
            vValid=1
            verr = verr + '<br>' + error_message
                # Check if email is already registered
       
        return vValid, verr