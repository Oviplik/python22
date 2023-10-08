from app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('app/tree_menu.html')
def draw_menu(menu_title: str = None, menu_item: str = None):

    def get_menu(menu_item: str = None, submenu: list = None):
        menu = list(items.filter(parent=None)) if menu_item is None \
            else list(items.filter(parent__title=menu_item))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(title=menu_item).parent.title, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__title=menu_title)
    return {'menu': get_menu()} if menu_title == menu_item \
        else {'menu': get_menu(menu_item)}
