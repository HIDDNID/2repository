from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Замените на ваш собственный секретный ключ

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update')

@app.route('/edit_profile', methods=['GET', 'POST'])  # Обратите внимание на точное название маршрута
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь можно обрабатывать данные формы, например, обновление в базе данных
        print("Form submitted successfully!")
    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
