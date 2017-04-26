from flask_wtf import FlaskForm
from wtforms import SelectField


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