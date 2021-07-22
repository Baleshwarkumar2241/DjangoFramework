from DoctorApp.models import Availibility
from django import template

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success text-white'
    return 'bg-danger text-white'   


@register.simple_tag
def get_availibilities(hospital):
    return Availibility.objects.filter(hospital=hospital).order_by('facility_id')



@register.simple_tag
def is_option_selected(selected_option, pk):
    if selected_option == str(pk):
        return 'selected'
    return ''    


