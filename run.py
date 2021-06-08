from flask import Flask
from flask import request
from flask import render_template
from flask import abort, url_for, make_response

app = Flask(__name__)
#mail= Mail(app)

#add pages here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
   # msg = Message('Hello', sender='kamilkarp22@gmail.com', recipients=['kamilkarp22@gmail.com'])
   # msg.body = "Hello Flask message sent from Flask-Mail"
   # mail.send(msg)
    return render_template('contact.html')
   # return "Sent"

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


#Errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

if __name__ == '__main__':
    app.run(debug=True)




