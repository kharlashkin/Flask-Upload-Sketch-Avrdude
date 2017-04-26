from flask import Flask, render_template, request, flash, redirect
import forms
from flask_wtf.csrf import CSRFProtect

ALLOWED_EXTENSIONS = set(['hex'])

app = Flask(__name__)
csrf = CSRFProtect(app)

app.secret_key = '9\xd8\xcc\xdb\x9d(\x94\xbex\xc4*\xd5\x17\xcet\xad\xc7\xe7i\x92\xaf\xf1x\xa8'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.Avrdude()
    if form.validate_on_submit():
         partno = request.form['partno']
         baudrate = request.form['baudrate']
         programmer = request.form['programmer']
         flash(partno + ' ' + baudrate + ' ' + programmer)
         return redirect(request.url)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)