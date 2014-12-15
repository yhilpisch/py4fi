#
# Valuation of European volatility options
# in Gruenbichler-Longstaff (1996) model
# square-root diffusion framework
# -- WSGI application for web service
#
from vol_pricing_service import get_option_value
from werkzeug.wrappers import Request, Response 
from werkzeug.serving import run_simple

def application(environ, start_response):
    request = Request(environ)
      # wrap environ in new object
    text = get_option_value(request.args)
      # provide all parameters of call to function
      # get back either error message or option value
    response = Response(text, mimetype='text/html')
      # generate response object based on the returned text
    return response(environ, start_response)

if __name__=='__main__':
    run_simple('localhost', 4000, application)