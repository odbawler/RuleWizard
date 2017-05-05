from flask_wtf import Form
from wtforms import StringField, FieldList, FormField, TextField
from wtforms.validators import DataRequired

class RuleForm(Form):
    #addresses = FieldList(FormField(RuleEntryForm), min_entries=5)
    source = StringField('source', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    port = StringField('port', validators=[DataRequired()])
    source1 = StringField('source1')
    destination1 = StringField('destination1')
    port1 = StringField('port1')
    source2 = StringField('source2')
    destination2 = StringField('destination2')
    port2 = StringField('port2')
    source3 = StringField('source3')
    destination3 = StringField('destination3')
    port3 = StringField('port3')
    source4 = StringField('source4')
    destination4 = StringField('destination4')
    port4 = StringField('port4')
    source5 = StringField('source5')
    destination5 = StringField('destination5')
    port5 = StringField('port5')
    source6 = StringField('source6')
    destination6 = StringField('destination6')
    port6 = StringField('port6')
