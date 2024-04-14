from django import template

register = template.Library()


@register.filter()
def my_media(data: str) -> str:
    """Функция для формирования полного пути к папке медиа"""
    if data:
        return f"/media/{data}"
    return f"/media/empty_avatar.jpg"
