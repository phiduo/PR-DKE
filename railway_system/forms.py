from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, RadioField, \
    SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NoneOf
from .models import User


class RegisterForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired(), Length(min=2, max=16)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField("Passwort wiederholen",
                                     validators=[DataRequired(), Length(min=8, max=16), EqualTo("password")])
    submit = SubmitField("Benutzer anlegen")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Benutzername bereits vergeben. Bitte einen anderen Benutzernamen wählen.")


class LoginForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired(), Length(min=2, max=16)])
    password = PasswordField("Passwort", validators=[DataRequired()])
    remember = BooleanField("Angemeldet bleiben")
    submit = SubmitField("Einloggen")


class StationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    state = StringField("Bundesland", validators=[DataRequired()])
    submit = SubmitField("Bestätigen")


GAUGE_CHOICES = [(1435, 'Normalspur (1435mm)'),
                 (1000, 'Schmalspur (1000mm)')]  # 1435mm = Normalspur, 1000mm = Schmalspur
class SectionForm(FlaskForm):
    starts_at = SelectField("Start", coerce=int, validators=[DataRequired()])
    ends_at = SelectField("Ende", coerce=int, validators=[DataRequired()])
    length = DecimalField("Länge", validators=[DataRequired()])
    user_fee = DecimalField("Nutzungsentgelt", validators=[DataRequired()])
    max_speed = IntegerField("Maximale Geschwindigkeit", validators=[DataRequired()])
    gauge = RadioField("Spurweite", choices=GAUGE_CHOICES, default='1435', validators=[DataRequired()])
    railway_id = SelectField("Strecken-Zuordnung (Optional)", coerce=int)
    submit = SubmitField("Bestätigen")

    def validate_ends_at(self, field):
        if field.data == self.starts_at.data:
            raise ValidationError("End-Bahnhof kann nicht gleichzeitig auch Start-Bahnhof sein.")


class RailwayForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    starts_at = SelectField("Start", coerce=int, validators=[DataRequired()])
    ends_at = SelectField("Ende", coerce=int, validators=[DataRequired()])
    #sections = SelectMultipleField("Zugeordnete Abschnitte (Optional)", coerce=int)  #TODO: check if selected sections already belong to another railway
    submit = SubmitField("Bestätigen")

    def validate_ends_at(self, field):
        if field.data == self.starts_at.data:
            raise ValidationError("End-Bahnhof kann nicht gleichzeitig auch Start-Bahnhof sein.")

    #def validate_sections(self, field):
    #    if len(field.data) > 1 and 0 in field.data:


class SectionAssignment1(FlaskForm):
    railway_id = SelectField("Strecke", coerce=int)
    submit = SubmitField("Wählen")


class SectionAssignment2(FlaskForm):
    railway_id = SelectField("Strecke", coerce=int)
    sections = SelectMultipleField("Abschnitt hinzufügen", coerce=int)  #TODO: check if selected sections already belong to another railway
    submit = SubmitField("Bestätigen")