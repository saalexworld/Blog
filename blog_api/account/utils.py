from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    message = f'Congratulations! Вы зареганы на нашем сайте. Активируйте аккаунт, отправив нам этот код {activation_code}'

    send_mail(
        'Активация аккаутна',
        message,
        'sidorevichaa@gmail.com',
        [email]
    )
