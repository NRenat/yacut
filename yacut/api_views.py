from http import HTTPStatus

from flask import jsonify, request
from . import db, app
from .constants import MAX_LENGTH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_random_string, is_valid_custom_id


@app.route('/api/id/', methods=('POST',))
def get_unique_short_id_api():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса',
                              HTTPStatus.BAD_REQUEST)

    if not data.get('url'):
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if data.get('custom_id'):

        if len(data.get('custom_id')) > MAX_LENGTH or not is_valid_custom_id(
                data.get('custom_id')):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                HTTPStatus.BAD_REQUEST)

    else:
        data['custom_id'] = get_random_string()

    if URLMap.is_short_exists(data.get('custom_id')):
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.',
            HTTPStatus.BAD_REQUEST)

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=('GET',))
def get_original_url_api(short_id):
    short = URLMap.query.filter_by(short=short_id).first()
    print(short)
    if not short:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    url = short.original
    return jsonify({'url': url}), HTTPStatus.OK
