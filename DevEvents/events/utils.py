from django.utils.text import camel_case_to_spaces

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])



def to_snake_case(camel_str):
    return camel_case_to_spaces(camel_str).replace(' ', '_')