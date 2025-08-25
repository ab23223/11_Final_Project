from bottle import route, run, template, view, static_file


# Static file serving
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def index():
    return template('index')

@route('/whatisclimatechange')
def whatisclimatechange():
    return template('whatisclimatechange')

@route('/climatechangeissues')
def climatechangeissues():
    return template('climatechangeissues')


run(host='localhost', port=8080, debug=True, reloader=True)