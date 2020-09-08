from django import template

register = template.Library()


@register.filter
def sub(value, arg): # 기존 값(value)에서 입력으로 받은 값(arg)을 빼서 리턴하는 필터
    return value - arg