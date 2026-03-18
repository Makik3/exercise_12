def analyze_password(password, min_length=8, require_digit=True, require_upper=True, require_symbol, banned_words):
    count = 0
    symboly = [!@#$%^&*()-_=+[]{};:,.?]
    if len(str(password)) >= min_length:
        count += 1
    has_digit = any(i.isdigit() for i in password)
    has_upper = any(y.isupper() for y in password)
    has_symbol = any(a in password for a in symbol)

    if has_digit == True:
        count += 1

    if has_upper == True:
        count += 1







