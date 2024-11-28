# "Рассылка писем":

def send_email (message, recipient, *,sender = "university.help@gmail.com"): # message(сообщение), recipient(
# получатель)
    print(message, recipient, sender)
    if format(recipient) == False or format(sender) == False:
        print(f"Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}")
        return ()
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}")
    else:
         print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: {sender} на адрес: {recipient}")
    return ()

def format (email):
    flag_email = False
    domen = [".com", ".ru", ".net"]
    if "@" in email:
        for d in domen:
            if len(email)-email.find(d) == len(d):
                flag_email = True
                break
    return (flag_email)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


