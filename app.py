from bottle import route, run, template, view, static_file


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def index():
    return template('index')

@route('/about')
def about():
    return template('about')

@route('/contact')
def contact():
    return template('contact')


run(host='localhost', port=8080, debug=True, reloader=True)