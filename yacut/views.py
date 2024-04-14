from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_random_string


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('yacut.html', form=form)

        url = URLMap(
            original=form.original_link.data,
            short=short if short else get_random_string(),
        )
        db.session.add(url)
        db.session.commit()
        return render_template('yacut.html', form=form, url=url)
    return render_template('yacut.html', form=form)


@app.route('/<short>')
def redirect_original(short):
    url = URLMap.query.filter_by(short=short).first()
    if url:
        return redirect(url.original)
    abort(HTTPStatus.NOT_FOUND)
