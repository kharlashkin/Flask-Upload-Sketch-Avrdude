from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField
import glob

ports = glob.glob('/dev/tty[A-Za-z]*')

class Avrdude(FlaskForm):
    partno = SelectField('partno', choices=[('m328', 'ATmega328'),
                                               ('m328p', 'ATmega328P'),
                                               ('m168',	'ATmega168'),
                                               ('m168p', 'ATmega168P'),
                                               ('m2560', 'ATmega2560 (**)'),
                                               ('m32u4', 'ATmega32U4'),
                                               ('t85', 'ATtiny85')])
    baudrate = SelectField('baudrate', choices=[('9600', '9600'),
                                                ('19200', '19200'),
                                                ('38400', '38400'),
                                                ('57600', '57600'),
                                                ('74880', '74880'),
                                                ('115200', '115200'),
                                                ('230400', '230400'),
                                                ('250000', '250000')])
    programmer = SelectField('programmer', choices=[('avrisp', 'Atmel AVR ISP'),
                                                    ('avrispmkII', 'Atmel AVR ISP mkII'),
                                                    ('arduino', 'Arduino'),
                                                    ('usbtiny', 'USBtiny simple USB programmer'),
                                                    ('usbasp', 'USBasp')])
    sketch = FileField(validators=[FileRequired('No selected file'), FileAllowed(['hex'], 'Incorrect file format')])
    port = SelectField('port', choices=[(i, i) for i in ports])