from flask import Flask, render_template, request, flash, redirect
import forms
from flask_wtf.csrf import CSRFProtect
from werkzeug import secure_filename
import os, subprocess


app = Flask(__name__)
csrf = CSRFProtect(app)

app.secret_key = '9\xd8\xcc\xdb\x9d(\x94\xbex\xc4*\xd5\x17\xcet\xad\xc7\xe7i\x92\xaf\xf1x\xa8'

@app.route('/upload_sketch', methods=['GET', 'POST'])
def upload_sketch():
    form = forms.Avrdude()
    if form.validate_on_submit():
        partno = request.form['partno']
        port = request.form['port']
        baudrate = request.form['baudrate']
        programmer = request.form['programmer']
        sketch = form.sketch.data
        filename = secure_filename(sketch.filename)
        sketch.save(os.path.join('/kharlashkin/Flask/uploads', filename))
        cmd = 'avrdude -p ' + partno + ' -P ' + port + ' -b ' + baudrate + ' -c ' + programmer + ' -U flash:w:' + filename
        flash(cmd)
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
        while True:
            console = p.stdout.readline()
            if not console: break
            flash(console)
        os.remove('/kharlashkin/Flask/uploads' + '/' + filename)
        return redirect(request.url)
    elif form.errors:
        for fieldName, errorMessages in form.errors.iteritems():
            for error in errorMessages:
                flash(error)
        return redirect(request.url)
    return render_template('upload_sketch.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)