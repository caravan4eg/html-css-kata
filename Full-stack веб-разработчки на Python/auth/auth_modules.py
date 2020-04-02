
def get_email_from_user(attempts=5, sleep_duration=15):
    email = input("Введите e-mail: ")
    i = 1
    # while (email.find("@") == -1):
    while not '@' in email:
        print("Неправильный email. Попробуйте ещё раз")
        i = i + 1
        email = input(f'Попытка {str(i)} из {attempts} Введите e-mail: ')
        if i % attempts == 0:
            print("Переборщили с попытками. Подождите " + str(sleep_duration)
                  + " секунд")
            time.sleep(sleep_duration)
    return email


def make_username(email):
    return email.split("@")[0].lower()
