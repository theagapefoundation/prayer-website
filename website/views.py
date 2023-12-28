from django.shortcuts import render


def handler404(request, *args, **argv):
    response = render(request, template_name="error_page.html")
    response.status_code = 200
    return response


def handler500(request, *args, **argv):
    response = render(request, template_name="error_page.html")
    response.status_code = 500
    return response
