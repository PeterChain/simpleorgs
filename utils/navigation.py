from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Navigation:
    """
    Navigation building object
    """

    def get_member_nav(self):
        nav_arr = []

        nav_arr.append({
            'url':reverse('members:create'), 'icon':'pe-7s-add-user', 'title':'New member'
        })
        nav_arr.append({
            'url':reverse('members:list'), 'icon':'pe-7s-users', 'title':'Members list'
        })
        nav_arr.append({
            'url':'', 'icon':'pe-7s-gift', 'title':'Members Perks'
        })
        nav_arr.append({
            'url':reverse('address:book'), 'icon':'pe-7s-notebook', 'title':'Address Book'
        })

        return nav_arr