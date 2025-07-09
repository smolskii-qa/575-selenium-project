translations = {
    'en': {
        'alert_success_add_to_basket': 'has been added to your basket',
        'alert_basket_total': 'Your basket total is now',
        'alert_empty_basket': 'Your basket is empty'
    },
    'ru': {
        'alert_success_add_to_basket': 'был добавлен в вашу корзину',
        'alert_basket_total': 'Стоимость корзины теперь составляет',
        'alert_empty_basket': 'Ваша корзина пуста'

    }
}


def get_text(key: str, language: str = 'en') -> str:
    """Возвращает перевод по языку и ключу"""
    return translations.get(language, {}).get(key, f'missing {language} translation: {key}')
