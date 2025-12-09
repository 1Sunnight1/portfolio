import dns.resolver
from typing import List

def validate_domain_mx(email: str) -> str:
    """
    Проверка MX-записи домена email-адреса.
    """
    try:
        # извлечение домена из email
        domain = email.split('@')[1]
        
        # Проверка MX-записи
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return f"{email}: домен валиден"
        else:
            return f"{email}: MX-записи отсутствуют или некорректны"
            
    except dns.resolver.NXDOMAIN:
        return f"{email}: домен отсутствует"
    except dns.resolver.NoAnswer:
        return f"{email}: MX-записи отсутствуют или некорректны"
    except IndexError:
        return f"{email}: некорректный формат email"
    except Exception:
        return f"{email}: ошибка проверки"

def main():
    """Основная функция для обработки списка email-адресов."""
    print("Проверка MX-записей доменов email-адресов")
    print("Введите email-адреса (по одному на строку, пустая строка для завершения):")
    print("-" * 50)
    
    emails: List[str] = []
    
    while True:
        email = input("Email: ").strip()
        if not email:  # Пустая строка = завершение
            break
        emails.append(email)
    
    if not emails:
        print("Не введено ни одного email-адреса.")
        return
    
    print("\nРезультаты проверки:")
    print("-" * 50)
    
    for email in emails:
        status = validate_domain_mx(email)
        print(status)

if __name__ == "__main__":
    main()
