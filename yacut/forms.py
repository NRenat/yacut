import re

from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from .constants import MAX_ORIGIN_LENGTH, MAX_SHORT_LENGTH, MATCH_URL


class URLForm(FlaskForm):
    original_link = URLField('Длинная ссылка', validators=(
        DataRequired(message='Обязательное поле'),
        Length(min=1, max=MAX_ORIGIN_LENGTH,
               message='Ссылка слишком длинная')))
    custom_id = URLField('Ваш вариант короткой ссылки',
                         validators=(Length(max=MAX_SHORT_LENGTH), Optional()))
    submit = SubmitField('Создать')

    @staticmethod
    def is_valid_custom_id(custom_id):
        return bool(re.match(MATCH_URL, custom_id))
