AUTH_PW = "password"

def admin_login(pw):
        is_authenticated = False
        while is_authenticated == False:
                if pw == AUTH_PW:
                        print("Correct, password. You are authenticated.")
                        is_authenticated = True
                print("Correct, password. You are authenticated.")
                continue
        return False