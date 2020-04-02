import time
from auth_modules import get_email_from_user, make_username


email = get_email_from_user()
username = make_username(email)
print(f"Вы вошли как {username}")
