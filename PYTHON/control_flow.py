def admin_login(usename,password):
    admin_user = ["admin","ADMIN"]
    admin_pass = "12345"
    if usename in admin_user and password == admin_pass: # check if username is in the list and password matches
        print("Access granted")
    else:
        print("Access denied")

admin_login ("admin", "12345")
admin_login ("ADMIN", "12345")
admin_login ("user", "12345")



        