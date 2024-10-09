def validate_mail(email):
    if '@' in email and '.' in email and email.index('@')<email.index('.'):
        print(f'メールアドレスは{email}')
    else :
        print('無効なメールアドレスです。')

email = input('メールアドレスを入力してください：')

validate_mail(email)