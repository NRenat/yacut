from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField('Длинная ссылка', validators=(
        DataRequired(message='Обязательное поле'),
        Length(min=1, max=254, message='Ссылка слишком длинная')))
    custom_id = URLField('Ваш вариант короткой ссылки',
                         validators=(Length(min=0, max=16), Optional()))
    submit = SubmitField('Создать')
